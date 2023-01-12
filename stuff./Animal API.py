import requests

def get_animal_image(animal: str) -> str:
    """Retrieves an image URL of a cat or a dog"""
    try:
        api_key = "live_w3DI7xX6ISzqM4DrhwTDqAIwSwWQqknTeSL7Jw3zFAFF34ghQl20PdCQPbwCXWTg" if animal == "cat" else "live_tHn7SfmqsCL4dKGwsViFeAUDm7cDf4LrHt1zz3CQYieL4t3bleXzaz5I5nYSYzBV"
        url = f'https://api.the{animal}api.com/v1/images/search?size=full&api_key={api_key}'
        response = requests.get(url)
        response.raise_for_status()
        return response.json()[0]["url"]
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def main():
    choice = input("Enter 'cat' for cat image or 'dog' for dog image: ")
    image_url = get_animal_image(choice)
    if image_url:
        print(image_url)
    else:
        print("Invalid choice. Please enter 'cat' or 'dog'.")

main()