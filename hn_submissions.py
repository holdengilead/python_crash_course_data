from operator import itemgetter
from time import sleep

import requests

# Make an API call and check the response.
URL = "https://hacker-news.firebaseio.com/v0/beststories.json"
r = requests.get(URL, timeout=10)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url, timeout=10)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dicts.append(
        {
            "title": response_dict["title"],
            "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
            "comments": response_dict["descendants"],
        }
    )
    sleep(0.5)

submission_dicts.sort(key=itemgetter("comments"), reverse=True)

for submission_dict in submission_dicts:
    print(f'\nTitle: {submission_dict["title"]}')
    print(f'Discussion link: {submission_dict["hn_link"]}')
    print(f'Comments: {submission_dict["comments"]}')
