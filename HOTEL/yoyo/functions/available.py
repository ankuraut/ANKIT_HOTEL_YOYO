import datetime  #this need to check function below
from yoyo.models import Room, Booking

def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    for booking in booking_list:
        if booking.check_in > check_out or booking.check_out < check_in: #Here it checks wheater the guest is still there or left
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)  # ALL is a type of function , the opposite of this is ANY            