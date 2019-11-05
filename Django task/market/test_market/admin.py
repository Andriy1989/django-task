from django.contrib import admin
# Register your models here.
from .forms import CsvImportForm
from django.shortcuts import render,redirect
from django.urls import path
from datetime import datetime
from .models import User,Goods,Orders
import csv
from io import TextIOWrapper

#import os
admin.site.register(Goods)			
admin.site.register(Orders)			
#admin.site.register(User)	

@admin.register(User)	
class UserAdmin(admin.ModelAdmin):
    
    change_list_template = "test_market/changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('import-csv/', self.import_csv),]
        return my_urls + urls
    
    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            csv_file =TextIOWrapper(csv_file, encoding=request.encoding)
            reader = csv.reader(csv_file, delimiter=',')
            
            
            for row in reader:
                self.message_user(request, row)
                try:
                    input_data = User(FirstName=row[0],
                                      LastName=row[1],
                                      BirthDate=datetime.strptime(row[2], "%Y/%m/%d"),
                                      RegistrationDate=datetime.strptime(row[3], "%Y/%m/%d"))
                  
                    input_data.save()
                except Exception as e:
                    print (e)
                    self.message_user(request, "there was a problem with line")
               
            self.message_user(request, "Your csv file has been imported")
            return redirect("..")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)
	     
                    
                    
                    
                    
                 