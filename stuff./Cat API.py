import requests
import json

api_key = ""
# Get API key from: https://thecatapi.com/

def CatAPI():
  def ajax_get(url):
    response = requests.get(url)
    if response.status_code == 200:
      try:
        data = response.json()
      except ValueError as err:
        print(err.message + " in " + response.text)
        return
      return data
  data = ajax_get('https://api.thecatapi.com/v1/images/search?size=full')
  if data:
    print(data[0]["url"])
    print(data)

CatAPI()