from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from store.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', cart_page),
    path('search_results/', search_result, name='search_results'),
    path('book_detail/<int:pk>/', book_detail.as_view(), name='book_detail'),
    path('', home_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
