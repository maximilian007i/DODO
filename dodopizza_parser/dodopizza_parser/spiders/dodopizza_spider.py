import scrapy
import json
from scrapy.exceptions import CloseSpider

class DodopizzaSpider(scrapy.Spider):
    name = 'dodopizza_spider'
    
    def __init__(self, city_ids=None, *args, **kwargs):
        super(DodopizzaSpider, self).__init__(*args, **kwargs)
        if city_ids is None:
            raise CloseSpider('No city IDs provided.')
        self.city_ids = city_ids.split(',')

    def start_requests(self):
        for city_id in self.city_ids:
            url = f'https://dodopizza.ru/api/v1/products/{city_id}'
            yield scrapy.Request(url=url, callback=self.parse, errback=self.errback)

    def parse(self, response):
        data = json.loads(response.text)
        for product in data.get('products', []):
            yield {
                'id': product.get('id'),
                'name': product.get('name'),
                'description': product.get('description'),
                'category': product.get('category'),
                'size': product.get('size'),
                'price': product.get('price'),
                'images': product.get('images'),
            }

    def errback(self, failure):
        self.logger.error(repr(failure))
