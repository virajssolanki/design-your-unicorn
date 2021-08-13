from PIL import Image, ImageDraw

image1 = Image.open('rk (2).png')
image2 = Image.open('img.png')
#resize, first image
image1 = image1.resize((173, 193))
#image1_size = image1.size
#image2_size = image2.size
#new_image = Image.new('RGB',image2.size, (250,250,250))
#new_image.paste(image1,(0,0))
image2.paste(image1,(322,45))
image2.save("merged_image.png","PNG")


def simple_upload(request, pk):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
    user_img = Uimg.objects.all()
    frame_img = Frame.objects.filter(id=pk).first()
    context = locals()
    return render(request, 'main/simple_upload.html', context)









from django.shortcuts import render
from .models import Frame, Uimg
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from PIL import Image
from .forms import UimgForm
from urllib.request import urlopen
import requests

def home(request):
    frames = Frame.objects.all()
    context = locals()
    return render(request, 'main/home.html', context)

def simple_upload(request, pk):
    if request.method == 'POST':
        form = UimgForm(request.POST, request.FILES)
        if form.is_valid():
            user_img = Uimg(img = request.FILES['img'])
            user_img.save()
            user_img_id = user_img.pk
    else:
        form = UimgForm()
        user_img_id = 1

    frame_img = Frame.objects.filter(id=pk).first()
    frame_img_id = frame_img.pk 
    context = locals()
    return render(request, 'main/simple_upload.html', context)

def merge(request, frame_img_id, user_img_id):
    frame = Image.open(requests.get('http://127.0.0.1:8000/media/frames_pic/frame.png', stream=True).raw)
    user_img = Image.open(requests.get('http://127.0.0.1:8000/media/user_img/Ram.jpeg', stream=True).raw)
    #user_img = Image.open(Uimg.objects.filter(pk=user_img_id).first().img.url)
    #resize, first image
    image1 = user_img.resize((173, 193))
    image2 = frame
    image1_size = image1.size
    image2_size = frame.size
    image2.paste(image1,(322,45))
    image2.save("merged_image.png","PNG")
    #fs = FileSystemStorage()
    #filename = fs.save('name', image2)
    #merged_file_url = fs.url(filename)
    context = locals()
    return render(request, 'main/merged.html', context)