from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    View,
    TemplateView,
    DetailView,
)

from .models import (
    Item,
    Shop,
    Department,
)

from .forms import (
    ItemForm,
    DepartmentForm,
    ItemWithoutDepartmentForm
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
    paginate_by = 12

    def get_queryset(self):
        # return Item.objects.filter()
        return Item.objects.select_related('department', 'department__shop')
        # return Item.objects.all()

    def get_paginate_by(self, queryset):
        page_number = self.request.GET.get('page_number')
        if page_number is not None:
            self.paginate_by = page_number
        return super(ItemListView, self).get_paginate_by(
            self.get_queryset()
        )

    def get(self, request, *args, **kwargs):
        return super(ItemListView, self).get(request, *args, **kwargs)


#  Реализация View когда у нас две формы
class CreateDepartmentAndItem(View):
    def get(self, request, *args, **kwargs):
        department_form = DepartmentForm()
        item_form = ItemWithoutDepartmentForm()
        context = {'department_form': department_form, 'item_form': item_form}
        return TemplateResponse(request, 'shop_app/department_and_item_create.html', context=context)

    def post(self, request, *args, **kwargs):
        department_form = DepartmentForm(data=request.POST)
        item_form = ItemWithoutDepartmentForm(request.POST)
        if not department_form.is_valid():
            context = {'department_form': department_form, 'item_form': item_form}
            return TemplateResponse(request, 'shop_app/department_and_item_create.html', context=context)
        if not item_form.is_valid():
            context = {'department_form': department_form, 'item_form': item_form}
            return TemplateResponse(request, 'shop_app/department_and_item_create.html', context=context)
        department = department_form.save(commit=True)
        item = item_form.save(commit=False)
        item.department = department
        item.save()
        return HttpResponseRedirect(reverse('shop_app:item_list'))


class ItemCreate(CreateView):
    template_name = 'shop_app/item_create.html'
    model = Item
    form_class = ItemForm


class ItemDetail(DetailView):
    model = Item
    template_name = 'shop_app/item_detail.html'
    context_object_name = 'item'

    def get_queryset(self):
        return Item.objects.select_related('department', 'department__shop')


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
