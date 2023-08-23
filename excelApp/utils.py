import os
import pandas as pd
import openpyxl
from tempfile import NamedTemporaryFile

from openpyxl import load_workbook


def create_excel_file():
    file_path = 'media/test.xlsx'
    wb = load_workbook(filename=file_path)
    ws = wb.active()


def save_data_to_excel(data):
    excel_file_path = r'C:\Users\USER\PycharmProjects\YMC\media\test.xlsx'
    if not os.path.exists(excel_file_path):
        create_excel_file()

    df = pd.read_excel(excel_file_path)
    df = df.append(data, ignore_index=True)
    df.to_excel(excel_file_path, index=False)
