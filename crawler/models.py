import requests
from django.db.models import CharField, Model, IntegerField, ImageField, FileField, ForeignKey,BooleanField
from lxml import html
from requests.exceptions import ConnectionError
from datetime import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from django.db import transaction
from django.core import serializers
import json
user_agent = {"User-agent": "Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; Build/KLP) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30"}

# Create your models here.

class Vendor(Model):
    """TipoItem"""
    nome = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

    nome = CharField(max_length=50, unique=True)
    url = CharField(max_length=5000, default='#')
    texto_completo = CharField(max_length = 4000, null=True, blank=True)
    
class Link(Model):
    """docstring for Link"""
    url = CharField(max_length= 5000)
    content = CharField(max_length = 10000)
    vendor = ForeignKey(Vendor)

class  KnowledgePanel(object):
    """docstring for  KnowledgePanel"""
    content = CharField(max_length=10000)
    