import logging
import pika
from pika import DeliveryMode
from pika.exchange_type import ExchangeType

logging.basicConfig(level=logging.DEBUG)

credentials = pika.PlainCredentials("guest", "guest")
parameters = pika.ConnectionParameters("localhost", credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.exchange_declare(
    exchange="test_exchange",
    exchange_type=ExchangeType.direct,
    passive=False,
    durable=True,
    auto_delete=False,
)

print("Sending message to create a queue")
channel.basic_publish(
    "test_exchange",
    "standard_key",
    "queue:group",
    pika.BasicProperties(
        content_type="text/plain", delivery_mode=DeliveryMode.Transient
    ),
)

connection.sleep(5)

print("Sending text message to group")
channel.basic_publish(
    exchange="test_exchange",
    routing_key="group_key",
    body="Message to group_key",
    properties=pika.BasicProperties(
        content_type="text/plain", delivery_mode=DeliveryMode.Transient
    ),
)

connection.sleep(5)

print("Sending text message")
channel.basic_publish(
    exchange="test_exchange",
    routing_key="standard_key",
    body="Message to standard_key",
    properties=pika.BasicProperties(
        content_type="text/plain", delivery_mode=DeliveryMode.Transient
    ),
)

connection.close()
