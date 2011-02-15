from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from django.forms import ModelForm

class Endereco(models.Model):
    codigo = models.CharField(max_length = 16, unique = True, validators = [RegexValidator(r'[a-zA-Z0-9]+')])
    destino = models.URLField(max_length = 512, verify_exists = False, unique = True)
    
    def __unicode__(self):
        return self.codigo

class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco