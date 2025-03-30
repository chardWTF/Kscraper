from Kscraper import Client

client = Client()
username = "example_user"
poll = client.get_current_poll(username)
print(poll)
