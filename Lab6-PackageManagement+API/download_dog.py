import requests

url = 'https://dog.ceo/api/breeds/image/random'

dog_json = requests.get(url).json()

img_url = dog_json['message']

img_response = requests.get(img_url)

# download the image from img_response chunk by chunk - in case the image is too large to download at once
with open('dog.jpg', 'wb') as file:
    for chunk in img_response.iter_content():
        file.write(chunk)

