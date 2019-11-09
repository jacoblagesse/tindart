from django.shortcuts import render

from django.http import HttpResponseRedirect

from .forms import UserForm, ArtistForm, ArtForm

def User(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/')
    else:
        form = UserForm()

    return render(request, 'tindartapp/userform.html', {'form': form})

def Artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/artist/')
    else:
        form = ArtistForm()

    return render(request, 'tindartapp/artistform.html', {'form': form})

def Art(request): 
    if request.method == 'POST': 
        form = ArtForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect('/art/')
    else: 
        form = ArtForm() 
    return render(request, 'tindartapp/artform.html', {'form' : form}) 
