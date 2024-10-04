from rest_framework import serializers
from .models import Cats, Breeds


class CatsSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(queryset=Breeds.objects.all(), slug_field='breed')
    owner = serializers.SlugRelatedField(queryset=Breeds.objects.all(), slug_field='owner')
    owner=serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cats
        fields = ('color','age','description','owner','breed')


    # def create(self, validated_data):
    #     return Cats.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.breed=validated_data.get('breed',instance.breed)
    #     instance.color=validated_data.get('color',instance.color)
    #     instance.age=validated_data.get('age',instance.age)
    #     instance.description=validated_data.get('description',instance.description)
    #     instance.save()
    #     return instance    

    # def delete(self, instance):
    #     instance.delete()
    #     return None