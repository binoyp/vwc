from os import path
from PIL import Image
from PIL.ImageColor import getrgb
import numpy as np
import cv2
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS
import argparse


MAX_WORDS = 2000

def make_img_transparent(imagepath):
    """Replace white bg with transparency

    """
    img = Image.open(imagepath)
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(imagepath, "PNG")


def gen_save(mask_path, text, pic_save_path, bgcolor = getrgb("hsl(25,0%,75%)")):
    """

    """
    assert os.path.exists(mask_path)
    pic_mask = np.array(Image.open(mask_path))
    # edges = cv2.Canny(np.array(pic_mask),100,200)
    STOPWORDS.add("said")
    wc = WordCloud(background_color=bgcolor , max_words=MAX_WORDS, mask=pic_mask, stopwords=STOPWORDS)
    # generate word cloud
    wc.generate(text)

    # store to file
    if pic_save_path:
        wc.to_file(path.join(d, pic_save_path))
    
    wc_arr = wc.to_array()
    return wc_arr


def showmask(inparr):
    
    plt.imshow(wc)
    plt.axis("off")
    plt.figure()
    # plt.imshow(edim, cmap = plt.cm.gist_earth)
    plt.axis("off")
    plt.show()

def GenWordCloud():
    pass


if __name__ == "__main__":

    pass