import aio_pika
import json
from core.rabbit import connect_to_rabbit

QUEUE_NAME = "reviews"
EXCHANGE_NAME = "review_events" #prioritary

async def publish_review_event(event: dict):
    channel = await connect_to_rabbit()

    exchange = await channel.declare_exchange(EXCHANGE_NAME, aio_pika.ExchangeType.TOPIC, durable=True) # Everyone can react to TOPIC

    routing_key = event.get("event_type", "reviews.unknown")

    message = aio_pika.Message(body=json.dumps(event).encode())
    
    await exchange.publish(message, routing_key=routing_key)