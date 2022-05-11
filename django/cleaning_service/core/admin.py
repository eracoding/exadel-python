from django.contrib import admin
from core.models import User, Service, Request, RequestStatus, Roles, Review
admin.site.register(User)
admin.site.register(Service)
admin.site.register(Request)
admin.site.register(RequestStatus)
admin.site.register(Roles)
admin.site.register(Review)
