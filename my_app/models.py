from django.db import models

# Create your models here.

class Musician(models.Model):
    # id will be created by default if we don't create
	# id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    # if don't set null as true, by default it will be false
    last_name = models.CharField(max_length=50, null=True)
    # if blank parameter is true, it becomes required
    instrument = models.CharField(max_length=100, blank=False)
    def __str__(self):
        return self.first_name + " " + self.last_name

    # # renaming the bd table
    # class Meta:
    #     db_table = "album"

class Album(models.Model):
	# id = models.AutoField(primary_key=True)
    # here we can't delete any musician if the musician's album exist here
    # when we use foreignkey the 1st parmeter must be that model name
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    # we can use choices as options
    rating = (
    (1, "Worst"),
    (2, "Bad"),
    (3, "Not Bad"),
    (4, "Good"),
    (5, "Excellent!"),
    )

    # here choices are int type 1, 2, 3.... and Good, Bad .... are their values
    num_stars = models.IntegerField(choices=rating)
    # num_stars = models.IntegerField()

    def __str__(self):
        return self.name + ", Rating: " + str(self.num_stars)

    # class Meta:
    #     db_table = "musician"
