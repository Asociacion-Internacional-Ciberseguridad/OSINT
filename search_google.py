import requests
from bs4 import BeautifulSoup
import time

def search_documents(query, file_types=["pdf", "docx", "pptx", "xlsx"], num_results=20):
    base_url = "https://www.google.com/search"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    results = []

    # Crear consulta avanzada
    file_type_query = " OR ".join([f"filetype:{ft}" for ft in file_types])
    full_query = f"{query} ({file_type_query})"
    params = {"q": full_query, "num": num_results}

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a"):
            href = link.get("href")
            if href and "url?q=" in href:
                url = href.split("url?q=")[1].split("&")[0]
                if any(ft in url for ft in file_types):
                    results.append(url)
        # Esperar para evitar bloqueos
        time.sleep(2)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    return results

if __name__ == "__main__":
    query = input("Enter the search term: ")
    file_types = ["pdf", "docx", "pptx", "xlsx"]
    documents = search_documents(query, file_types)
    if documents:
        print(f"\nDocuments found ({len(documents)}):")
        for idx, doc in enumerate(documents, 1):
            print(f"{idx}. {doc}")
    else:
        print("No documents found.")
