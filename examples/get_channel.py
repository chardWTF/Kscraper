from Kscraper import Client

client = Client()
username = "example_user"
channel = client.get_channel(username)
print(channel)
