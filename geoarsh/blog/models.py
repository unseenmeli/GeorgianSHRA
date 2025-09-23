from django.db import models
from django.utils import timezone

class Translation(models.Model):
    language = models.CharField(max_length=20)
    key = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        unique_together = ("language", "key")

class DynamicPost(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'News'),
        ('publications', 'Publications'),
        ('events', 'Events'),
        ('gapag_news', 'GAPAG News'),
        ('gapag_events', 'GAPAG Events'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    title_en = models.CharField(max_length=300)
    title_ge = models.CharField(max_length=300)
    content_en = models.TextField()
    content_ge = models.TextField()
    main_image = models.ImageField(upload_to='posts/main/', null=True)
    additional_image1 = models.ImageField(upload_to='posts/additional/', blank=True, null=True)
    additional_image2 = models.ImageField(upload_to='posts/additional/', blank=True, null=True)
    additional_image3 = models.ImageField(upload_to='posts/additional/', blank=True, null=True)
    image1_caption_en = models.CharField(max_length=200, blank=True)
    image1_caption_ge = models.CharField(max_length=200, blank=True)
    image2_caption_en = models.CharField(max_length=200, blank=True)
    image2_caption_ge = models.CharField(max_length=200, blank=True)
    image3_caption_en = models.CharField(max_length=200, blank=True)
    image3_caption_ge = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True, max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title_en
