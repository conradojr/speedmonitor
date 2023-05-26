import requests
from speedtest import Speedtest

def get_speed():
    """Gets the speed of the internet connection."""
    speedtest = Speedtest()
    download_speed = speedtest.download()
    upload_speed = speedtest.upload()
    return download_speed, upload_speed

if __name__ == "__main__":
    download_speed, upload_speed = get_speed()
    print("Download speed: {:.2f} Mbps".format(download_speed))
    print("Upload speed: {:.2f} Mbps".format(upload_speed))
