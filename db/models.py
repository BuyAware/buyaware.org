from django.db import models
# validators
from django.core.validators import MaxValueValidator, MinValueValidator

# ------------------
# Global Constants
# ------------------

DEFAULT_RATING_ID = 1


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

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):

        super(Product, self).save(*args, **kwargs)

        # get all criteria that need an answer in order to create the rating
        criteriaToAnswer = Criterion.objects.all()
        # iterate over all criterias and check if the answer exists in database
        for crit in criteriaToAnswer:
            # if it doesn't exist, create an answer
            if not CriterionAnswer.objects.filter(criterion=crit).filter(product=self):
                print "Criteria answer to: <%s> does not exist... creating new one" % crit.__str__()
                new_criterionAnswer = CriterionAnswer()
                new_criterionAnswer.criterion = crit
                new_criterionAnswer.product = self
                new_criterionAnswer.save()
            else:
                print "Criteria answer to: <%s> exists." % crit.__str__()


class GlobalProductRating(models.Model):
    '''
    Temporary rating. no calculations involved
    '''
    product = models.OneToOneField(
        'Product',
        on_delete=models.CASCADE,
    )

    overall = models.IntegerField(validators=[MaxValueValidator(
        100), MinValueValidator(0)], verbose_name='Overall rating')
    CE = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Climate/Energy')
    EC = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Ecology')
    WR = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Worker Rights')
    CM = models.IntegerField(validators=[MaxValueValidator(
        100), MinValueValidator(0)], verbose_name='Conflict Materials')
    TR = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Transparancy')
    PR = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], verbose_name='Performance')

    def __unicode_(self):
        return "rating of " + product.name

    class Meta:
        verbose_name = "Global Product Rating"
        verbose_name_plural = "Global Product Ratings"


# class Category(models.Model):
#     """
#     Category of a criterion

#     *** Relations ***
#     one :model:'db.Category' has many :model:'db.Criterion'.
#     """

#     name = models.CharField(max_length=20)

#     # --------------------
#     # methods
#     # --------------------

#     def __unicode__(self):
#         return self.name


class Criterion(models.Model):
    """
    Element of a rating.

    *** Relations ***
    many :model:'db.Rating' can have many :model:'db.Criterion'
    many :model:'db.Criterion' belong to a same :model:'db.Category'
    """

    CATEGORIES = (
        ('CE', 'Climate/Energy'),
        ('EC', 'Ecology'),
        ('WR', 'Worker Rights'),
        ('CM', 'Conflict Minerals'),
        ('TR', 'Transparancy'),
        ('PR', 'Performance'),
        )

    # --------------------
    # fields
    # --------------------

    question = models.TextField()
    date_added = models.DateField()
    weight = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    category = models.CharField(
        max_length = 2, 
        choices = CATEGORIES, 
    )

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return self.question


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

    answer = models.IntegerField(default=0,
                                    validators=[
                                        MaxValueValidator(100),
                                        MinValueValidator(0)
                                    ],
                                    null=True,
                                    )
    # source of information
    source = models.CharField(max_length=256, null=True, blank=True)
    
    comment = models.TextField(null=True, blank=True)

    # --------------------
    # relations
    # --------------------

    criterion = models.ForeignKey('Criterion', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    # --------------------
    # methods
    # --------------------

    def __unicode__(self):
        return "Criterion answer " + str(self.criterion.id) + " to " + str(self.product)
