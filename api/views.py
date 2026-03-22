from django.http import JsonResponse
import time

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

def force_error(request):
    return JsonResponse({
        "message": "Intentional error response for Jaeger",
        "status": "error"
    }, status=500)
