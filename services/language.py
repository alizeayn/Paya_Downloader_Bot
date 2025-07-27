import json
import os 

messages =  {}

def load_locales():
    try:
        with open("locales/fa.json", "r", encoding="utf-8") as f:
            messages["fa"] = json.load(f)
        with open("locales/en.json", "r", encoding="utf-8") as f:
            messages["en"] = json.load(f)
    except FileNotFoundError:
        print("Error: Locale file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format!")

def get_message(language: str, key: str) -> str:
    if not messages:
        load_locales()
    if language not in messages:
        return "Message not found!"
    return messages.get(language, {}).get(key, "Message not found!")

if __name__ == "__main__":
    print(get_message("en", "welcome"))