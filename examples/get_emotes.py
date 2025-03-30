from Kscraper import Client

client = Client()
username = "example_user"
emotes = client.get_emotes(username)
print(emotes)
