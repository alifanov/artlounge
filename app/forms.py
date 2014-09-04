from django.forms import ModelForm, TextInput
from app.models import Order
class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['comment'].widget = TextInput()
    class Meta:
        model = Order