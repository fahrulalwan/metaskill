# scripts/llm_extract.py
import sys, json, os

def extract_levels(error_desc):
    # Try Anthropic first
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        msg = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[{"role": "user", "content": f"""Extract 3 correction levels from this error/mistake:

"{error_desc}"

Return ONLY valid JSON:
{{"surface": "what specifically went wrong in this instance", "principle": "the underlying rule or mental model that was violated", "habit": "the concrete behavioral change that prevents recurrence"}}"""}]
        )
        return json.loads(msg.content[0].text)
    except:
        pass
    
    # Try OpenAI
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f'Extract 3 correction levels from: "{error_desc}". Return JSON: {{"surface": "...", "principle": "...", "habit": "..."}}'}]
        )
        return json.loads(resp.choices[0].message.content)
    except:
        pass
    
    return None

if __name__ == "__main__":
    error = " ".join(sys.argv[1:])
    result = extract_levels(error)
    if result:
        print(json.dumps(result))
    else:
        print("FALLBACK")
