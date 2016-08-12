from django.db import models
# validators
from django.core.validators import MaxValueValidator, MinValueValidator

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

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.name


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
        null=True,
    )

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.name


class Rating(models.Model):
    """
    Gathers many criterions under one rating.

    *** Relations ***
    many :model:'db.Rating' can have many :model:'db.Criterion'
    """

    name = models.CharField(max_length=30)
    date_added = models.DateField()
    is_active = models.BooleanField()

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.name    


class Category(models.Model):
    """
    Category of a criterion
    
    *** Relations ***
    one :model:'db.Category' has many :model:'db.Criterion'.
    """

    name = models.CharField(max_length=20)

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.name


class Criterion(models.Model):
    """
    Element of a rating.

    *** Relations ***
    many :model:'db.Rating' can have many :model:'db.Criterion'
    many :model:'db.Criterion' belong to a same :model:'db.Category'
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
    crit_type = models.CharField(max_length=2, choices=CRIT_TYPES)
    is_brand_specific = models.BooleanField()
    best_grade = models.IntegerField(default = 0, help_text = "Only for xx and xy criterion types.")
    worst_grade = models.IntegerField(default = 0, help_text = "Only for xx and xy criterion types.")

    # --------------------
    # relations
    # --------------------
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
    )

    # TODO: handle on_delete event with calback function
    rating = models.ManyToManyField(
        'Rating',
        through='CriterionInRating',
        through_fields=('criterion', 'rating'),
    )

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.question

class CriterionInRating(models.Model):
    '''
    Many to many intermediate model, adds a weighting to the criterion in 
    the specfic rating.
    '''

    criterion = models.ForeignKey('Criterion', 
                                  on_delete=models.CASCADE,
                                  default = None,
                              )
    rating = models.ForeignKey('Rating', 
                               on_delete=models.CASCADE,
                               default = None,
                           )
    weight = models.IntegerField(
        default = 0, 
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return "criterion " + str(self.criterion.id) + " in " + self.rating.name

    
    # --------------------
    # Meta
    # --------------------

    class Meta:
        unique_together = ('criterion', 'rating')

class CriterionAnswer(models.Model):
    '''
    Answer to a criterion for a specific product.

    *** Relations ***
    A :model:'db.Product' has many :model:'db.CriterionAnswer'
    A :model:'db.Criterion' has many :model:'db.CriterionAnswer'
    '''
    
    # --------------------
    # fields
    # --------------------

    answer_bool = models.BooleanField(default=False,
                                  )
    answer_xx   = models.IntegerField(default= 0, 
                                      validators=[
                                          MaxValueValidator(100),
                                          MinValueValidator(0)
                                      ],
                                      null = True,
                                  )
    answer_xy   = models.IntegerField(default=0, 
                                      validators=[
                                          MaxValueValidator(100),
                                          MinValueValidator(0)
                                      ],
                                      null = True,
                                  )

    # --------------------
    # relations
    # --------------------

    criterion = models.ForeignKey('Criterion', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return "Answer to criterion " + str(self.criterion.id) + " for " + self.product.name
