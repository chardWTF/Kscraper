from Kscraper import Client

client = Client()
user_id = 123456
messages = client.get_messages(user_id)
print(messages)
