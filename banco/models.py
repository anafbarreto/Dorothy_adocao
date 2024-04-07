from django.db import models
from cadastro_animal.models import Animal

class Adotante(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50) 
    cpf = models.CharField(max_length=11, unique=True)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    endereco = models.CharField(max_length=50)
    termo_responsabilidade = models.BooleanField()
    espaco = models.BooleanField()
    tempo = models.BooleanField()
    ciente_custos = models.BooleanField()
    disposicao_fisica_emocional = models.BooleanField()
    
    def validate_termo_responsabilidade(self):
        if not (self.espaco and self.tempo and self.ciente_custos and self.disposicao_fisica_emocional):
            self.termo_responsabilidade = False
        else:
            self.termo_responsabilidade = True
            
    def __str__(self): 
        return f'{self.nome}, {self.email}, {self.telefone}, {self.termo_responsabilidade}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Adotante' # Nome do formulario'
        verbose_name_plural = 'Adotantes'
        ordering = ['nome'] 
        
class adocao(models.Model):
    id = models.AutoField(primary_key=True)
    animais = models.ForeignKey(Animal, on_delete=models.PROTECT)
    adotante = models.ForeignKey(Adotante, on_delete=models.PROTECT)
    termo_aceito = models.BooleanField() 
    data = models.DateTimeField(auto_now_add=True)
    
    #Verifica se o termo de responsabilidade foi aceito
    def save(self, *args, **kwargs):
        if self.adotante:  # Verifica se há um adotante associado
            self.termo_aceito = self.adotante.termo_responsabilidade  # Atribui o valor de termo_responsabilidade a termo_aceito
        super().save(*args, **kwargs) # Termo aceito vai receber o valor de termo_responsabilidade (True ou False)
    
    def __str__(self):
        return f'{self.animais}, {self.adotante}, {self.termo_aceito}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Adocao' # Nome do formulario'
        verbose_name_plural = 'Adocoes'
        ordering = ['-data'] 

class funcionarios(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50) 
    email = models.EmailField(max_length=50, unique=True)
    cargo_choices = [
        ('voluntário', 'Voluntário'),
        ('cuidador', 'Cuidador'),
        ('admin', 'Admin'),
    ]
    cargo = models.CharField(max_length=15, choices=cargo_choices)
    usuario = models.CharField(max_length=20, unique=True)
    senha = models.CharField(max_length=10)
    
    def __str__(self): 
        return f'{self.nome}, {self.cargo}'
    
    class Meta: # Alterando o nome das bases dentro do admin
        verbose_name = 'Funcionário' # Nome do formulario'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome']
        
""" Toda vez que mexer no banco, precisa fazer o comando:
terminal: python manage.py makemigrations
terminal: python manage.py migrate
Para criar essas informações na tabela"""
