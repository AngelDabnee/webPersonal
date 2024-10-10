from django.shortcuts import render
from django.shortcuts import HttpResponse

html_base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href = "/portafolio/">Portafolio</a></li>
    <li><a href = "/contact/">Contacto</a></li>
</ul>


"""



# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about (request):
    return render(request, "core/about.html") 

def portafolio (request):
    return render(request, "core/portafolio.html")

def contact(request):
    return render(request, "core/contact.html")