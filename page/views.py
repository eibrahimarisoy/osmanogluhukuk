from django.shortcuts import get_object_or_404, render
from attorney.models import Attorney
from practice_area.models import PracticeArea, Faq
from page.models import Carousel


def index(request):
    context = dict()
    practice_areas = PracticeArea.objects.filter(
        status="published"
    )
    carousels = Carousel.objects.filter(
        status="published"
    )
    context['banner_page_name'] = "Ana Sayfa"
    context['practice_areas'] = practice_areas
    context['carousels'] = carousels
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
    context = dict()
    attorneys = Attorney.objects.filter(
    status="published"
    ).exclude(cover_image="")[::-1]  

    context['banner_page_name'] = "Ekibimiz"
    context['attorneys'] = attorneys
    return render(request, "page/attorneys.html", context)


def practice_areas(request):
    context = dict()
    practice_areas = PracticeArea.objects.filter(
        status="published"
    )    
    context['banner_page_name'] = "Çalışma Alanlarımız"
    context['practice_areas'] = practice_areas
    return render(request, "page/practice_areas.html", context)


def practice_area_details(request, practice_area_name):
    context = dict()
    practice_area = get_object_or_404(
                    PracticeArea,
                    slug=practice_area_name
                    )
    practice_areas = PracticeArea.objects.filter(
        status="published",
        category=practice_area.category
    ).exclude(id=practice_area.id)

    context['banner_page_name'] = "Çalışma Alanlarımız"
    context['practice_area_name'] = practice_area.title
    context['practice_area'] = practice_area
    context['practice_areas'] = practice_areas
    return render(request, "page/practice_area_details.html", context)


def attorney_details(request, attorney_name):    
    context = dict()
    attorney = Attorney.objects.get(slug=attorney_name)
    practice_areas = PracticeArea.objects.filter(
        status="published"
    ) 
    context['banner_page_name'] = "Ekibimiz"
    context['attorney_name'] = attorney.name
    context['attorney'] = attorney
    context['practice_areas'] = practice_areas
    return render(request, "page/attorney_details.html", context)


def error_404_view(request, exception):
    return render(request, 'page/page-404.html')
    