import pika
import json
from app.scraper import scrape_data
from app.redis_handler import store_task_result, update_task_status
from app.config import RABBITMQ_URL


def callback(ch, method, properties, body):
    data = json.loads(body)
    task_id = data['task_id']
    cnpj = data['cnpj']

    update_task_status(task_id, "in_progress")

    try:
        result = scrape_data(cnpj)
        store_task_result(task_id, result)
        update_task_status(task_id, "completed")
    except Exception as e:
        update_task_status(task_id, "failed")


connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
channel = connection.channel()
channel.queue_declare(queue='scraping_tasks')
channel.basic_consume(queue='scraping_tasks', on_message_callback=callback, auto_ack=True)
print("Worker is waiting for tasks...")
channel.start_consuming()
