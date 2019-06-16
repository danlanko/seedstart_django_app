from django.views import generic
from .forms import PersonForm
from django.urls import reverse_lazy
from .models import PersonModel
# Create your views here.


class Homepage(generic.TemplateView):
    template_name = 'index.html'


class PersonCreate(generic.CreateView):
    form_class = PersonForm
    template_name = 'new_person.html'
    success_url = reverse_lazy('person_list')


class PersonList(generic.ListView):
    model = PersonModel
    template_name = 'list_person.html'

