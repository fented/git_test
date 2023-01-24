import requests

def get_animal_image(animal: str) -> str:
    """Retrieves an image URL of a cat or a dog"""
    try:
        api_key = "" if animal == "cat" else ""
        url = f'https://api.the{animal}api.com/v1/images/search?size=full&api_key={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[0]["url"]
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def main():
    while True:
        choice = input("Enter 'cat' for cat image or 'dog' for dog image: ")
        image_url = get_animal_image(choice)
        if image_url:
            print(image_url)
        else:
            print("Invalid choice. Please enter 'cat' or 'dog'.")
        again = input("Do you want to retrieve another image? (y/n): ")
        if again.lower() == "n":
            break

main()
