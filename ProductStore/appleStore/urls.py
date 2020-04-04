from django.conf.urls.static import static
from django.urls import path

from ProductStore import settings
from appleStore import views

urlpatterns = [
    path('', views.showIndex, name ='main'),
    path('save_product/', views.saveProduct, name = 'save_product')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)