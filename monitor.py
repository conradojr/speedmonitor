import requests

def get_speed():
    """Gets the speed of the internet connection."""
    speedtest_url = "https://www.speedtest.net/"
    response = requests.get(speedtest_url)
    if response.status_code == 200:
        data = response.json()
        download_speed = data["download"]
        upload_speed = data["upload"]
        return download_speed, upload_speed
    else:
        raise Exception("Error getting speed")

if __name__ == "__main__":
    download_speed, upload_speed = get_speed()
    print("Download speed:", download_speed)
    print("Upload speed:", upload_speed)
