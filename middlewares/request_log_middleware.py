import time
import logging


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        logger.info(
            f"Method: {request.method}, Path: {request.path}, "
            f"Status: {response.status_code}, Duration: {duration:.2f}s"
        )
        return response
