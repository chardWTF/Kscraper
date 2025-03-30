from Kscraper import Client  # Import the Client class

# Create an instance of the Client class
client = Client()

# Call the get_emotes method on the instance
channel = client.get_channel(username="chard0") # get the channel JSON
user_id = channel["user_id"]
response = client.send_chat(user_id ="12345", token="token", content="content") # grab the bearer token from your browser and put in the part after Bearer
print(response)
