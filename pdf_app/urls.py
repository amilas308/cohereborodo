from django.urls import path
from .views import upload_pdf
app_name= "pdf_app"
urlpatterns = [
    path("upload/", upload_pdf, name="upload"),
]
