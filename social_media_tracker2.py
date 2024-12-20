# social_media_tracker.py
import requests

def check_social_media(username):
    platforms = {
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://instagram.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Youtube": f"https://www.youtube.com/@{username}"
    }
    results = {}
    for platform, url in platforms.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[platform] = url
            else:
                results[platform] = "Not Found"
        except requests.RequestException:
            results[platform] = "Error occurred"
    return results

if __name__ == "__main__":
    username = input("Enter username: ")
    results = check_social_media(username)
    for platform, status in results.items():
        print(f"{platform}: {status}")
