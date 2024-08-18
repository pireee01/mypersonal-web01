from django.shortcuts import render, get_object_or_404, redirect
from .models import Certificate, Portfolio, Microblog
from django.conf import settings
from .forms import CertificateForm, MicroblogForm




def home(request):
    return render(request, 'main/home.html')

def microblog_new(request):
    if request.method == 'POST':
        form = MicroblogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('microblog_list')
    else:
        form = MicroblogForm()
    return render(request, 'main/microblog_form.html', {'form': form})

def microblog_detail(request, pk):
    microblog = get_object_or_404(Microblog, pk=pk)
    return render(request, 'main/microblog_detail.html', {'microblog': microblog})

def microblog_edit(request, pk):
    microblog = get_object_or_404(Microblog, pk=pk)
    if request.method == "POST":
        form = MicroblogForm(request.POST, instance=microblog)
        if form.is_valid():
            form.save()
            return redirect('microblog_detail', pk=microblog.pk)
    else:
        form = MicroblogForm(instance=microblog)
    return render(request, 'microblog_form.html', {'form': form})

def microblog_delete(request, pk):
    microblog = get_object_or_404(Microblog, pk=pk)
    if request.method == "POST":
        microblog.delete()
        return redirect('microblog_list')
    return render(request, 'microblog_delete.html', {'microblog': microblog})

def microblog_list(request):
    microblogs = Microblog.objects.all().order_by('-created_at')
    return render(request, 'main/microblog_list.html', {'microblogs': microblogs})

def microblog_detail(request, pk):
    microblog = get_object_or_404(Microblog, pk=pk)
    return render(request, 'main/microblog_detail.html', {'microblog': microblog})

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'main/certificates.html', {'certificates': certificates})

def certificate_detail(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    return render(request, 'main/certificate_detail.html', {'certificate': certificate})

def certificate_new(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            certificate = form.save()
            return redirect('certificate_detail', pk=certificate.pk)
    else:
        form = CertificateForm()
    return render(request, 'main/certificate_edit.html', {'form': form})

def certificate_edit(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            certificate = form.save()
            return redirect('certificate_detail', pk=certificate.pk)
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'main/certificate_edit.html', {'form': form})

def certificate_delete(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        certificate.delete()
        return redirect('certificates')
    return render(request, 'main/certificate_delete.html', {'certificate': certificate})

def portfolio(request):
    image_names = [
        '1.jpg',
        '2.jpg',
        '3.jpg',
        '4.jpg',
        '5.jpg'
    ]
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio': portfolio,
        'image_names': image_names
    }
    return render(request, 'main/portfolio.html', context)

def chatbot(request):
    return render(request, 'main/chatbot.html')


