import os
import urllib.request
import struct
import ctypes

def download_url(url):
    name = "image" + ".jpg"
    urllib.request.urlretrieve(url, name)
    print("image downloaded")
    
download_url('https://www.bing.com/az/hprichbg/rb/TulipsEquinox_EN-US11642351862_1366x768.jpg')


SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'C:\\Users\\Praveen\\Documents\\New folder\\image.jpg'


def is_64_windows():
    
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)

    
    if not r:
        print(ctypes.WinError())
    time.sleep(1)
    os.remove("C:\\Users\\Praveen\\Documents\\New folder\\image.jpg")

change_wallpaper()
