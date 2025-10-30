// app/api/transcribe/route.ts
import { NextRequest, NextResponse } from "next/server";

const invokeUrl = "https://integrate.api.nvidia.com/v1/chat/completions";

export async function POST(req: NextRequest) {
  try {
    const formData = await req.formData();
    const audioFile = formData.get("audio") as File;

    if (!audioFile) {
      return NextResponse.json(
        { error: "No audio file provided" },
        { status: 400 }
      );
    }

    // Convert file to base64
    const audioBuffer = await audioFile.arrayBuffer();
    const audio_b64 = Buffer.from(audioBuffer).toString("base64");

    const headers = {
      Authorization: `Bearer ${process.env.API_KEY}`,
      "Content-Type": "application/json",
    };

    const payload = {
      model: "google/gemma-3n-e4b-it",
      messages: [
        {
          role: "user",
          content: `Transcribe the following speech segment in English: <audio src="data:audio/wav;base64,${audio_b64}" />`,
        },
      ],
      max_tokens: 512,
      temperature: 0.2,
      top_p: 0.7,
      frequency_penalty: 0.0,
      presence_penalty: 0.0,
      stream: false,
    };

    const response = await fetch(invokeUrl, {
      method: "POST",
      headers: headers,
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      console.error("NVIDIA API error:", errorText);
      return NextResponse.json(
        { error: "Transcription service error" },
        { status: response.status }
      );
    }

    const data = await response.json();
    const transcribedText = data.choices?.[0]?.message?.content || "";

    return NextResponse.json({ text: transcribedText });
  } catch (error) {
    console.error("Transcription error:", error);
    return NextResponse.json(
      { error: "Internal server error" },
      { status: 500 }
    );
  }
}