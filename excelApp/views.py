from django.shortcuts import render
from openpyxl import load_workbook

from .forms import Form
from .utils import save_data_to_excel


def view(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            fullname = form.cleaned_data['fullname']
            phone = form.cleaned_data['phone']
            description = form.cleaned_data['description']

            data = {
                "ФИО": fullname,
                "Номер телефона": phone,
                "Краткое описание": description,
            }

            # Сохраняем данные в Excel-файл
            file_path = 'media/test.xlsx'
            wb = load_workbook(filename=file_path)
            ws = wb.active()


            return render(request, 'thanks.html')
    else:
        form = Form()

    return render(request, 'thanks.html', {'form': form})


def first_page(request):
    return render(request, './index.html')


def page_about(request):
    return render(request, './about.html')


def tax_free(request):
    return render(request, './TAXFREE.html')


def map(request):
    return render(request, './map.html')


def thanks_page(request):
    return render(request, './thanks.html')
