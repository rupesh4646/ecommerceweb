from django.db import models


class Logo( models.Model):
        name = models.CharField(max_length=300, unique=True)
        image = models.ImageField(upload_to='media')
        description = models.TextField(blank=True)


        def __str__(self):
            return self.name


class Featuredcategory( models.Model):
    name = models.CharField(max_length=300,unique=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Slider( models.Model):
    name = models.CharField(max_length=300,unique=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500,blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name



class Awesome( models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)

    def __str__(self):
            return self.name

class Weeklysale( models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)


    def __str__(self):
        return self.name

class Bestseller(models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Subscription(models.Model):
    name = models.CharField(max_length=300, unique=True)
    email= models.EmailField(max_length=50,unique=True)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    url = models.URLField(max_length=500, blank=True)


    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')
    comment = models.TextField()
    post = models.CharField(max_length=300)
    star = models.IntegerField()

    def __str__(self):
        return self.name




class Siteinformation( models.Model):
    name = models.CharField(max_length=300,unique=True)
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=20)
    twitter  = models.URLField(max_length=500,blank=True)
    facebook = models.URLField(max_length=500, blank=True)
    instagram = models.URLField(max_length=500, blank=True)
    youtube = models.URLField(max_length=500, blank=True)
    url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Clientlogo(models.Model):
    name = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.name

