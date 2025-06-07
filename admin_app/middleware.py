from django.http import HttpResponseForbidden
from decouple import config

# Middleware to block access to the admin panel based on IP addresses
class IPAdminBlockerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = config('ALLOWED_IP_ADMIN')

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
            if ip:
                ip = ip.split(',')[0]  
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            print(f"IP detected: {ip}")    
            if ip not in self.allowed_ips:
                return HttpResponseForbidden("Access denied.")
        return self.get_response(request)