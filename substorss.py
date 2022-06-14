#!/usr/bin/python
import webbrowser
import listtorss
import os

webbrowser.open('https://www.youtube.com/feed/channels', new=2)

info = open("instructions.txt","r")
print(info.read())

if os.name == 'nt': # Windows NT
    os.system("notepad.exe channels.txt")
else:
    os.system("gnome-terminal -- sensible-editor channels.txt")

input("Press ENTER when you're done.")

listtorss.convert("channels.txt","subscriptions.opml")