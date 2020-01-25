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
)

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


# if request.method == 'GET':
#     student_form = StudentForm()
#     return render(
#         request,
#         'my_app/create_student.html',
#         context={'student_form': student_form}
#     )
# elif request.method == 'POST':
#     student_form = StudentForm(request.POST)
#     if student_form.is_valid():
#         student_form.save(commit=True)
#         return HttpResponseRedirect(
#             reverse('my_app:get_all_students')
#         )

class MyView(View):
    def post(self, request, *args, **kwargs):
        pass

    def get(self, request, *args, **kwargs):
        pass


class ItemListView(ListView):
    template_name = 'shop_app/item_list.html'
    model = Item
    context_object_name = 'item_list'

    # def get(self, request, *args, **kwargs):
    #     return super(ItemListView, self).get(request, *args, **kwargs)


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
