from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from shop.views import MahsulotView

app_name = 'shop'
urlpatterns = [
    path('mahsulot/<int:pk>/', MahsulotView.as_view(), name='batafsil'),
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category, name='category')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)