from src.BRAIN.lm_ai import client


def chat_bot(initial_prompt , model="Lewdiculous/Eris_PrimeV4-Vision-32k-7B-GGUF-IQ-Imatrix" , temperature=0.7):
    history = [
        {"role": "system", "content": "You are JARVIS, Tony Stark's intelligent assistant. You are highly efficient, incredibly knowledgeable, and always provide well-reasoned answers that are both correct and helpful. You maintain a professional, yet personable tone, and your responses are characterized by your advanced intelligence and wit."},
        {"role": "user", "content": initial_prompt},
    ]

    while True:
        try:
            completion = client.chat.completions.create(
                model=model,
                messages=history,
                temperature=temperature,
                stream=True,
            )

            new_message = {"role": "assistant", "content": ""}
            
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    print(chunk.choices[0].delta.content, end="", flush=True)
                    new_message["content"] += chunk.choices[0].delta.content

            history.append(new_message)

            # Uncomment to see chat history
            # print(f"\033[90m\n{'-'*20} History dump {'-'*20}\n")
            # print(json.dumps(history, indent=2))
            # print(f"\n{'-'*55}\n\033[0m")

            print()
            user_input = input("> ")
            if user_input.lower() in ['exit', 'quit','end']:
                break
            history.append({"role": "user", "content": user_input})
        
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    return 


def send_to_ai(prompt, role, max_token = 2000 , model="Lewdiculous/Eris_PrimeV4-Vision-32k-7B-GGUF-IQ-Imatrix"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=max_token,
            top_p=1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    role =  "you are the refined email writer use shorter subject. write a email without changing any given personal details."
    prompt = "get leave from the office , boss name : harry , my_email = ganeshnikhil123 , cause : headache , holiday : 3 day , location : begusarai hemra"
    ans = send_to_ai(prompt , role)
    print(ans)
# Example usage:
# chat_bot()
# print(send_to_ai("Hello, how are you?", "You are an assistant"))
