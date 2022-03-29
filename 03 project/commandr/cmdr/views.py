from pyexpat import model
from django.views.generic import ListView
from.models import cmdr

class homepageview(ListView):
    model = cmdr
    template_name = 'home.html'
    


