from django.urls import path
from .views import RoomListView, BookingList, BookingView, RoomDetailView

app_name = 'yoyo'

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='RoomList'), # as_view is used here to call class based view
    path('booking/', BookingList.as_view(), name='BookingList'),
    path('book/', BookingView.as_view(), name='Bookingview'),
    path('room/<category>', RoomDetailView.as_view(), name='RoomDetailView'),
]
