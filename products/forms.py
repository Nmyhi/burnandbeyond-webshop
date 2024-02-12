from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    # Define the model and the fields we want to include
    class Meta:
        model = Product
        # include all the fields with the special __all__ dundler
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'