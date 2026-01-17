---
title: "Autonomous Agents"
description: "From Chatbots to Agents that DO things."
---

# Autonomous Agents

A Chatbot answers. An Agent acts.

## The ReAct Pattern (Reason + Act)

Instead of just generating text, the model enters a loop:
1.  **Thought**: "I need to find the weather in Tokyo."
2.  **Action**: `call_weather_api("Tokyo")`
3.  **Observation**: "It is 25 degrees Celsius."
4.  **Thought**: "I have the answer."
5.  **Final Answer**: "It is 25C in Tokyo."

## Tools

Agents need tools (functions) to interact with the world:
*   Search the web.
*   Read files.
*   Execute code.
*   Send emails.

See `code/basic_agent.py`.
