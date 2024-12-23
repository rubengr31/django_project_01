from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("home")

def bye(request):
    return HttpResponse("bye")