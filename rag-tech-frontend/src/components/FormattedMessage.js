import React from "react";

export default function FormattedMessage({ text }) {
  if (!text) return null;

  // Convert special formatting
  const formatted = text
    .replace(/```([\s\S]*?)```/g, "<pre class='code-block'>$1</pre>")
    .replace(/\n/g, "<br>")
    .replace(/\*\*(.*?)\*\*/g, "<b>$1</b>")
    .replace(/^- (.*)/gm, "<li>$1</li>")
    .replace(/\n\n/g, "<br><br>");

  return (
    <div
      className="formatted-text"
      dangerouslySetInnerHTML={{ __html: formatted }}
    />
  );
}
