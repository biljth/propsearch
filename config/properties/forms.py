from django import forms
from .models import InternalProperty


class PropertyForm(forms.ModelForm):

    class Meta:
        model = InternalProperty

        fields = [
            'agent_name',
            'agent_phone',
            'agent_whatsapp',

            'title',
            'description',
            'price',
            'location',
            'wilayah',
            'full_address',
            'google_drive_link',

            'property_type',
            'property_category',

            'area_surface',
            'area_building',
            'bedrooms',
            'bathrooms',
        ]