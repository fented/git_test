import requests


api_key = "live_w3DI7xX6ISzqM4DrhwTDqAIwSwWQqknTeSL7Jw3zFAFF34ghQl20PdCQPbwCXWTg"
# Get API key from: https://thecatapi.com/

import requests
import json
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
    print(data[0]["id"])
    print(data[0]["url"])
    html = f'<img src="{data[0]["url"]}">'
    print(html)

CatAPI()