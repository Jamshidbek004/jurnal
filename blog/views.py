from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic import ListView
from blog.models import *
from django.core.paginator import Paginator


# Create your views here.

def asosiy(request):
    jurnal = Jurnallar.objects.all()
    turi = Fayl_turi.objects.all()
    context = {
        "jurnal": jurnal,
        "fayl_turi": turi
    }
    return render(request, "landing page/index.html", context=context)


def jurnal_detel(request, id):
    detel = get_object_or_404(Jurnallar, id=id)
    context = {
        "jurnal_detel": detel
    }
    return render(request, "malumotlar.html", context=context)


def yangilik_detel(request, id):
    detel = get_object_or_404(Yangiliklar, id=id)
    context = {
        "yangilik_detel": detel
    }
    return render(request, "yangilik_detel.html", context=context)


class SearchResultList(ListView):
    model = Jurnallar
    template_name = 'landing page/index.html'
    context_object_name = 'jurnal'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Jurnallar.objects.filter(
            Q(nomi__icontains=query) | Q(Text__icontains=query)
        )


def sinov_detel(request, id=id):
    n = Jurnallar.objects.filter(kategory=id)
    turi = Fayl_turi.objects.all()
    context = {
        "jurnal": n,
        "fayl_turi": turi
    }
    return render(request, "landing page/index.html", context=context)


def jurnallar(request):
    contact_list = Jurnallar.objects.all()
    paginator = Paginator(contact_list, 1)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "jurnallar/index.html", {"page_obj": page_obj})


def yangiliklar(request):
    contact_list = Yangiliklar.objects.all()
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "yangiliklar/yangiliklar.html", {"page_obj": page_obj})
