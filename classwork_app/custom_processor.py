from datetime import datetime
from classwork_app.models import Category

def footer_date(request):
    footer_time = datetime.now()
    context = {'site_date':footer_time}
    return context

def menu_cat(request):
    category = Category.objects.all()
    kwargs = {'cat':category}
    return kwargs