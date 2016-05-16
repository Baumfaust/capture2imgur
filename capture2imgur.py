#!/usr/bin/env python
# Captures a screenshot, uploads it to imgur, copies the URL to clipboard and dumps it into a history.csv file.

from subprocess import call, check_output
from imgurpython import ImgurClient
from os.path import expanduser
from time import strftime
import pyperclip
import csv
import os

home = expanduser("~")
_path = os.path.join(home, "imgur")


def take_screen():
    path = os.path.join(_path, "imgur.png")
    win_id = int(check_output(['xdotool', 'getactivewindow']))
    screen = check_output(["maim", path, "-i " + str(win_id)])
    notify("active window captured")
    return path


def upload(path):
    client = ImgurClient("1cc97dbda52da82", "")
    image = client.upload_from_path(path, config=None, anon=True)

    if not image["link"]:
        notify("error uploading")
    else:
        notify("uploaded")
    return image["link"]


def save_data(date, link):
    path = os.path.join(_path, "history")
    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, "uploads.csv"), 'a', newline='') as uploads:
        writer = csv.writer(uploads, delimiter=';')
        writer.writerow([date, link])


def copy_text(text):
    pyperclip.copy(text)
    pyperclip.paste()


def notify(message):
    call(["/usr/bin/notify-send", message])


if __name__ == '__main__':
    if not os.path.exists(_path):
        os.mkdir(_path)
    now = strftime("%d.%m.%Y %H:%M:%S")
    path = take_screen()
    if path:
        link = upload(path)
        if link:
            copy_text(link)
            save_data(now, link)
