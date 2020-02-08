from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    TemplateView)

from .models import (
    Item,
    Shop,
    Department,
)

from .forms import (
    ItemForm,
)


def index(request):
    return render(request, 'shop_app/base.html', context={})


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('users_app:login')
    template_name = 'shop_app/base.html'


class ItemListView(ListView):
    template_name = 'shop_app/item_list.html'
    model = Item
    context_object_name = 'item_list'

    def get_queryset(self):
        # return Item.objects.filter()
        return Item.objects.all()

    def get(self, request, *args, **kwargs):
        return super(ItemListView, self).get(request, *args, **kwargs)


class ItemCreate(CreateView):
    template_name = 'shop_app/item_create.html'
    model = Item
    form_class = ItemForm


class ItemUpdate(UpdateView):
    template_name = 'shop_app/item_create.html'
    model = Item
    form_class = ItemForm


class ItemDelete(DeleteView):
    model = Item
    # при успешном удалении редиректим на....
    success_url = reverse_lazy('shop_app:item_list')
    # указываем шаблон для страницы подтверждения удаления
    template_name = 'shop_app/confirm_delete.html'
