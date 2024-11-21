import uuid
import pika
from app.config import RABBITMQ_URL

def send_task_to_queue(cnpj: str):
    task_id = str(uuid.uuid4())
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue='scraping_tasks')
    channel.basic_publish(
        exchange='',
        routing_key='scraping_tasks',
        body=json.dumps({"task_id": task_id, "cnpj": cnpj})
    )
    connection.close()
    return task_id
