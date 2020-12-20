# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

# Class for menu prices spider
class Product(Item):
    # define the fields for your item here like:
    restaurant = Field()
    category = Field()
    name = Field()
    size = Field()
    price = Field()
    url = Field()


# Class for nutrition spider
class Nutrition(Item):
    # define the fields for your item here like:
    restaurant = Field()
    category = Field()
    name = Field()
    size = Field()
    calories = Field()