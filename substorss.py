#!/usr/bin/python
import webbrowser
import listtorss
import os

webbrowser.open('https://www.youtube.com/feed/channels', new=2)

info = open("instructions.txt","r")
print(info.read())

os.system("gnome-terminal -- sensible-editor channels.txt")

input("Press ENTER when you're done.")

os.mkdir("out")
listtorss.convert("channels.txt","out/subscriptions.opml")