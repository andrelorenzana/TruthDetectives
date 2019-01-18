import pandas as pd
import requests
import pprint
import time

andre_api_key = '94f29862bf8140a9808e23ad2494fea9'
'''
endpoints:
    everything
    top-headlines

attributes:
    sources&
    from yyyy-mm-dd&
    sortBy= (e.g. popularity)&

'''
trusted_sources = ['bbc-news', 'the-washington-post', 'reuters', 'the-economist', 'the-guardian-au', 'the-guardian-uk',
                   'cnn', 'the-new-york-times']
variable_list = ['source_id', 'source_name', 'label', 'author','title','description', 'url', 'published_at', 'content']

def extract_news(sources_list):
    df = {variable:[] for variable in variable_list}

    for source in sources_list:
        page = 1
        response = api_request(source, page, andre_api_key)
        while response.status_code == 200:
            if page % 5 == 0:
                time.sleep(5)
            for entry in response.json()['articles']:
                df['source_id'].append(entry['source']['id'])
                df['source_name'].append(entry['source']['name'])
                df['author'].append(entry['author'])
                df['title'].append(entry['title'])
                df['description'].append(entry['description'])
                df['url'].append(entry['url'])
                df['published_at'].append(entry['publishedAt'])
                df['content'].append(entry['content'])
                df['label'].append('Reliable')
            page += 1
            response = api_request(source, page, andre_api_key)

    return pd.DataFrame(df)

def api_request(source, page_number, api_key):
    url = f'https://newsapi.org/v2/everything?sources={source}&sortBy=popularity&page={page_number}&apiKey={api_key}'
    response = requests.get(url)
    print(f'Call to {source} on page {page_number} returns {response}')
    return response

def main():
    df = extract_news(trusted_sources)
    df.to_csv('Resources/Trusted_Google_News2.csv')

if __name__ == '__main__':
    main()
