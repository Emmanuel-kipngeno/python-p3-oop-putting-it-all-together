#!/usr/bin/env python3


class Shoe:
   def __init__(self, brand, size, color):
       self.brand = brand
       self.size = size
       self.color = color

   def get_info(self):
       return f"Brand: {self.brand}, Size: {self.size}, Color: {self.color}"
