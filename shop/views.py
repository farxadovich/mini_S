from django.shortcuts import render
from .models import Mahsulot, Toifa
from django.core.paginator import Paginator
from django.views.generic import DetailView



def index(request):
    mahsulotlar = Mahsulot.objects.all()
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'kategoriyalar': toifalar, 'mahsulotlar': mahsulotlar})
    

def category(request, category_id):
    page = request.GET.get('page')
    toifa = Toifa.objects.get(pk=category_id)
    all_mahsulotlar = Mahsulot.objects.filter(toifasi=toifa).order_by(id)
    paginator = Paginator(all_mahsulotlar, 2)
    mahsulotlar = paginator.get_page(page)
    toifalar = Toifa.objects.all()
    return render(request, 'shop/index.html', {'kategoriyalar': toifalar, 'mahsulotlar': mahsulotlar})


class MahsulotView(DetailView):
    model = Mahsulot
    template_name = 'shop/mahsulot.html'