const apiKey = process.env.EVOLINK_API_KEY;

if (!apiKey) {
  throw new Error("Set EVOLINK_API_KEY before running this example.");
}

const response = await fetch("https://direct.evolink.ai/v1/messages", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "claude-fable-5",
    max_tokens: 1024,
    messages: [
      {
        role: "user",
        content:
          "Review this repository plan and list the top three engineering risks.",
      },
    ],
  }),
});

if (!response.ok) {
  throw new Error(`${response.status} ${await response.text()}`);
}

console.log(JSON.stringify(await response.json(), null, 2));
