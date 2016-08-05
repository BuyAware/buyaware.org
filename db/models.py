from django.db import models

class Brand (models.Model):
    """
    Stores information on brands.
    
    *** Relations ***
    one :model:'db.Brand' may have many :model:'db.Product'
    """

    # --------------------
    # fields
    # --------------------

    name = models.CharField(max_length=50)



class Product (models.Model):
    """
    Stores information about a Product

    ** Relations **
    many :model:'db.Product' can have a same :model:'db.Brand'
    many :model:'db.Product' can have a same :model:'db.Rating'
    """
    
    # --------------------
    # fields
    # --------------------

    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='products')
    description = models.TextField()
    date_added = models.DateField()

    # --------------------
    # relations
    # --------------------
    
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.CASCADE,
    )

    # TODO: add calable function to handle on_delete (pass last active rating)
    # TODO: limit_choices_to={'is_coherent': True}
    rating = models.ForeignKey(
        'Rating',
        on_delete=models.SET_NULL,
    )

class Rating(models.Model):
    """
    Gathers many criterions under one rating.
    """

    name = models.CharField(max_length=30)
    date_added = models.DateField()
    is_active = models.BooleanField()
    
class Criterion(models.Model):
    """
    Element of a rating.
    """

    CRIT_TYPES = (
        ('YN', 'Yes/No'),
        ('XX', 'Linear'),
        ('XY', 'Compare'),
    )

    # --------------------
    # fields
    # --------------------

    question = models.TextField()
    date_added = models.DateField()
    crit_type = models.charField(max_length=2, choices=CRIT_TYPES)
    is_brand_specific = models.BooleanField()

    # --------------------
    # relations
    # --------------------
    
    # TODO: handle on_delete event with calback function
    category = models.ForeignKey(
        'Category',
        on_delete = models.SET_NULL
    )
    
