from django.shortcuts import render,redirect
from django.urls import reverse
import validators
from main.models import Url, View
import random
import string
from django.utils import timezone

def index(request):
    print()
    return render(request, 'main/index.html')


def shorten(request):
    if request.method == 'POST':


        url = request.POST.get('url')

        isValid = validators.url(url)
        if isValid:
            shortened_url_hash = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
            mapping = Url(original_url=url, hash=shortened_url_hash)
            mapping.save()
            return redirect(reverse('shortendetail',kwargs={'pk':mapping.id}))
        else:
            return render(request,'main/index.html',context={
                'error': 'Не правильный адрес, попробуйте другую'
            })
    else:
        return redirect('/')
    
def detail(request,pk):
    url = Url.objects.get(id=pk)
    shortened_url = request.build_absolute_uri(reverse('redirect', args=[url.hash]))
    return render(request,'main/index.html',context={'url': shortened_url})

def redirect_hash(request, url_hash):
    original_url = Url.objects.get(hash=url_hash)

    try:
        remote_addr = request.META.get('REMOTE_ADDR','NOT')
        http_agent = request.META.get('HTTP_USER_AGENT','NOT')
        View.objects.create(url=original_url,ip_adress=remote_addr,user_device=http_agent)
    except Exception as e:
        print(e)

    return redirect(original_url.original_url)
