from django.shortcuts import render
from .models import Order
from .forms import OrderForm


# Create your views here.
def first_page(request):
    form = OrderForm()
    dict_obj = {
        'form': form,
    }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        return render(request, './thanks.html', {'name': name, })
    else:
        return render(request, './thanks.html')


def page_about(request):
    return render(request, './about.html')


def tax_free(request):
    return render(request, './TAXFREE.html')


def map(request):
    return render(request, './map.html')
