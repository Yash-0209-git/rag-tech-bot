export async function askBackend(question) {
  try {
    const response = await fetch("http://127.0.0.1:8000/ask", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ question }),
    });

    if (!response.ok) {
      throw new Error("Backend returned an error");
    }

    const data = await response.json();
    return data.answer;

  } catch (error) {
    console.error("Backend error:", error);
    return "Error: Cannot reach backend. Make sure it's running.";
  }
}
