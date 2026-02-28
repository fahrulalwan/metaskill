# scripts/llm_transfer.py
import sys, json, os

def get_analogous_principles(task_desc, learnings_content):
    prompt = f"""Given this task:
"{task_desc}"

Which of these past learnings are analogically relevant? Explain the connection. Return ONLY valid JSON in this format:
{{"principles": [{{"principle": "...", "reasoning": "..."}}]}}

Past learnings:
{learnings_content}"""

    # Try Anthropic first
    try:
        import anthropic
        client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        msg = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(msg.content[0].text)
    except Exception as e:
        pass
    
    # Try OpenAI
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return json.loads(resp.choices[0].message.content)
    except Exception as e:
        pass
    
    return None

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("FALLBACK")
        sys.exit(0)
    
    task_desc = sys.argv[1]
    learnings_file = sys.argv[2]
    
    try:
        with open(learnings_file, "r") as f:
            content = f.read()
            
        # Extract just the headers + first 2 lines of each entry
        lines = content.split('\n')
        extracted_lines = []
        capture = 0
        for line in lines:
            if line.startswith('## '):
                capture = 3
            if capture > 0:
                extracted_lines.append(line)
                capture -= 1
        
        extracted_content = '\n'.join(extracted_lines)
    except Exception as e:
        print("FALLBACK")
        sys.exit(0)

    result = get_analogous_principles(task_desc, extracted_content)
    if result:
        print(json.dumps(result))
    else:
        print("FALLBACK")
