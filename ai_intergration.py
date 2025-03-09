import os
import requests
from typing import Optional

class AIGenerator:
    def __init__(self, api_key: str = None, service: str = "openrouter"):
        self.api_key = api_key or os.getenv("AI_API_KEY")
        self.service = service
        self.endpoints = {
            "openrouter": "https://openrouter.ai/api/v1/chat/completions",
            "custom": "https://your-custom-api.com/v1/generate"
        }

    def generate_documentation(self, project_name: str, prompt: str) -> Optional[str]:
        """Генерация документации через ИИ"""
        try:
            response = requests.post(
                self.endpoints[self.service],
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4" if self.service == "openrouter" else "default",
                    "messages": [{
                        "role": "user",
                        "content": f"Создай документацию для проекта {project_name}. {prompt}"
                    }]
                }
            )
            return response.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(f"AI Error: {str(e)}")
            return None0