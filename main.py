import os
import requests

class SportsCoachingAI:
    def __init__(self):
        self.api_key = os.getenv('GEMINI_API_KEY')
        self.base_url = "https://api.gemini.com/v1"

    def get_coaching_tips(self, sport):
        response = requests.get(f"{self.base_url}/coaching_tips/{sport}", headers={"Authorization": f"Bearer {self.api_key}"})
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code} {response.text}")

if __name__ == '__main__':
    coaching_ai = SportsCoachingAI()
    tips = coaching_ai.get_coaching_tips('soccer')  # Example usage for soccer
    print(tips)