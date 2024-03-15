from django.shortcuts import render, redirect
from .forms import ItemForm
from .models import Item
from django.http import JsonResponse

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list') # Redirect to a list view or another page
    else:
        form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

def list_items(request):
    items = Item.objects.all() # Fetch all items
    return render(request, 'items.html', {'items': items})

# def serch_uom(request):
#     if request.is_ajax():
#         query = request.GET.get('term', '')
#         results = [{'id': uom.id, 'label': uom:name} for uom in uoms]
#         return JsonResponse({'error': 'Invalid request'}, status=400)
        