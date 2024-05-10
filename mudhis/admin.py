# middleware.py

from django.http import HttpResponseForbidden

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Burada token kontrolü yapılacak





        if not request.user.is_authenticated or not request.user.token:
            # Kullanıcı giriş yapmamış veya tokenı yoksa erişimi reddet
            forbidden_response = HttpResponseForbidden("Erişim reddedildi.")
            return forbidden_response

        return self.get_response(request)
