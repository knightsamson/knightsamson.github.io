import csv
import requests

url = ('https://newsapi.org/v2/everything?'
       'q=Tesla&'
       'from=2023-06-20&'
       'sortBy=popularity&'
       'language=en&'
       'apiKey=1f3cebfb0b314af7af6ceb0fb278c122')

response = requests.get(url)
data = response.json()

# Check if the request was successful
if response.status_code == 200:
    articles = data['articles']
    
    with open('articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Source', 'Description'])
        
        for article in articles:
            title = article['title']
            source = article['source']['name']
            description = article['description']
            
            writer.writerow([title, source, description])

    print("Articles saved successfully!")
else:
    print("Error:", data['message'])
