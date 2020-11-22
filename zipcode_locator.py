from tkinter import *
from PIL import ImageTk,Image
import requests
import json
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup

root = Tk()
root.title('Find Zipcode')
root.geometry("400x400")

def zipLookup():
    api_request = requests.get("http://api.zippopotam.us/us/" + zip.get())
    api = json.loads(api_request.content)
    try:
        for places in api['places']:
            city = (places['place name'])
            state = (places['state'])
            zipcode = city + ", " + state
    except Exception as e:
        zipcode = "Not a valid zip code..."

    myLabel = Label(root, text=zipcode)
    myLabel.grid(row=1)


zip = Entry(root)
zip.grid(row=0, column=0, stick=W+E+N+S)

zipButton = Button(root, text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0, column=1, stick=W+E+N+S)



root.mainloop()




