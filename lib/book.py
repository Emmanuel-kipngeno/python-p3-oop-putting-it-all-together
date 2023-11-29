#!/usr/bin/env python3

class Book:
   def __init__(self, title, author, price):
       self.title = title
       self.author = author
       self.price = price

   def get_info(self):
       return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"


class Book:
    def __init__(self, title, page_count, price):
        self.title = title
        self.page_count = page_count
        self.price = price

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

