#!/usr/bin/python
from genericpath import exists
import sys
import requests
import os

def get_channel_name(url: str) -> str:
    xml = requests.get(url).text
    start = xml.find("<author>")+len("<author>\n..<name>") # crap
    stop = xml.find("</name>")
    name = xml[start:stop].replace('\'',"") # remove dangerous apostrophes
    if "Error 404 (Not Found)" in name:
        return None
    if "Loading..." in name:
        return None
    return name

def convert(path: str, out: str):
    print("Generating OPML from " + path)
    
    if not exists(path):
        print(path + " is not a valid file!")
        return
    
    content = open(path,"r").read()

    template = open("template.html","r").read()

    outlines = ""
    for line in content.split('\n'):
        if (line == ""):
            continue
        name = get_channel_name(line)
        if name == None:
            continue
        print(name)
        outlines += "<outline title='%s' text='%s' type='rss' xmlUrl='%s'/>\n"%(name,name,line)
    
    output = template.replace("<!--HERE-->",outlines)

    # export
    file = open(out,"w")
    file.write(output)

    print ("Saved to " + out)

if "__main__" == __name__:
    if len(sys.argv) > 2:
        convert(sys.argv[1],sys.argv[2])
    else:
        print("No input and output path given...")
