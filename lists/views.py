from django.shortcuts import render, redirect
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        item = Item()
        item.text = new_item_text
        item.save()
        return redirect('/lists/the-only-list')
    # return render(request,'home.html',{'new_item_text': new_item_text})
    # items = Item.objects.all()
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
