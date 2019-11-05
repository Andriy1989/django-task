# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:56:47 2019

@author: Andrij
"""

from .models import User,Goods,Orders
import csv
from django import forms
class CsvImportForm(forms.Form):

    csv_file = forms.FileField()