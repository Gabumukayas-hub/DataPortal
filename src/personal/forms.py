from django import forms
class farmerforms(forms.Form):
	name=forms.CharField()
	age=forms.IntegerField()
	city=forms.CharField()
	livestock=forms.CharField()
	crop=forms.CharField()
	profit_or_loss=forms.IntegerField()