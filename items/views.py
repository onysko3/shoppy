from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Item


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.all()
    template_name = 'items/list.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'items/detail.html'


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ('title', 'body', 'price', 'category', 'location', 'picture')
    template_name = 'items/update.html'

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    template_name = 'items/delete.html'
    success_url = reverse_lazy('items:list')

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    template_name = 'items/create.html'
    fields = ('title', 'body', 'price', 'category', 'location', 'picture',)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)