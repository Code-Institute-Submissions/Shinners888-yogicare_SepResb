from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Item


def all_items(request):

    items = Item.objects.all()

    context = {
        'items': items,
    }

    return render(request, 'shop/items.html', context)


def item_detail(request, item_id):

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'shop/item_detail.html', context)
