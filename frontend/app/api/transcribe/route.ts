import { generateText } from "ai"

export async function POST(request: Request) {
  try {
    const formData = await request.formData()
    const audioFile = formData.get("audio") as File

    if (!audioFile) {
      return Response.json({ error: "No audio file provided" }, { status: 400 })
    }

    // Convert audio to base64 for API
    const buffer = await audioFile.arrayBuffer()
    const base64Audio = Buffer.from(buffer).toString("base64")

    // Use AI SDK to transcribe (requires audio model support)
    const { text } = await generateText({
      model: "openai/gpt-4-turbo",
      prompt: `Transcribe this audio (base64): ${base64Audio}`,
      system: "You are a transcription assistant. Transcribe the audio accurately.",
    })

    return Response.json({ text })
  } catch (error) {
    console.error("Transcription error:", error)
    return Response.json({ error: "Transcription failed" }, { status: 500 })
  }
}
