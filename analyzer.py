import openai
import os
import sys

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_log(log_text):
    prompt = f"""
    Analyze and classify this cybersecurity log entry. Provide:
    - Incident Type
    - Brief Summary
    - Recommended Immediate Actions

    LOG:
    {log_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    print(response.choices[0].message.content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]
    with open(logfile, 'r') as file:
        log_data = file.read()

    analyze_log(log_data)
