from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Book,Admin
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'home.html')

 # Retrieve all books
def all_books(request):
    books_data = Book.objects.all()
    context= {'book': books_data}
    return render(request, 'all_books.html', context )


# Create a book entry
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        published_date = request.POST['published_date']
        isbn_number = request.POST['isbn_number']
        
        # Create the book record
        book = Book(title= title,author = author,published_date=published_date,isbn_number=isbn_number)

        book.save()
        return redirect('/all_books')
    return render(request, 'create_book.html')



# Update a book entry
def update_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = request.POST['published_date']
        book.isbn_number = request.POST['isbn_number']
        book.save()

        return redirect('/all_books')
    else:
        context = { 'book' : book }
        return render(request, 'update_book.html', context)

    # Delete a book entry
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/all_books')

# Admin signup view
def admin_signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Check if the admin already exists
        if Admin.objects.filter(email=email).exists():
            messages.error(request, "Admin with this email already exists.")
            return redirect('admin_signup')
        
        # Create a new admin
        admin = Admin.objects.create(email=email, password=password)
        admin.save()
        messages.success(request, "Admin registered successfully.")
        return redirect('admin_login')
    return render(request, 'admin_signup.html')

    # Admin login view
def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Authenticate the admin
        try:
            admin = Admin.objects.get(email=email)
            if admin.password == password:
                login(request, admin)
                return redirect('all_books')
            else:
                messages.error(request, "Invalid password.")
        except Admin.DoesNotExist:
            messages.error(request, "Admin does not exist.")
        
    return render(request, 'admin_login.html')