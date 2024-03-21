#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Custom User Agent'}  # Reddit requires a custom User-Agent header

    response = requests.get(url, headers=headers)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0  # Return 0 for invalid subreddit or any other error

# Test the function
if __name__ == "__main__":
    subreddit = "programming"
    print(number_of_subscribers(subreddit))  # Example: Output should be the number of subscribers for the "programming" subreddit

