from django.shortcuts import render
from attorney.models import Attorney
from practice_area.models import PracticeArea

# Create your views here.

def index(request):
    attorneys = Attorney.objects.filter(
        status="published"
    ).exclude(cover_image="")[::-1]

    practice_areas = PracticeArea.objects.filter(
        status="published"
    )
    context = dict()
    context['banner_page_name'] = "Ana Sayfa"
    context['attorneys'] = attorneys
    context['practice_areas'] = practice_areas
    return render(request, "page/index.html", context)

def about(request):
    context = dict()
    context['banner_page_name'] = "Hakkımızda"
    return render(request, "page/about.html", context)

def contact(request):    
    context = dict()
    context['banner_page_name'] = "İletişim"
    return render(request, "page/contact.html", context)

def attorneys(request):  
    attorneys = Attorney.objects.filter(
    status="published"
    ).exclude(cover_image="")[::-1]  
    context = dict()
    context['banner_page_name'] = "Avukatlarımız"
    context['attorneys'] = attorneys

    return render(request, "page/attorneys.html", context)

def single_attorney(request, attorney_name):    
    attorney = Attorney.objects.get(slug=attorney_name)
    context = dict()
    context['banner_page_name'] = "Avukatlarımız"
    context['attorney_name'] = attorney.name
    context['attorney'] = attorney
    return render(request, "page/single_attorney.html", context)

def practice_areas(request):
    practice_areas = PracticeArea.objects.filter(
        status="published"
    )    
    context = dict()
    context['banner_page_name'] = "Çalışma Alanlarımız"
    context['practice_areas'] = practice_areas
    return render(request, "page/practice_areas.html", context)

def single_practice_area(request, practice_area_name):
    practice_area = PracticeArea.objects.get(slug=practice_area_name)    
    context = dict()
    context['banner_page_name'] = "Çalışma Alanlarımız"
    context['practice_area_name'] = practice_area.title
    context['practice_area'] = practice_area
    return render(request, "page/single_practice_area.html", context)