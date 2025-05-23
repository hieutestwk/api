from llama_cpp import Llama

class ChatBot:
    def __init__(self):
        self.model = Llama(model_path="models/tinyllama-1.1b-chat-v1.0.Q2_K.gguf")

    def ask(self, prompt):
        full_prompt = (
            "You are an English tutor. Correct grammar/spelling mistakes, "
            "and explain difficult words.\n"
            f"Student said: '{prompt}'"
        )
        response = self.model(full_prompt, max_tokens=256)
        text = response.get('choices', [{}])[0].get('text', '').strip()

        if not text:
            text = "Sorry, I didn't understand that."
        else:
            text = text.replace("Student said:", "").strip()

        print(f"🤖 Bot: {text}")
        return text