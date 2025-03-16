import requests
import cv2
import numpy as np

def get_pixels():
    get_tile = requests.get('https://olimp.miet.ru/ppo_it/api')
    # get_coords = requests.get('https://olimp.miet.ru/ppo_it/api/coords')
    data = get_tile.json()['message']['data']
    return data

def get_img():
    d = np.array([np.array(i, dtype=np.uint8) for i in get_pixels()], dtype=np.uint8)
    cv2.imwrite('img.jpg', d)