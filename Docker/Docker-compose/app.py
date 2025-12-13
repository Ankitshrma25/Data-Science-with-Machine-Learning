import redis
import time

# Connect to Redis (service name = redis from docker-compose)
r = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

# Wait until Redis is ready
while True:
    try:
        r.ping()
        break
    except redis.exceptions.ConnectionError:
        print("Waiting for Redis...")
        time.sleep(1)

# Set and get a value
r.set("message", "Kis color ki chaddi pehni hai tumhe")
value = r.get("message")

print(value)
