#mapping the URLs
from django.urls import path
from my_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload, name='upload'),  # This is now pointing to the upload view
    path('upload_ppt/', views.upload, name='upload_ppt'),
    path('upload_word/', views.upload, name='upload_word'),
]