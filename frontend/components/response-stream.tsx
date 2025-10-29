interface ResponseStreamProps {
  content: string
}

export default function ResponseStream({ content }: ResponseStreamProps) {
  return (
    <div className="bg-card border border-border rounded-lg p-3 sm:p-4 max-h-64 sm:max-h-96 overflow-y-auto">
      <p className="text-foreground text-xs sm:text-sm leading-relaxed whitespace-pre-wrap">{content}</p>
    </div>
  )
}
