from attorney.models import Firm

def firm_data(request):
    context = dict()
    
    context['firm'] = Firm.objects.filter().first()
       
    return context