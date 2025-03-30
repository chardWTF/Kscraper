from Kscraper import Client

client = Client()
username = "example_user"
rules = client.get_rules(username)
print(rules)
