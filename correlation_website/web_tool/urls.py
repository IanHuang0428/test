from django.urls import path
from web_tool import views

urlpatterns = [
    path('stock/', views.show),
    path('screen_input/',views.screen_input),
]