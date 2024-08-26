import gspread
from django.conf import settings
from decouple import config
import json

def G_sheet(name,email,phone,source):
    sa = gspread.service_account("/Users/Erfan/Workspace/brandexpert/secret_key.json")
    sh = sa.open("Clients")
    wks = sh.worksheet('Data')
    row = [name, email, phone, source]
    wks.append_row(row)
