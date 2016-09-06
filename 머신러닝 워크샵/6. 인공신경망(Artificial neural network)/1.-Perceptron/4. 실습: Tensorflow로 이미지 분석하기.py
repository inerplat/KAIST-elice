import classify_image
import subprocess
import urllib.request
import elice_utils

def main():
    __download_file = "./download.jpg"

    image_url = "http://i.imgur.com/A8eQsll.jpg"

    download_image(image_url, __download_file)
    elice_utils.send_image(__download_file)
    classify_image.main(__download_file)

def download_image(image_url, download_filepath):
    urllib.request.urlretrieve(image_url, download_filepath)

if __name__ == "__main__":
    main()
