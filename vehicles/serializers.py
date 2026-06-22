from rest_framework import serializers
from .models import Brand, Car, Comment

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):

    my_brand = serializers.ChoiceField(choices=Car.objects.all(), write_only=True)

    class Meta:
        model = Car
        fields = '__all__'
        depth=1

    def create(self, validated_data):
        brand = validated_data.pop('my_brand')
        car =Car.objects.create(**validated_data, brand=brand)
        return car

    def update(self, instance, validated_data):
        instance.brand = validated_data.pop('my_brand') if validated_data.pop('my_brand') else instance.brand
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class CommentSerializer(serializers.ModelSerializer):

    my_car = serializers.ChoiceField(choices=Car.objects.all(), write_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        car = validated_data.pop('my_car')
        author = self.context['request'].user
        comment = Comment.objects.create(**validated_data, car=car, author=author)
        return comment

    def update(self, instance, validated_data):
        car = validated_data.pop('my_car', None)
        if car is not None:
            instance.car = car

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance