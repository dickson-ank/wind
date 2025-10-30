"use client";

import type React from "react";
import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui/button";
import { convertWebmToWav } from "@/lib/convert-wav"
import { Mic } from "lucide-react";

interface InputFormProps {
  onSubmit: (input: string) => void;
  isLoading: boolean;
}

export default function InputForm({ onSubmit, isLoading }: InputFormProps) {
  const [text, setText] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [inputMode, setInputMode] = useState<"audio" | "text">("audio");
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  useEffect(() => {
    startRecording();
  }, []);

  useEffect(() => {
    if (inputMode === "text" && isRecording) {
      stopRecording();
    }
  }, [inputMode]);

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      chunksRef.current = [];

      mediaRecorder.ondataavailable = (e) => chunksRef.current.push(e.data);
      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(chunksRef.current, { type: "audio/webm" });
        await transcribeAudio(audioBlob);
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorder.start();
      setIsRecording(true);
    } catch (err) {
      console.error("Microphone access denied:", err);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  const transcribeAudio = async (audioBlob: Blob) => {
    try {
      const wavBlob = await convertWebmToWav(audioBlob);

      const formData = new FormData();
      formData.append("audio", wavBlob, "recording.wav");

      const res = await fetch("/api/transcribe", {
        method: "POST",
        body: formData,
      });

      if (!res.ok) throw new Error("Transcription failed");

      const data = await res.json();
      setText(data.text);
    } catch (err) {
      console.error("Transcription error:", err);
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (text.trim() && !isLoading) {
      onSubmit(text);
      setText("");
    }
  };

  const handleModeSwitch = (mode: "audio" | "text") => {
    setInputMode(mode);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 sm:space-y-6">
      {inputMode === "audio" ? (
        <>
          <div className="flex flex-col items-center justify-center gap-4 py-6 sm:py-8">
            {/* Recording indicator with animation */}
            <div className="relative w-20 h-20 sm:w-24 sm:h-24 flex items-center justify-center">
              {isRecording && (
                <>
                  <div className="absolute inset-0 bg-primary/20 rounded-full animate-pulse"></div>
                  <div
                    className="absolute inset-2 bg-primary/10 rounded-full animate-pulse"
                    style={{ animationDelay: "0.2s" }}
                  ></div>
                </>
              )}
              <div
                className={`relative z-10 w-16 h-16 sm:w-20 sm:h-20 rounded-full flex items-center justify-center transition-all ${
                  isRecording
                    ? "bg-primary text-primary-foreground shadow-lg shadow-primary/50"
                    : "bg-muted text-muted-foreground border-2 border-border"
                }`}
              >
                <Mic className="w-8 h-8 sm:w-10 sm:h-10" />
              </div>
            </div>

            {/* Status text */}
            <div className="text-center">
              <p className="text-sm sm:text-base font-medium text-foreground">
                {isRecording ? "Listening..." : "Recording stopped"}
              </p>
            </div>
          </div>

          {/* Transcribed text display */}
          {text && (
            <div className="bg-input border border-border rounded-lg px-4 sm:px-5 py-3 sm:py-4">
              <p className="text-xs sm:text-sm text-muted-foreground mb-2">
                Transcribed:
              </p>
              <p className="text-sm sm:text-base text-foreground text-balance">
                {text}
              </p>
            </div>
          )}

          {/* Controls */}
          <div className="flex gap-2 sm:gap-3 justify-center">
            <Button
              type="button"
              onClick={isRecording ? stopRecording : startRecording}
              disabled={isLoading}
              className={`px-6 sm:px-8 ${
                isRecording
                  ? "bg-red-500/20 border border-red-500/50 text-red-400 hover:bg-red-500/30"
                  : "bg-primary text-primary-foreground hover:bg-primary/90"
              }`}
            >
              {isRecording ? "Stop" : "Resume"}
            </Button>
            <Button
              type="submit"
              disabled={!text.trim() || isLoading}
              className="px-6 sm:px-8 bg-primary text-primary-foreground hover:bg-primary/90 disabled:opacity-50"
            >
              Send
            </Button>
          </div>
          <Button
            type="button"
            onClick={() => handleModeSwitch("text")}
            variant="outline"
            className="px-6 sm:px-8 border-border text-foreground hover:bg-muted"
          >
            Text
          </Button>
        </>
      ) : (
        <>
          {/* Text input mode */}
          <div className="flex flex-col sm:flex-row gap-2 sm:gap-3">
            <input
              type="text"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Enter your query..."
              disabled={isLoading}
              className="flex-1 bg-input border border-border rounded-lg px-4 sm:px-5 py-3 sm:py-4 text-sm text-foreground placeholder-muted-foreground focus:outline-none focus:ring-2 focus:ring-primary disabled:opacity-50"
            />
            <Button
              type="submit"
              disabled={!text.trim() || isLoading}
              className="w-full sm:w-auto px-6 sm:px-8 bg-primary text-primary-foreground hover:bg-primary/90 disabled:opacity-50"
            >
              Send
            </Button>
          </div>

          {/* Switch back to audio */}
          <div className="flex justify-center">
            <Button
              type="button"
              onClick={() => handleModeSwitch("audio")}
              variant="outline"
              className="border-border text-foreground hover:bg-muted"
            >
              <Mic className="w-4 h-4 mr-2" />
              Back to Audio
            </Button>
          </div>
        </>
      )}
    </form>
  );
}
