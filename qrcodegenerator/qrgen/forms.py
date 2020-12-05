from django import forms
from .models import QrcodeData

class QrcodeDataForm(forms.ModelForm):
	class Meta:
		model=QrcodeData
		fields=['labelname','description']