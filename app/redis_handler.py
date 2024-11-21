import redis
import json
from app.config import REDIS_URL

redis_client = redis.Redis.from_url(REDIS_URL)

def update_task_status(task_id, status):
    redis_client.set(f"{task_id}_status", status)

def store_task_result(task_id, result):
    redis_client.set(f"{task_id}_result", json.dumps(result))

def get_task_status(task_id):
    return redis_client.get(f"{task_id}_status").decode()

def get_task_result(task_id):
    return json.loads(redis_client.get(f"{task_id}_result"))
