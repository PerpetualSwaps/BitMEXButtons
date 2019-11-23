import os
import sys
import ccxt
import tkinter as tk
import configparser
import ttkthemes

from api import exchange
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

my_config_parser = configparser.ConfigParser()
my_config_parser.read('config.ini')
exchange = ccxt.bitmex({
    'apiKey': my_config_parser.get('BITMEX','apikey'),
    'secret': my_config_parser.get('BITMEX','apisecret'),
    'enableRateLimit': True,
})

HEIGHT = 150
WIDTH = 275
symbol = 'BTC/USD'
type = 'Market'
type_limit = 'Limit'
side_buy = 'buy'
side_sell = 'sell'
price = None
root = ThemedTk(theme="black")

root.title('Execut0r')
root.attributes('-alpha', 0.9)
root.iconbitmap(r'D:\Python Projects\BitMEX_Buttons\mexicon.ico')
root.resizable(False, False)
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
frame = ttk.Frame(root)
frame.place(relwidth=1, relheight=1)
label = ttk.Label(frame, text="Order Quantity")
label.pack()
position_size = ttk.Entry(frame)
position_size.pack()
label2 = ttk.Label(frame, text="Limit Order Price")
label2.pack()
limit_price = ttk.Entry(frame)
limit_price.pack()

canvas.pack()

def place_buy():
    exchange.create_order(symbol, type, side_buy, position_size.get(), price)

def place_sell():
    exchange.create_order(symbol, type, side_sell, position_size.get(), price)

def place_limit_buy():
    exchange.create_order(symbol, type_limit, side_buy, position_size.get(), limit_price.get())

def place_limit_sell():
    exchange.create_order(symbol, type_limit, side_sell, position_size.get(), limit_price.get())

buybutton = ttk.Button(frame, command=place_buy, text="Market Buy")
buybutton.pack(side='left')
sellbutton = ttk.Button(frame, command=place_sell, text="Market Sell")
sellbutton.pack(side='left')
limitsellbutton = ttk.Button(frame, command=place_limit_sell, text="Limit Sell")
limitsellbutton.pack(side='right')
limitbuybutton = ttk.Button(frame, command=place_limit_buy, text="Limit Buy")
limitbuybutton.pack(side='right')

image = Image.open(r'D:\Python Projects\BitMEX_Buttons\Arthur.png')
photo = ImageTk.PhotoImage(image)
arthurlabel = ttk.Label(root, image=photo)
arthurlabel.place(x=215, y=20)

root.mainloop()
