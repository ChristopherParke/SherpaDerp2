from django.shortcuts import render
from .models import MFP, Accessory

# Create your views here.
def products(request):

    mfpName = MFP.objects.filter(name='IM C2000')
    
    context = {
        "MFP": mfpName
    }
    
    return render(request, 'products/products.html', context)