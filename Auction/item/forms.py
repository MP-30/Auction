from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import *
from datetime import datetime

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_code', 'item_name', 'item_category', 'standard_buying_rate','date', 'standard_selling_rate', 'uom', 'item_subcategory', 'hsn_code', 'description', 'warehouse']
        
    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        # Generate the item code
        now = datetime.now()
        year = now.strftime('%y')
        month = now.strftime('%m')
        day = now.strftime('%d')
        # Generate a unique sequence number
        # This is a simple example; you might need a more robust method for generating unique sequences
        sequence_number = 1 # Start with 1 for simplicity
        self.fields['item_code'].initial = f'ITM-{year}-{month}-{day}-{sequence_number:04d}'
        # Populate the uom field with available UOMs
        self.fields['uom'].queryset = UOM.objects.all()
        
class UomForm(forms.ModelForm):
    class Meta:
        model = UOM 
        fields = ['name']