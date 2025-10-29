import axios from "axios";
import { readFile } from "node:fs/promises";

const invokeUrl = "https://integrate.api.nvidia.com/v1/chat/completions";
const stream = true;

const headers = {
  Authorization:
    
};

export const client = Promise.all([
  Promise.resolve(null),
  readFile("audio.wav"),
])
  .then(([imgData, audioData]) => {
    const audio_b64 = Buffer.from(audioData).toString("base64");

    const payload = {
      model: `google/gemma-3n-e4b-it`,
      messages: [
        {
          role: "user",
          content: `Transcribe the following speech segment in English: <audio src=\"data:audio/wav;base64,${audio_b64}\" />`,
        },
      ],
      max_tokens: 512,
      temperature: 0.2,
      top_p: 0.7,
      frequency_penalty: 0.0,
      presence_penalty: 0.0,
      stream: stream,
    };

    return axios.post(invokeUrl, payload, {
      headers: headers,
      responseType: stream ? "stream" : "json",
    });
  })
  .then((response) => {
    if (stream) {
      response.data.on("data", (chunk) => {
        console.log(chunk.toString());
      });
    } else {
      console.log(JSON.stringify(response.data));
    }
  })
  .catch((error) => {
    console.error(error);
  });
