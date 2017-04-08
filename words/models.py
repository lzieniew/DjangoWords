from django.db import models

# Create your models here.

class Word(models.Model):
    eng = models.CharField(max_length = 200)
    pol = models.CharField(max_length = 200)
    spelling = models.CharField(max_length=200, default = "")
    level = models.IntegerField(default = -2)
    chapter = models.IntegerField(default = 1)

    def __str__(self):
        return 'Eng: ' + self.eng + ', Pol: ' + self.pol + '<' + self.spelling + '>'

    def expanded_str(self):
        return 'Eng: ' + self.eng + ', Pol: ' + self.pol + '<' + self.spelling + '> poziom: ' + self.level + ', rozdzial' + self.chapter