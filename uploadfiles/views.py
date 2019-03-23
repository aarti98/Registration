from .models import Document
from django.http import Http404
from django.conf import settings
from .forms import DocumentForm
from django.shortcuts import render,redirect

User = settings.AUTH_USER_MODEL


def upload_file(request):
    user = request.user

    if user.is_authenticated:
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('homepage')
        else:
            form = DocumentForm()
        return render(request, 'uploadfiles/upload_file.html', {
            'form': form
        })

    else:
        raise Http404("You need to Login first")


def display_file(request):
    files = Document.objects.all()
    return render(request, 'uploadfiles/display.html', {'files': files})
