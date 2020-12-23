from django.shortcuts import render
from .models import Data
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw, ImageOps
import time
import requests

# from django.shortcuts import render_to_response


# Create your views here.

clown = 'None'


def index(request):
    who = Data.objects.all()
    # print(who)
    print(Data.Who_is_clown)

    if Data.Who_is_clown == 'No one':
        img = Image.open("main/static/images/clown.png")
        img.save('main/static/images/clown2.png')

    return render(request, 'main/index.html', {'Clown': Data.Who_is_clown, 'page': Data.clownUrl})


def about(request):
    return render(request, 'main/about.html')


def handleClowns(request, name, vkurl):
    if name not in Data.Amound_of_times.keys():
        Data.Amound_of_times[name] = 0
    status = "unfunny downer"
    if request.method == 'POST':
        if (time.time() - Data.time) > 1:
            if Data.Who_is_clown != name:
                Data.Amound_of_times[name] += 1
                status = "clown"
                Data.clownUrl = vkurl
                r = requests.session()
                img = Image.open("main/static/images/clown.png")
                url = r.get(vkurl).text[
                      r.get(vkurl).text.find('https://sun'):r.get(
                          vkurl).text.find('ava=1') + 5]

                try:
                    im = Image.open(requests.get(url, stream=True).raw)
                except:
                    im = Image.open('main/static/images/Anonym.png')
                mask = Image.open('main/static/images/mask2.png').convert('L')
                im = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                im.putalpha(mask)
                img_w, img_h = im.size
                bg_w, bg_h = img.size
                im = im.resize((round(img_w * 2.5), round(img_h * 2.5)))
                img.paste(im, (375, 48), im)

                # img = Image.open("main\static\images\clown.png")
                draw = ImageDraw.Draw(img)
                draw.text((100, 250), name, (0, 0, 0), font=ImageFont.truetype("KaushanScript-Regular.otf", 20))
                img.save('main/static/images/clown2.png')

            Data.Who_is_clown = name
    return status


def Oleg_Malyshev(request):
    status = handleClowns(request, "Oleg Malyshev", 'https://vk.com/maloleg')
    return render(request, 'main/Oleg_Malyshev.html',
                  {"Times": Data.Amound_of_times['Oleg Malyshev'], "Status": status})


def Rodion_Pronin(request):
    status = handleClowns(request, "Rodion Pronin", 'https://vk.com/millerick')
    return render(request, 'main/Rodion_Pronin.html',
                  {"Times": Data.Amound_of_times['Rodion Pronin'], "Status": status})


def Alexander_Petrov(request):
    status = handleClowns(request, "Alexander Petrov", 'https://vk.com/sasha_c')
    return render(request, 'main/Alexander_Petrov.html',
                  {"Times": Data.Amound_of_times['Alexander Petrov'], "Status": status})


def Nikita_Kinelovsky(request):
    status = handleClowns(request, "Nikita Kinelovsky", 'https://vk.com/rends_east')
    return render(request, 'main/Nikita_Kinelovsky.html',
                  {"Times": Data.Amound_of_times['Nikita Kinelovsky'], "Status": status})


def Stepan_Bazrov(request):
    status = handleClowns(request, "Stepan Bazrov", 'https://vk.com/bazrv')
    return render(request, 'main/Stepan_Bazrov.html',
                  {"Times": Data.Amound_of_times['Stepan Bazrov'], "Status": status})

def Alexander_Volkov(request):
    status = handleClowns(request, "Alexander Volkov", 'https://vk.com/ssidex')
    return render(request, 'main/Alexander_Volkov.html',
                  {"Times": Data.Amound_of_times['Alexander Volkov'], "Status": status})

def Akhmed_Khakhaev(request):
    status = handleClowns(request, "Akhmed Khakhaev", 'https://vk.com/kha18')
    return render(request, 'main/Akhmed_Khakhaev.html',
                  {"Times": Data.Amound_of_times['Akhmed Khakhaev'], "Status": status})

def Alexey_Ischenko(request):
    status = handleClowns(request, "Alexey Ischenko", 'https://vk.com/id163201074')
    return render(request, 'main/Alexey_Ischenko.html',
                  {"Times": Data.Amound_of_times['Alexey Ischenko'], "Status": status})

def Kirill_Shvetsov(request):
    status = handleClowns(request, "Kirill Shvetsov", 'https://vk.com/kirillllllllllllll')
    return render(request, 'main/Kirill_Shvetsov.html',
                  {"Times": Data.Amound_of_times['Kirill Shvetsov'], "Status": status})

def Vova_Bukin(request):
    status = handleClowns(request, "Vova Bukin", 'https://vk.com/bukv0')
    return render(request, 'main/Vova_Bukin.html',
                  {"Times": Data.Amound_of_times['Vova Bukin'], "Status": status})

def Daniil_Dobrin(request):
    status = handleClowns(request, "Daniil Dobrin", 'https://vk.com/psychozzzzz')
    return render(request, 'main/Daniil_Dobrin.html',
                  {"Times": Data.Amound_of_times['Daniil Dobrin'], "Status": status})

def Danil_Kadochnikov(request):
    status = handleClowns(request, "Danil Kadochnikov", 'https://vk.com/dan_moken')
    return render(request, 'main/Danil_Kadochnikov.html',
                  {"Times": Data.Amound_of_times['Danil Kadochnikov'], "Status": status})

def Maks_Agafonov(request):
    status = handleClowns(request, "Maks Agafonov", 'https://vk.com/volzenal')
    return render(request, 'main/Maks_Agafonov.html',
                  {"Times": Data.Amound_of_times['Maks Agafonov'], "Status": status})

def Rodion_Fedotov(request):
    status = handleClowns(request, "Rodion Fedotov", 'https://vk.com/rodionfed')
    return render(request, 'main/Rodion_Fedotov.html',
                  {"Times": Data.Amound_of_times['Rodion Fedotov'], "Status": status})