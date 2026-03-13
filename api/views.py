from django.http import JsonResponse
import time
import random

def hello_world(request):
    # Simulate a database query that takes a random amount of time
    delay = random.uniform(0.1, 0.5)
    time.sleep(delay)
    
    return JsonResponse({
        "message": "Hello from the Nest POC!",
        "processing_time": round(delay, 2),
        "status": "success"
    })