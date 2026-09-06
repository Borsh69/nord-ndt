from django.shortcuts import render
from .models import Service
# Create your views here.
def index(request):
    all_objects = Service.objects.all()
    context = {"objects": all_objects}
    return render(request, 'index.html', context)

def service(request, pk):
    service = Service.objects.get(id=pk)
    print()
    return render(request, 'service.html')