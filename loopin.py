import random
import sys
import os
class Cars:
    __name = ""
    __color = ""
    __brand = ""
    __model = ""
    __drive = ""
    __tranytype = ""
    __seattype = ""
    def __init__(self, name, color, brand, model, drive, tranytype, seattype):
        self.__name = name
        self.__color = color
        self.__brand = brand
        self.__model = model
        self.__drive = drive
        self.__tranytype = tranytype
        self.__seattype = seattype

    def set_name(self, name):
        self.__name = name

    def set_color(self, color):
        self.__color = color
