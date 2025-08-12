from django.db import models

class Question(models.Model):
    LEVEL_CHOICES = [(i, f"R${i*1000}") for i in range(1, 16)]
    
    text = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[
        ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')
    ])
    level = models.IntegerField(choices=LEVEL_CHOICES)
    wrong_options = models.CharField(max_length=3, default='')  # Ex: "A,C" (opções erradas)

    def __str__(self):
        return f"Pergunta Nível {self.level}: {self.text}"