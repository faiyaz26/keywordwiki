from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField("Category title", max_length=50)
    description = RichTextField('Category description', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Keyword(models.Model):
    title = models.CharField("Keyword Title", max_length=50)
    description = RichTextField("Keyword description", blank=False, null=False)
    related_keywords = ArrayField(models.CharField(max_length=50, blank=False), blank=True, null=True)

    slug = models.SlugField(unique=True, blank=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    visitor_counter = models.IntegerField(default=0)

    categories = models.ManyToManyField(Category)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Keyword.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title


class Resource(models.Model):

    title = models.CharField("Resource Title", max_length=200, blank=False, null=False)
    summary = RichTextField("Resource summary", blank=True)
    link = models.CharField("Resource link", max_length=200)

    RESOURCE_TYPE_CHOICES = (
        ('book', "Book"),
        ('course', "Course"),
        ('blog', "Blog"),
        ('video_tutorial', "Video Tutorial"),
        ('text_tutorial', "Text based Tutorial")
    )

    resource_type = models.CharField(max_length=30, choices=RESOURCE_TYPE_CHOICES)
    
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


