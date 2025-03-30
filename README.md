![Kscraper Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Kick.com_icon_logo.svg/1200px-Kick.com_icon_logo.svg.png) Kscraper

Kscraper is a Python package for interacting with Kick.com APIs. It allows you to fetch emotes, leaderboards, messages, polls, and more.

## Installation

```bash
pip install Kscraper
```

## Usage

```python
from Kscraper import Client

client = Client()

# Get emotes for a user
emotes = client.get_emotes("example_user")
print(emotes)

# Get leaderboard
leaderboard = client.get_leadboard("example_user")
print(leaderboard)

# Get messages from a channel
messages = client.get_messages(123456)
print(messages)
```

## Available Methods

- `get_emotes(username: str)`: Fetch emotes for a user.
- `get_leadboard(username: str)`: Fetch leaderboard data.
- `get_messages(user_id: int)`: Fetch chat messages from a channel.
- `get_current_poll(username: str)`: Fetch the current poll for a channel.
- `get_top_category()`: Fetch the top category on Kick.com.
- `get_featured_streams()`: Fetch featured livestreams.
- `get_channel(username: str)`: Fetch channel details.
- `get_chatroom(username: str)`: Fetch chatroom details.
- `get_rules(username: str)`: Fetch chatroom rules.
- `send_chat(user_id: int, token: str, content: str)`: Send a chat message.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Author

Your Name - [GitHub](https://github.com/chardWTF)
