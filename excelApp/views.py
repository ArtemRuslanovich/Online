from django.shortcuts import render, redirect
from django.http import HttpResponse
import openpyxl


def my_view(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        phone = request.POST.get('phone')
        description = request.POST.get('description')

        data = {
            "ФИО": fullname,
            "Номер телефона": phone,
            "Краткое описание": description
        }

        excel_file = r"C:\Users\USER\PycharmProjects\YMC\media\test.xlsx"

        try:
            workbook = openpyxl.load_workbook(excel_file)
            sheet = workbook.active

            for key, value in data.items():
                sheet.append([key, value])

            workbook.save(excel_file)

            return redirect('thanks')
        except Exception as e:
            return HttpResponse(f"ебнулось: {e}")

    return render(request, 'thanks.html')


def thanks(request):
    fullname = request.GET.get('fullname')
    phone = request.GET.get('phone')
    description = request.GET.get('description')

    return render(request, 'thanks.html', {'fullname': fullname, 'phone': phone, 'description': description})


def first_page(request):
    return render(request, './index.html')


def page_about(request):
    return render(request, './about.html')


def tax_free(request):
    return render(request, './TAXFREE.html')


def map(request):
    return render(request, './map.html')

