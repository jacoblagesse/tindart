from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ArtForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)

class Homepage(TemplateView):
    template_name = "tindartapp/index.html"

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def Art(request): 
    if request.method == 'POST': 
        form = ArtForm(request.POST, request.FILES) 
        logger.error(request.user.username)
        if form.is_valid(): 
            obj = form.save(commit=False)
            obj.user = request.user.username
            form.save()
            return HttpResponseRedirect('/art/')
    else: 
        form = ArtForm() 
    return render(request, 'tindartapp/artform.html', {'form' : form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form}) 
