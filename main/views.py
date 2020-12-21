from django.shortcuts import render
from .models import Data
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# Create your views here.

clown = 'None'

def index(request):
    who = Data.objects.all()
    # print(who)
    print(Data.Who_is_clown)
    return render(request, 'main/index.html', {'Clown': Data.Who_is_clown})

def about(request):
    return render(request, 'main/about.html')

def Oleg_Malyshev(request):
    if 'Oleg_Malyshev' not in Data.Amound_of_times:
        Data.Amound_of_times['Oleg_Malyshev'] = 0
    status = "unfunny downer"
    if request.method == 'POST':
        if Data.Who_is_clown != "Oleg Malyshev":
            Data.Amound_of_times['Oleg_Malyshev'] += 1
            status = "clown"

            img = Image.open("main\static\images\clown.png")
            draw = ImageDraw.Draw(img)
            draw.text((100, 250), "Oleg Malyshev", (0, 0, 0), font=ImageFont.truetype("font.ttf", 20))
            img.save('main\static\images\clown2.png')

        Data.Who_is_clown = "Oleg_Malyshev"
    return render(request, 'main/Oleg_Malyshev.html', {"Times": Data.Amound_of_times['Oleg_Malyshev'], "Status": status})

def Rodion_Pronin(request):
    if 'Rodion_Pronin' not in Data.Amound_of_times:
        Data.Amound_of_times['Rodion_Pronin'] = 0
    status = "unfunny downer"
    if request.method == 'POST':
        if Data.Who_is_clown != "Rodion Pronin":
            Data.Amound_of_times['Rodion_Pronin'] += 1
            status = "clown"

            img = Image.open("main\static\images\clown.png")
            draw = ImageDraw.Draw(img)
            draw.text((100, 250), "Rodion Pronin", (0, 0, 0), font=ImageFont.truetype("font.ttf", 20))
            img.save('main\static\images\clown2.png')

        Data.Who_is_clown = "Rodion Pronin"
    return render(request, 'main/Rodion_Pronin.html', {"Times": Data.Amound_of_times['Rodion_Pronin'], "Status": status})

def Alexander_Petrov(request):
    if 'Alexander_Petrov' not in Data.Amound_of_times:
        Data.Amound_of_times['Alexander_Petrov'] = 0
    status = "unfunny downer"
    if request.method == 'POST':
        if Data.Who_is_clown != "Alexander Petrov":
            Data.Amound_of_times['Alexander_Petrov'] += 1
            status = "clown"

            img = Image.open("main\static\images\clown.png")
            draw = ImageDraw.Draw(img)
            draw.text((100, 250), "Alexander Petrov", (0, 0, 0), font=ImageFont.truetype("font.ttf", 20))
            img.save('main\static\images\clown2.png')

        Data.Who_is_clown = "Alexander_Petrov"
    return render(request, 'main/Alexander_Petrov.html', {"Times": Data.Amound_of_times['Alexander_Petrov'], "Status": status})

def Nikita_Kinelovsky(request):
    if 'Nikita_Kinelovsky' not in Data.Amound_of_times:
        Data.Amound_of_times['Nikita_Kinelovsky'] = 0
    status = "unfunny downer"
    if request.method == 'POST':
        if Data.Who_is_clown != "Nikita Kinelovsky":
            Data.Amound_of_times['Nikita_Kinelovsky'] += 1
            status = "clown"

            img = Image.open("main\static\images\clown.png")
            draw = ImageDraw.Draw(img)
            draw.text((100, 250), "Nikita Kinelovsky", (0, 0, 0), font=ImageFont.truetype("font.ttf", 20))
            img.save('main\static\images\clown2.png')

        Data.Who_is_clown = "Nikita Kinelovsky"
    return render(request, 'main/Nikita_Kinelovsky.html', {"Times": Data.Amound_of_times['Nikita_Kinelovsky'], "Status": status})

def Stepan_Bazrov(request):
    if 'Stepan_Bazrov' not in Data.Amound_of_times:
        Data.Amound_of_times['Stepan_Bazrov'] = 0
    status = "unfunny downer"
    if request.method == 'POST':
        if Data.Who_is_clown != "Stepan Bazrov":
            Data.Amound_of_times['Stepan_Bazrov'] += 1
            status = "clown"

            img = Image.open("main\static\images\clown.png")
            draw = ImageDraw.Draw(img)
            draw.text((100, 250), "Stepan Bazrov", (0, 0, 0), font=ImageFont.truetype("font.ttf", 20))
            img.save('main\static\images\clown2.png')

        Data.Who_is_clown = "Stepan Bazrov"



    return render(request, 'main/Stepan_Bazrov.html', {"Times": Data.Amound_of_times['Stepan_Bazrov'], "Status": status})