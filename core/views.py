from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')

def calendar(request):
    return render(request, 'calendar.html')

def facilities(request):
    return render(request, 'facilities.html')

def outreach(request):
    return render(request, 'outreach.html')

def curriculum(request):
    return render(request, 'curriculum.html')

def infrastructure(request):
    return render(request, 'infrastructure.html')

def tools(request):
    return render(request, 'tools.html')
