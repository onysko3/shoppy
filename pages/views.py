from django.urls import reverse_lazy
from django.views.generic import RedirectView


class HomePageView(RedirectView):
    url = reverse_lazy('items:list')
