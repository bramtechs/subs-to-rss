#!/usr/bin/python
import webbrowser
import listtorss
import os

if os.name == 'nt': # Windows NT
    webbrowser.open('https://www.youtube.com/feed/channels', new=2)
    info = open("instructions.txt","r")
    print(info.read())
    info.close()
    os.system("notepad.exe channels.txt")
else:
    term = input("Whats the command for your terminal? (gnome-terminal if empty) ")
    if term == "":
        term = "gnome-terminal"

    info = open("instructions.txt","r")
    print(info.read())
    info.close()
    webbrowser.open('https://www.youtube.com/feed/channels', new=2)

    if term == "gnome-terminal":
        os.system(term + " -- sensible-editor channels.txt")
    else:
        os.system(term + " -x sensible-editor channels.txt")


input("Press ENTER after you edited AND SAVED the file.")

listtorss.convert("channels.txt","subscriptions.opml")
