"""
Problem:
    ANY LANGUAGE: Using any language or library of your choice, make an HTTP GET request to the Dogs API.
    You want to get the URL of a dog photo at random.
    For the documentation, see https://dog.ceo/dog-api/.

"""

import requests

URL = "https://dog.ceo/api/breeds/image/random"


def random_pic_url():
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        if data["status"] == "success":
            save_image(data["message"])
            return data["message"]


def save_image(url):
    image_name = url.split("/")[-1]
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_name, "wb") as fh:
            fh.write(response.content)


if __name__ == "__main__":
    print(random_pic_url())
    print(random_pic_url())
    print(random_pic_url())
    print(random_pic_url())
