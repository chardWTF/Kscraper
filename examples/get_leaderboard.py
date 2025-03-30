from Kscraper import Client

client = Client()
username = "example_user"
leaderboard = client.get_leadboard(username)
print(leaderboard)
