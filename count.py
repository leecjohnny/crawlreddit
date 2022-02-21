import requests
import csv

keywords = [
    'cloudflare',
    'fastly',
    'edge computing',
    'zscaler',
    'cloudflare workers',
    'cloudfront',
    'akamai'
]
subreddits = [
    'computerscience',
    'netsec',
    'networking',
    'sysadmin',
    'programming',
    'cybersecurity'
]

result_types = [
    'submission',
    'comment']

# https://www.reddit.com/r/computerscience/
# https://www.reddit.com/r/netsec/
# https://www.reddit.com/r/networking/
# https://www.reddit.com/r/sysadmin/
# https://www.reddit.com/r/programming/
# https://www.reddit.com/r/cybersecurity/


headers = ['subreddit', 'type', 'created_time', 'term']
out_rows = [headers]


def fetch_results(result_type, subreddit, term):
    payload = {
        'q': term,
        'after': '1577836800',
        'subreddit': subreddit,
        'size': '500'
    }
    url = url = 'https://api.pushshift.io/reddit/search/' + result_type + '/'
    r = requests.get(url, params=payload)
    if r.status_code == 200:
        results = r.json()['data']
        for result in results:
            row = [subreddit, result_type, str(
                result.get('created_utc')), term]
            out_rows.append(row)


for keyword in keywords:
    for subreddit in subreddits:
        for result_type in result_types:
            fetch_results(result_type, subreddit, keyword)


fetch_results('comment', 'networking', 'cloudflare')

file = open('data/reddit_results.csv', 'w+', newline='')

with file:
    write = csv.writer(file)
    write.writerows(out_rows)
