from datetime import*
from urllib.request import urlopen, urlretrieve
import urllib.request
from xml.dom import minidom
import os
import struct
import ctypes
    
def download(url_1):
    url=str(url_1)
    today=str(date.today())
    print(url)
    pic_name="bing_wall_" + str(today) + ".jpg"
    urllib.request.urlretrieve(url,pic_name)
    return pic_name
    
def wall_download():
    idx=0
    use=True
    try:
        page=urlopen('http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=ru-RU')
    except Exception as e:
        print('Error while downloading #', idx, e)
        return
    try:
        xmldoc = minidom.parse(page)
    # This is raised when there is trouble finding the image url.
    except Exception as e:
        print('Error while processing XML index #', idx, e)
        return
    for item in xmldoc.getElementsByTagName("url"):
        url="http://www.bing.com" + item.firstChild.nodeValue
    
    return(url)

url_1=wall_download()
url=str(url_1)
url= url[:-12] + "1920x1200" + ".jpg"
pic_name=download(url)

pic_name=str(pic_name)


SPI_SETDESKWALLPAPER = 20

bingpath = os.path.abspath('.')
final_path = os.path.join(bingpath,pic_name)
WALLPAPER_PATH = final_path


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


change_wallpaper()
