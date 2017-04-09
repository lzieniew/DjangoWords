from django.db import models

# Create your models here.

class Chapter(models.Model):
    name = models.CharField(max_length = 200, default=0)
    number = models.IntegerField(default = 0)

    def __str__(self):
        return 'Chapter: ' + str(self.number) + ', ' + self.name

class Word(models.Model):
    eng = models.CharField(max_length = 200)
    pol = models.CharField(max_length = 200)
    spelling = models.CharField(max_length=200, default = "")
    level = models.IntegerField(default = -2)
    chapter = models.ForeignKey(Chapter)
    string = models.CharField(max_length=200, default='')

    def word_to_string(self):
        self.string = self.__str__();

    def __init__(self):
        self.string = self.eng + ' - ' + self.pol + ' <' + self.spelling + '>'

    def __str__(self):
        return self.eng + ' - ' + self.pol + ' <' + self.spelling + '>'

    def expanded_str(self):
        return 'Eng: ' + self.eng + ', Pol: ' + self.pol + '<' + self.spelling + '> poziom: ' + str(self.level) + ', rozdzial' + self.chapter


