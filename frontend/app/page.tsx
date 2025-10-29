"use client";

import { useState } from "react";
import InputForm from "@/components/input-form";
import ResponseStream from "@/components/response-stream";

export default function Home() {
  const [response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (input: string) => {
    setError("");
    setResponse("");
    setIsLoading(true);

    try {
      const res = await fetch("/api/query", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query: input }),
      });

      if (!res.ok) throw new Error("Request failed");

      const reader = res.body?.getReader();
      const decoder = new TextDecoder();

      if (!reader) throw new Error("No response body");

      let fullResponse = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value);
        fullResponse += chunk;
        setResponse(fullResponse);
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-background flex items-center justify-center p-4 sm:p-6 lg:p-8">
      <div className="w-full max-w-2xl">
        <div className="space-y-6 sm:space-y-8">
          <div className="text-center">
            <p className="text-xs sm:text-sm text-muted-foreground mt-2">
              Audio or text input with streamed responses
            </p>
          </div>

          <InputForm onSubmit={handleSubmit} isLoading={isLoading} />

          {error && (
            <div className="bg-red-500/10 border border-red-500/20 rounded-lg p-3 sm:p-4 text-red-400 text-xs sm:text-sm">
              {error}
            </div>
          )}

          {response && <ResponseStream content={response} />}
        </div>
      </div>
    </main>
  );
}
