from django.shortcuts import redirect, render
from amali_slider.models import Slider
from amali_setting.models import SiteSetting


# header code behind
def header(request, *args, **kwargs):
    contex = {"title": "title"}
    return render(request, "shared/Header.html", contex)

#footer code behind
def footer(request, *args, **kwargs):

    setting = SiteSetting.objects.first()

    contex = {'setting': setting}
    return render(request, "shared/Footer.html", contex)



def home_page(request):
    sliders = Slider.objects.all()
    contex = {
        "data": "new data",
        'sliders': sliders
    }
    return render(request, "home_page.html", contex)