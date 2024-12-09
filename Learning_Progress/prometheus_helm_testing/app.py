from prometheus_client import start_http_server, Counter
import time
import random

# Create a Prometheus counter
REQUESTS = Counter('http_requests_total', 'Total HTTP requests')

# Start a Prometheus metrics server
start_http_server(8000)

def process_request():
    """Simulate request processing and increase the counter"""
    REQUESTS.inc(random.randint(1, 5))  # Increment random counts for testing

if __name__ == '__main__':
    while True:
        process_request()
        time.sleep(1)
