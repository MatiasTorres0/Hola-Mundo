from django.shortcuts import render

# Create your views here.
def holamundo(request):
    return render(request, 'core/holamundo.html')