# social_media_tracker.py
import requests

def check_social_media(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "LinkedIn": f"https://linkedin.com/in/{username}",
        "Youtube": f"https://www.youtube.com/@{username}"
    }
    results = {}
    for platform, url in platforms.items():
        response = requests.get(url)
        results[platform] = response.status_code == 200
    return results

if __name__ == "__main__":
    username = input("Enter username: ")
    results = check_social_media(username)
    print(results)
