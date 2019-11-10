from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, View
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import ArtForm, SignUpForm, ArtworkForm
from .models import Art
from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import random
import logging
from django.views.generic.edit import UpdateView


logger = logging.getLogger(__name__)

class Homepage(TemplateView):
    template_name = "tindartapp/index.html"

class Artworks(UpdateView):
    model = Art
    form_class = ArtworkForm
    template_name = 'tindartapp/Artwork.html'
    #pk_url_kwarg = 'artwork_id' 
    disliking = False
    context = {}

    def get_initial(self, *args, **kwargs):
        return { 'artwork': get_object_or_404(Art, pk=self.kwargs['pk']) }

    print(context)

    def post(self, request, *args, **kwargs):
        artwork = get_object_or_404(Art, pk=self.kwargs['pk'])
        if "dislike" in request.POST:
            logger.error("booga")
            self.disliking = True
            request.POST._mutable = True
            artwork.likes = artwork.likes - 1
            artwork.save()
        else:
            self.disliking = False
            artwork.likes = artwork.likes + 1
            artwork.save()
        new_artwork = Art.objects.order_by('?').first()
        print(new_artwork.id)
        return HttpResponseRedirect(new_artwork.get_absolute_url())        
'''
    def form_Valid(self, form):
        artwork = get_object_or_404(Art, pk=self.kwargs['artwork_id'])
        print(artwork.id)
        if(self.disliking == True):
            artwork.likes -= 1
        else:
            artwork.likes += 1
        form.save()
        new_artwork = Art.objects.order_by('?').first()
        print(new_artwork.id)
        return HttpResponseRedirect(new_artwork.get_absolute_url())
'''
'''
class Mainpage(View):
    number_of_records = models.Art.objects.count()
    random_index = int(random.random()*number_of_records)+1
    random_art = models.Art.get(pk = random_index)
    template_name = "tindartapp/pp.html"
'''
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def ArtW(request): 
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
