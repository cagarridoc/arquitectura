from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'index.html')

def formulario(request):
    return render(request,'blog.html')
