from django.db import models

class Cats(models.Model):
    color=models.CharField(max_length=20)
    age=models.IntegerField()
    description=models.TextField(blank=False)
    owner=models.ForeignKey('Owners', on_delete=models.CASCADE)
    breed=models.ForeignKey('Breeds', on_delete=models.CASCADE)

    def __str__(self):
        return self.color
    
class Breeds(models.Model):
    breed=models.CharField(max_length=40)

    def __str__(self):
        return self.breed
    
class Owners(models.Model):
    owner=models.CharField(max_length=40)

    def __str__(self):
        return self.breed


