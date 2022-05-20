from tkinter import *
import tkintermapview
import sys

class Map():
    master, label, cmap = None, None, None
    def __init__(self, master):
        self.master = master
        self.label = LabelFrame(master)
        self.label.pack(pady = 20)
        self.cmap = tkintermapview.TkinterMapView(
            self.label,
            width = 2000,
            height = 1000,
            
        )
        
        self.cmap.pack(side = "top", fill = "both", expand = True)
        
        
        
    def setPos(self, lat, long):
        self.cmap.set_position(lat, long)
        
    def setZoom(quant):
        self.cmap.set_zoom(quant)
           
    def viewAddress(addy):
        self.cmap.set_address(addy)



        
        
            