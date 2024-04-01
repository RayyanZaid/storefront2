from rest_framework import serializers


# Completely separate from the product class

# Using this, we can go from (Product Object) --> Python Dictionary
class ProductSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)