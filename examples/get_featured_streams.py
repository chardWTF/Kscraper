from Kscraper import Client

client = Client()
featured_streams = client.get_featured_streams()
print(featured_streams)
