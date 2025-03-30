from Kscraper import Client

client = Client()
top_category = client.get_top_category()
print(top_category)
