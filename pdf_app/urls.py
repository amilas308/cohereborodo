from django.urls import path
from .views import upload_pdf
from . import views
app_name= "pdf_app"
urlpatterns = [
    path("", views.upload_view, name="upload"),
    path("upload/", upload_pdf, name="upload"),
]
