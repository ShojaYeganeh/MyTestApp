from django.shortcuts import render
from . import models
# Create your views here.
def articles_list(request):
    objectarticle= models.Articles.objects.all().order_by('date')

    argu={'namayeshobjectarticle':objectarticle}
    return render(request,'articles/articleslist.html',argu)
