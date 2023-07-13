from django.shortcuts import render, HttpResponse, redirect
from app.models import Book
from django.contrib import messages
from django import forms
from django.contrib.auth.decorators import login_required
import csv

# Create your views here.
@login_required
def welcome_page(request):     # HTTP request
    return render(request, "welcome.html")


import datetime
@login_required
def show_all_books(request):
    books = Book.objects.filter(is_active=True)  # get only active records from database
    return render(request, "showbooks.html", {"allbooks": books, "today": datetime.datetime.now()})

@login_required
def show_single_book(request, bid):
    try:

         book_object = Book.objects.get(id=bid)
    except Book.DoesNotExist :
         return HttpResponse("Book does not exist...!")
    return render(request=request, template_name="bookdetails.html", context={"book": book_object})
    
def commom_var(request):
    final_dict = request.POST
    book_name = final_dict.get("nm")
    book_price = final_dict.get("prc")
    book_qty = final_dict.get("qty")
    book_is_published = final_dict.get("is_pub")  
    return book_name, book_price, book_qty, book_is_published  

@login_required
def add_single_book(request):
    if request.method == "POST":
    #    user = request.user
       book_name, book_price, book_qty, book_is_published = commom_var(request)
       if book_is_published == "YES":
           is_pub = True
       elif book_is_published =="NO":
            is_pub = False
       Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_published=is_pub) #created_by = user) 
       messages.success(request, "Book has been added successfully.....!")
       return redirect("show_books")
    
    elif request.method == "GET":
        # request.GET  --- query params 
        return render(request, "addbook.html")


@login_required
def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "bookedit.html", {"single_book": book_obj})
    elif request.method == "POST":
        book_name, book_price, book_qty, book_is_published = commom_var(request)
        if book_is_published == "YES":
            is_pub = True
        else:
            is_pub = False
        #  update data
        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_published = is_pub
        book_obj.save()
        messages.success(request, f"{book_obj.name} has been updated successfully...!")
        return redirect("show_books")
    
@login_required
def delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()  # hard delete
    return redirect("show_books")

@login_required
def soft_delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = False   # soft delete
    book_obj.save()
    messages.success(request,"Book has been deleted successfully")
    return redirect("show_books")

@login_required
def show_inactive_books(request):
    
      books = Book.objects.filter(is_active=False)
      return render(request,'inactivebooks.html', {"allbooks": books})

@login_required
def restore_single_book(request,bid):
    books= Book.objects.get(id=bid)
    books.is_active = True
    books.save()
    messages.success(request,"Book is restored")
    return redirect("show_books")

def create_csv(request):
    response = HttpResponse(content_type='text/csv') 
    response['content_Disposition']= 'attachment; filename="test.csv"'
    writer = csv.writer(response)
    writer.writerow(["name", "price", "qty", "is_published", "is_active"])
    books = Book.objects.all().values_list("name", "price", "qty", "is_published", "is_active")
    for book in books:
        writer.writerow(book)
    return response

def upload_csv(request):
    file = request.FILES['csv_file']  
    data = file.read().decode('utf-8').splitlines()
    expected_header_lst = ["name", "price", "qty", "is_published"]
    expected_header_lst.sort()
    actual_header_lst = data[0].split(",")
    actual_header_lst.sort()
    if expected_header_lst!=actual_header_lst:
        return HttpResponse("Error.......headers are not equal.")
    reader = csv.DictReader(data)
    lst = []
    for element in reader:
      is_pub = element.get("is_published") 
      if is_pub =="TRUE":
          is_pub = "True"
      else:
          is_pub = "False"
          lst.append(Book(name=element.get("name"),price=element.get("price"), qty=element.get("qty"),is_published=is_pub))  
          Book.objects.bulk_create(lst)
          print(lst)
    return HttpResponse("success")  

# # --------------------------------for forms-----------------------------------

from app.forms import GeeksForm, BookForm, AddressForm
  
# Create your views here.

@login_required
def form_view(request):
    if request.method == "POST":
      print("in post request")
      data = request.POST
      print(data)
      form = BookForm(data)
      if form.is_valid():
          form.save()
          return redirect("show_books")
    # print(GeeksForm())
    elif request.method == "GET":
        print("in get request")
        return render(request, "book_forms_test.html",{"bookform": BookForm()})












# <!-- <form  method = "post">
#     {% csrf_token %}
#     <div class="form-row">
#         <div class="form-group col-md-6 mb-0">
#           {{ form.email|as_crispy_field }}
#         </div>
#         <div class="form-group col-md-6 mb-0">
#           {{ form.password|as_crispy_field }}
#         </div>
#       </div>
#       {{ form.address_1|as_crispy_field }}
#       {{ form.address_2|as_crispy_field }}
#       <div class="form-row">
#         <div class="form-group col-md-6 mb-0">
#           {{ form.city|as_crispy_field }}
#         </div>
#         <div class="form-group col-md-4 mb-0">
#           {{ form.state|as_crispy_field }}
#         </div>
#         <div class="form-group col-md-2 mb-0">
#           {{ form.zip_code|as_crispy_field }}
#         </div>
#       </div>
#       {{ form.check_me_out|as_crispy_field }}
#       <button type="submit" class="btn btn-primary">Sign in</button>
#     </form> -->