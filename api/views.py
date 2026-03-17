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


def fast_ping(request):
    return JsonResponse({
        "message": "pong",
        "status": "success"
    })


def slow_request(request):
    # Supports /api/slow/?seconds=1.2 to control span duration.
    try:
        delay = float(request.GET.get("seconds", 1.0))
    except ValueError:
        delay = 1.0

    delay = max(0.1, min(delay, 5.0))
    time.sleep(delay)

    return JsonResponse({
        "message": "Slow endpoint completed",
        "delay": round(delay, 2),
        "status": "success"
    })


def random_outcome(request):
    delay = random.uniform(0.1, 0.8)
    time.sleep(delay)

    if random.random() < 0.35:
        return JsonResponse({
            "message": "Random failure for trace testing",
            "delay": round(delay, 2),
            "status": "error"
        }, status=500)

    return JsonResponse({
        "message": "Random success",
        "delay": round(delay, 2),
        "status": "success"
    })


def force_error(request):
    return JsonResponse({
        "message": "Intentional error response for Jaeger",
        "status": "error"
    }, status=500)


def user_profile(request, user_id):
    delay = random.uniform(0.05, 0.25)
    time.sleep(delay)

    return JsonResponse({
        "user_id": user_id,
        "message": f"Fetched profile for user {user_id}",
        "processing_time": round(delay, 2),
        "status": "success"
    })