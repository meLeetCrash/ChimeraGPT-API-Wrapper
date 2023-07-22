import requests


class Models:
    GPT_4 = "gpt-4"


class Assistant:
    def __init__(self, token: str, model: Models = Models.GPT_4):
        self.token = token
        self.model = model

    def ask(self, request: str):
        try:
            response = requests.get(
                url="https://chimeragpt.adventblocks.cc/v1/chat/completions",
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                  "Chrome/114.0.0.0 Safari/537.36",
                    "Referer": "https://chimeragpt.adventblocks.cc/",
                    "Content-Type": "application/json",
                    "Connection": "keep-alive",
                    "Authorization": f"Bearer {self.token}",
                },
                json={
                    "model": self.model,
                    "messages": [
                        {
                            'role': "user",
                            "content": request
                        }
                    ]
                }
            )
            return response.json()['choices'][0]['message']['content']
        except:
            pass
