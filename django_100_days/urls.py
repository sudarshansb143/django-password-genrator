
from django.contrib import admin
from django.urls import path

# custom imports
from authentication import views


urlpatterns = [
    path("home/", views.home, name="home"),
    path("generated_password/", views.generate_password, name="generated_password"),
    path("about/", views.about, name="about"),
    path('admin/', admin.site.urls),
]
