import plotly.express as px
import requests

# Make an API call and check the response.
URL = "https://api.github.com/search/repositories"
URL += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(URL, headers=headers, timeout=10)
print(f"Status code: {r.status_code}")

# Process overall results.
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Process repository information.
repo_dicts = response_dict["items"]
repo_links, starts, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_links.append(f"<a href='{repo_url}'>{repo_name}</a>")
    starts.append(repo_dict["stargazers_count"])

    # Build hover texts.
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_texts.append(f"{owner}<br />{description}")

# Make visualization.
TITLE = "Most-Starred Python Projects on GitHub"
labels = {"x": "Repository", "y": "Stars"}
fig = px.bar(x=repo_links, y=starts, title=TITLE, labels=labels, hover_name=hover_texts)
fig.update_layout(
    title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20
)
fig.update_traces(marker_color="SteelBlue", marker_opacity=0.6)

fig.show()
