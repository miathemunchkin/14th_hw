from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'


from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Author, Quote
from .forms import AuthorForm, QuoteForm

@login_required
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request, 'quotes/add_author.html', {'form': form})

@login_required
def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            return redirect('home')
    else:
        form = QuoteForm()
    return render(request, 'quotes/add_quote.html', {'form': form})

from django.views.generic import ListView, DetailView

class AuthorListView(ListView):
    model = Author
    template_name = 'quotes/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'quotes/author_detail.html'

class QuoteListView(ListView):
    model = Quote
    template_name = 'quotes/quote_list.html'

from django.contrib.auth.views import PasswordResetView

class CustomPasswordResetView(PasswordResetView):
