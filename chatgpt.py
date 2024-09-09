from openai import OpenAI


def run_chat_completion(api_key: str, prompt: list, history=[]):
    client = OpenAI(api_key=api_key)
    # history += prompt
    respond = client.chat.completions.create(
        messages=prompt,
        model="gpt-4o",
        temperature=0,
        # response_format= {"type":"json_object"},
    )
    # history.append({"role":"assistant", "content":respond.choices[0].message.content})
    # ans_JSON = []
    # ans_JSON.append(json.loads(respond.choices[0].message.content or {}))
    # print(history[-1]['content'])
    return respond
