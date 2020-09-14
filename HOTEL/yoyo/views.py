from django.shortcuts import render , HttpResponse
from django.views.generic import ListView, FormView, View #pre-defined
from .models import Room, Booking
from .forms import AvailableForm
from yoyo.functions.available import check_availability

# Create your views here.
class RoomListView(request):
    room = Room.objects.all()[0]
    room_typess = dict(room.ROOM_TYPES)
    #print('typess=', room_typess)

    room_values = room_typess.values()
    #print('typess=', room_values)
    room_list = []

    for room_type in room_typess:
        room = room_typess.get(room_type)
        room_url = reverse('yoyo:RoomDetailView', kwargs={'types': room_type})
        room_list.append((room, room_url))
    context = {
        "room_list": room_list,
    }
    return render(request, 'room_list_view.html', context)
    

class BookingList(ListView):
    model = Booking
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = Booking.objects.all()
            return booking_list
        else:
            booking_list = Booking.objects.filter(user=self.request.user)
            return booking_list    

class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        types = self.kwargs.get('types',None)
        form = AvailableForm()
        room_list = Room.objects.filter(types=types)
        
        if len(room_list) > 0:
            room = room_list[0]
            room_type = dict(room.ROOM_TYPES).get(room.type, None)
            context = {
                'room_type': room_type,
                'form' : form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse(' SORRY FOR THIS CATEGORY')    


    def post(self, request, *args, **kwargs):
        types = self.kwargs.get('types',None)
        room_list = Room.objects.filter(types=types)
        form = AvailableForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out']
            )        
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse(' SORRY FOR THIS')        


#This one is only for admin porpose
class BookingView(FormView):
    form_class = AvailableForm
    template_name = 'available_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(types = data['room_type'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        
        if len(available_rooms)>0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out']
            )        
            booking.save()
            return HttpResponse(booking)
        else:
            return HttpResponse(' SORRY FOR THIS')    
