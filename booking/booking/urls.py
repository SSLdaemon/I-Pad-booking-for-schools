from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
    path('', views.availability, name='availability'),
    path('book/', views.book_ipad, name='book_ipad'),
    path('booking_success/', views.booking_success, name='booking_success'),
]