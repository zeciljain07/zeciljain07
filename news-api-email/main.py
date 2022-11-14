import requests
from send_email import send_email

topic = "tesla"

api_key = "5d2f67d5129e4c64a3621c134bfc92d8"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      "apiKey=5d2f67d5129e4c64a3621c134bfc92d8&" \
      "language=en"

# Make request
requests = requests.get(url)

# Get a dictionary with data
content = requests.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's News" + "\n" \
               + body + article["title"] \
               + "\n" + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
