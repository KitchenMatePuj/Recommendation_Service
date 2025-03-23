import pika
import json
from src.main.python.ApplicationProperties import ApplicationProperties
from src.main.python.services.rabbit_service import process_recipe_event

def start_rabbit_listener():
    credentials = pika.PlainCredentials(
        username=ApplicationProperties.RABBIT_USER,
        password=ApplicationProperties.RABBIT_PASSWORD
    )

    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=ApplicationProperties.RABBIT_HOST,
        port=ApplicationProperties.RABBIT_PORT,
        credentials=credentials
    ))

    channel = connection.channel()
    channel.queue_declare(queue=ApplicationProperties.RABBIT_QUEUE, durable=True)

    def callback(ch, method, properties, body):
        try:
            message = json.loads(body)
            process_recipe_event(message)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        except Exception as e:
            print(f"[ERROR] Failed to process message: {e}")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=ApplicationProperties.RABBIT_QUEUE, on_message_callback=callback)
    print("[*] Rabbit listener started. Waiting for messages...")
    channel.start_consuming()
