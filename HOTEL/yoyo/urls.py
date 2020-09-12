from django.urls import path
from .views import RoomList, BookingList, BookingView

app_name = 'yoyo'

urlpatterns = [
    path('room/', RoomList.as_view(), name='RoomList'), # as_view is used here to call class based view
    path('booking/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='booking_view')
]
