from django import forms
from berita.models import Artikel

class ArtikelForm(forms.ModelForm):
    
    class Meta:
        model = Artikel
        fields = ('judul', 'isi', 'kategori', 'thumbnail')
        widgets = {
            
            "judul" : forms.TextInput(
                attrs={
                    'class': 'form-control',
                }),
            "isi" : forms.Textarea(
                attrs={
                    'class': 'form-control',
                }),
            "Kategori" : forms.Select(
                attrs={
                    'class': 'form-control',
                }),
        }
