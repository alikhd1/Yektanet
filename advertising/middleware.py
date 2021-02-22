class EventTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        if view_func.__name__ == 'IndexView' or view_func.__name__ == 'AdView':
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                view_kwargs['ip'] = x_forwarded_for.split(',')[0]
            else:
                view_kwargs['ip'] = request.META.get('REMOTE_ADDR')