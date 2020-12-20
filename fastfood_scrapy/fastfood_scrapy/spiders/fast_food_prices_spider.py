
import scrapy
from scrapy.spiders import SitemapSpider

# import items.py Product class
from fastfood_scrapy.items import Product

# Need to change this to sitemap spider
class FoodSpider(SitemapSpider):
	name = 'fastfood_spider'

	sitemap_urls = ['https://www.fastfoodmenuprices.com/page-sitemap.xml']



# Based on commetns on regex, passing the name in the slashes should work? VERIFY
# Might have to put forwarslashes around prices here....

	sitemap_rules = [
		('prices', 'parse_product')
	]


	def parse_product(self, response):

		# Using the '//' in the xpath will jump to the next available versus hardcoding path with '/'
		table_rows = response.xpath("//table//tr")

		

		for row in table_rows:

			item = Product()

			item['url'] = response.url
			
			item['restaurant'] = response.xpath("string(//main/article/header/h1)").get()

			item['category'] = row.xpath("string(.//h2)").get()

			item['name'] = row.xpath("string(td)").get() # NEED TO ACCOUTN FOR SIZES BC PRICE IS BASED ON THAT FOR SOME MENUS

			item['size'] = row.xpath("string(td[@class='column-2'])").get()

			item['price'] = row.xpath("td//@value").get()
			
			yield item




# Can alter the above to use the @class = column-[1,2,3] if these show issues.

# NEED TO SET UP ROTATING LIST OF PROXIES AND USERS TO GET THIS WORKING BEST POSSIBLE