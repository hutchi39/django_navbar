from django.shortcuts import render


def home(request):
    return render(request, 'travel/home.html')

def company(request):
    return render(request, 'travel/company.html')

def destinations(request):
    return render(request, 'travel/destinations.html', {'title': 'Destinations'})

def asia(request):
    return render(request, 'travel/destinations/asia.html', {'title': 'Asia'})

def southeastasia(request):
    return render(request, 'travel/destinations/southeastasia.html', {'title': 'South East Asia'})

def brunei(request):
    return render(request, 'travel/destinations/southeastasia/brunei.html', {'title': 'Brunei'})

def cambodia(request):
    return render(request, 'travel/destinations/southeastasia/cambodia.html', {'title': 'Cambodia'})

def indonesia(request):
    return render(request, 'travel/destinations/southeastasia/indonesia.html', {'title': 'Indonesia'})

def laos(request):
    return render(request, 'travel/destinations/southeastasia/laos.html', {'title': 'Laos'})

def malaysia(request):
    return render(request, 'travel/destinations/southeastasia/malaysia.html', {'title': 'Malaysia'})

def philippines(request):
    return render(request, 'travel/destinations/southeastasia/philippines.html', {'title': 'Philippines'})

def singapore(request):
    return render(request, 'travel/destinations/southeastasia/singapore.html', {'title': 'Singapore'})

def thailand(request):
    return render(request, 'travel/destinations/southeastasia/thailand.html', {'title': 'Thailand'})

def vietnam(request):
    return render(request, 'travel/destinations/southeastasia/vietnam.html', {'title': 'Vietnam'})

def southasia(request):
    return render(request, 'travel/destinations/southasia.html', {'title': 'South Asia'})

def sri_lanka(request):
    return render(request, 'travel/destinations/southasia/sri_lanka.html', {'title': 'Sri Lanka'})