from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('web_tool/', include('web_tool.urls')),
]
