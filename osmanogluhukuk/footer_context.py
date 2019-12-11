from practice_area.models import PracticeArea

def footer_data(request):
    context = dict()
    
    context['practice_areas'] = PracticeArea.objects.filter(
        status="published"
    ).order_by('title')
       
    return context