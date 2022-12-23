from django.shortcuts import render

def Inicio(request):
    template_name = 'index.html'
    ctx = {}
    return render(request, template_name, ctx)
    
def registro(request):
    template_name = 'registro.html'
    ctx = {}
    return render(request, template_name, ctx)    

def blog(request):
    template_name = 'blog.html'
    ctx = {}
    return render(request, template_name, ctx)

    