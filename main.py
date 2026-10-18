
import os
from exa_py import Exa

exa = Exa(os.environ["EXA_API_KEY"])

social_domains = [
    "tiktok.com",
    "reddit.com",
    "x.com",
    "twitter.com",
    "youtube.com",
    "instagram.com",
    "facebook.com",
    "linkedin.com",
]

print("=== Exa Search Engine ===")
print("1. All websites")
print("2. Social media")

choice = input("Choose search mode (1 or 2): ").strip()
query = input("Search here: ").strip()

if not query:
    print("Please enter a search query.")
elif choice not in ("1", "2"):
    print("Invalid choice. Please enter 1 or 2.")
else:
    search_options = {
        "num_results": 10,
        "type": "keyword",
    }

    if choice == "2":
        search_options["include_domains"] = social_domains

    response = exa.search(query, **search_options)

    if not response.results:
        print("No results found.")
    else:
        for i, result in enumerate(response.results, start=1):
            print(f"\n--- Result {i} ---")
            print(f"Title: {result.title}")
            print(f"URL: {result.url}")
