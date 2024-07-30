from django import forms 
choices=[
    (1,"jpg"),(2,"png")
]
class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    type=forms.ChoiceField(choices=choices,label="Img format")
