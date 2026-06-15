#!/usr/bin/env python3
"""Minimal Claude Fable 5 Messages API example through EvoLink."""

import json
import os
import urllib.request


API_KEY = os.environ["EVOLINK_API_KEY"]
URL = "https://direct.evolink.ai/v1/messages"

payload = {
    "model": "claude-fable-5",
    "max_tokens": 1024,
    "messages": [
        {
            "role": "user",
            "content": "Review this repository plan and list the top three engineering risks.",
        }
    ],
}

request = urllib.request.Request(
    URL,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=120) as response:
    print(response.read().decode("utf-8"))
