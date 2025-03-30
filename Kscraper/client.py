from tls_client import Session
import time, asyncio, random, string, datetime, requests


class Client:
    def __init__(self):
        self.session = Session(client_identifier="chrome_112", random_tls_extension_order=True)
        self.session.headers = {
    "accept": "application/json",
    "accept-language": "en-GB,en;q=0.8",
    "cache-control": "max-age=0",
    "cluster": "v2",
    "priority": "u=1, i",
    "sec-ch-ua": "\"Chromium\";v=\"112\", \"Not:A-Brand\";v=\"24\"",
    "sec-ch-ua-arch": "\"x86\"",
    "sec-ch-ua-bitness": "\"64\"",
    "sec-ch-ua-full-version-list": "\"Chromium\";v=\"112.0.0.0\", \"Not:A-Brand\";v=\"24.0.0.0\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-model": "\"\"",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-ch-ua-platform-version": "\"10.0.0\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
}
    def get_emotes(self, username: str):
        while True:
            r = self.session.get(f"https://kick.com/emotes/{username}")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_leadboard(self, username: str):
        while True:
            r = self.session.get(f"https://kick.com/api/v2/channels/{username}/leaderboards")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_messages(self, user_id: int):
        while True:
            r = self.session.get(f"https://kick.com/api/v2/channels/{user_id}/messages")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_current_poll(self, username: str):
        while True:
            r = self.session.get(f"https://kick.com/api/v2/channels/{username}/polls")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_top_category(self):
        while True:
            r = self.session.get("https://kick.com/api/v1/categories/top")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_featured_streams(self):
        while True:
            r = self.session.get("https://kick.com/stream/featured-livestreams/en")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_channel(self, username: str):
        while True:
            r = self.session.get(f"https://kick.com/api/v2/channels/{username}/")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def get_chatroom(self, username: str):
        while True:
            r = self.session.get(f"https://kick.com/api/v2/channels/{username}/chatroom")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()

    def get_rules(self, username: str):
        while True:
            r = self.session.get(f"https://kick.com/api/v2/channels/{username}/chatroom/rules")
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                r.raise_for_status()
    def send_chat(self, user_id: int, token: str, content: str):
        while True:
            self.session.headers.update({
                "authorization": "Bearer " + token
            })
            json = {
                "content": content,
                "type": "message"
            }
            r = self.session.post(f"https://kick.com/api/v2/messages/send/{user_id}", json=json)
            if r.status_code == 200:
                return r.json()
            elif r.status_code == 403:
                print("cloudflared retrying")
                time.sleep(2)
            else:
                print(r.status_code, r.text)
    