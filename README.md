# AI-powered Log Analyzer

A lightweight cybersecurity tool that uses OpenAI's GPT-3.5 to analyze log files, detect incidents like brute-force attacks, and suggest immediate action items.

---

## Features

- **AI-Powered Analysis**: Uses ChatGPT to analyze logs and summarize incidents.
- **Classifies Threats**: Brute force, malware attempts, unauthorized access, etc.
- **Auto-Execution Support**: Can run on a schedule via cron.
- **Modular & Lightweight**: Built using Python and runs in Termux.

---

## How It Works

1. Reads system or application logs.
2. Sends the logs to the OpenAI API.
3. Receives a structured security incident report.

---

## Usage

```bash
python analyzer.py sample.log
