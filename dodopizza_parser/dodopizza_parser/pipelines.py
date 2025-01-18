import pika

class RabbitMQPipeline:
    def open_spider(self, spider):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='products')

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.channel.basic_publish(exchange='', routing_key='products', body=str(item))
        return item
