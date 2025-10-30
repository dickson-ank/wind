/**
 * Converts a WebM audio blob to WAV format
 * @param webmBlob - The WebM audio blob to convert
 * @returns Promise that resolves to a WAV blob
 */
export async function convertWebmToWav(webmBlob: Blob): Promise<Blob> {
  // Create an audio context
  const audioContext = new (window.AudioContext ||
    (window as any).webkitAudioContext)();

  // Read the WebM blob as an array buffer
  const arrayBuffer = await webmBlob.arrayBuffer();

  // Decode the audio data
  const audioBuffer = await audioContext.decodeAudioData(arrayBuffer);

  // Convert to WAV
  const wavBlob = audioBufferToWav(audioBuffer);

  // Close the audio context to free up resources
  await audioContext.close();

  return wavBlob;
}

/**
 * Converts an AudioBuffer to a WAV blob
 * @param audioBuffer - The AudioBuffer to convert
 * @returns WAV blob
 */
function audioBufferToWav(audioBuffer: AudioBuffer): Blob {
  const numberOfChannels = audioBuffer.numberOfChannels;
  const sampleRate = audioBuffer.sampleRate;
  const format = 1; // PCM
  const bitDepth = 16;

  // Interleave channels
  const length = audioBuffer.length * numberOfChannels * 2;
  const buffer = new ArrayBuffer(44 + length);
  const view = new DataView(buffer);
  const channels: Float32Array[] = [];
  let offset = 0;
  let pos = 0;

  // Write WAV header
  setString(view, pos, "RIFF");
  pos += 4;
  view.setUint32(pos, 36 + length, true);
  pos += 4;
  setString(view, pos, "WAVE");
  pos += 4;
  setString(view, pos, "fmt ");
  pos += 4;
  view.setUint32(pos, 16, true);
  pos += 4; // Subchunk1Size (16 for PCM)
  view.setUint16(pos, format, true);
  pos += 2; // AudioFormat (1 for PCM)
  view.setUint16(pos, numberOfChannels, true);
  pos += 2;
  view.setUint32(pos, sampleRate, true);
  pos += 4;
  view.setUint32(pos, (sampleRate * numberOfChannels * bitDepth) / 8, true);
  pos += 4; // ByteRate
  view.setUint16(pos, (numberOfChannels * bitDepth) / 8, true);
  pos += 2; // BlockAlign
  view.setUint16(pos, bitDepth, true);
  pos += 2;
  setString(view, pos, "data");
  pos += 4;
  view.setUint32(pos, length, true);
  pos += 4;

  // Get channel data
  for (let i = 0; i < numberOfChannels; i++) {
    channels.push(audioBuffer.getChannelData(i));
  }

  // Write interleaved audio data
  offset = 44;
  for (let i = 0; i < audioBuffer.length; i++) {
    for (let channel = 0; channel < numberOfChannels; channel++) {
      const sample = Math.max(-1, Math.min(1, channels[channel][i]));
      view.setInt16(
        offset,
        sample < 0 ? sample * 0x8000 : sample * 0x7fff,
        true
      );
      offset += 2;
    }
  }

  return new Blob([buffer], { type: "audio/wav" });
}

/**
 * Helper function to write a string to a DataView
 */
function setString(view: DataView, offset: number, str: string): void {
  for (let i = 0; i < str.length; i++) {
    view.setUint8(offset + i, str.charCodeAt(i));
  }
}
