from django.db import models


class Topic(models.Model):
    TOPIC_CHOICES = [
        ('air', 'air'),
        ('water', 'water'),
        ('food', 'food'),
        ('housing', 'housing'),
        ('health', 'health'),
        ('education', 'education'),
        ('transportation', 'transportation'),
        ('sexuality', 'sexuality')
    ]

    name = models.CharField(max_length=25, choices=TOPIC_CHOICES)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    CATEGORY_CHOICES = [
        ('article_review', 'article_review'),
        ('book_review', 'book_review'),
        ('commentary', 'commentary')
    ]
    featured = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    category = models.CharField(
        max_length=25, choices=CATEGORY_CHOICES, default='article_review')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=200)
    topics = models.ManyToManyField(Topic)
    author = models.CharField(max_length=150)
    content = models.TextField()
    summary = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True,
                              upload_to='media/upload/posts')
    thumbnail = models.ImageField(
        blank=True, null=True, upload_to='media/upload/posts')

    class Meta:
        ordering = ['posted_date']

    def __str__(self):
        return self.title
