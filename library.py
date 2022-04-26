import requests
import ctypes


def download_image_from_url(image_url, save_path):

    """
    Downloads an image from a url and saves it to a specified path

    :param image_url: the url of the image to be downloaded
    :param save_path: the path to where you want to save the image

    """
    print("Downloading image from URL...", end='')

    response = requests.get(image_url)

    if response.status_code == 200:  
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("Success")

    else:
        print('failed. Response code:', response.status_code)
        

def set_desktop_background(image_path):
    """
    sets the specified image as the desktop background

    :param image_path: The path where the image is saved
    
    """
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

