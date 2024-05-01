from django.shortcuts import render
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name': 'Lets learn python'},
#     {'id':2, 'name': 'Design with me'},
#     {'id':3, 'name': 'Frontend Developers'},
# ]
 
def home(request):
    rooms = Room.objects.all()
    
    return render(request, 'playground/home.html', {'rooms': rooms}) 

def room(request, pk):
    room = Room.objects.get(id=pk)
        
    context = {'room': room}
    
    return render(request, 'playground/room.html', context) 

