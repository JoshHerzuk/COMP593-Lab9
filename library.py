import requests


def download_image_from_url(image_url, save_path)

    print("Downloading image from URL...", end='')

    response = requests.get(image_url)

    if response.status_code == 200:
        print("Success")
        img_data = response.content as handler

        with open(save_path, 'wb')


    else:
        print('failed. Response code:', response.status_code)
        