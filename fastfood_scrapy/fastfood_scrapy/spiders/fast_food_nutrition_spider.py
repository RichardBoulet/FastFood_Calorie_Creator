
import scrapy
from scrapy.spiders import SitemapSpider

# import items.py Product class
from fastfood_scrapy.items import Nutrition

# Need to change this to sitemap spider
class NutritionSpider(SitemapSpider):
	name = 'nutrition_spider'

	sitemap_urls = ['https://www.fastfoodmenuprices.com/page-sitemap.xml']



# Based on commetns on regex, passing the name in the slashes should work? VERIFY
# Might have to put forwarslashes around prices here....

	sitemap_rules = [
		('nutrition', 'parse_product')
	]


	def parse_product(self, response):

		# Using the '//' in the xpath will jump to the next available versus hardcoding path with '/'
		table_rows = response.xpath("//table//tr")



		for row in table_rows:

			item = Nutrition()

			cal_class = response.xpath("//table//thead//th[contains(text(), 'Calories')]/@class").get()

			size_class = response.xpath("//table//thead//th[contains(text(), 'Size')]/@class").get()
			
			item['restaurant'] = response.xpath("string(//main/article/header/h1)").get()

			item['category'] = row.xpath("string(.//h2)").get()

			item['name'] = row.xpath("string(td)").get() # NEED TO ACCOUTN FOR SIZES BC PRICE IS BASED ON THAT FOR SOME MENUS

			item['size'] = row.xpath("string(td[@class = $column])", column = size_class).get()

			item['calories'] = row.xpath("td[@class = $column]//@value", column = cal_class).get()

			yield item




# Can alter the above to use the @class = column-[1,2,3] if these show issues.

# NEED TO SET UP ROTATING LIST OF PROXIES AND USERS TO GET THIS WORKING BEST POSSIBLE