from django.db import models
from django.contrib.auth.models import User
import datetime
from tagging.fields import TagField
from markdown import markdown

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    # Slug prepopulated from title in admin.py
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/categories/%s/" % self.slug

class Entry(models.Model):
    # Entry types
    LIVE_STATUS = 1
    DRAFT_STATUS = 2
    HIDDEN_STATUS = 3
    STATUS_CHOICES = (
        (LIVE_STATUS, 'Live'),
        (DRAFT_STATUS, 'Draft'),
        (HIDDEN_STATUS, 'Hidden'),
    )
    author = models.ForeignKey(User)
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    # Bit of redundancy with excerpt & excerpt_html and body & body_html, but seems to be cleanest way to seperate plain text and html
    excerpt = models.TextField(blank=True, help_text='Add an excerpt - a short summary of your post.')
    excerpt_html = models.TextField(editable=False, blank=True)
    body = models.TextField(help_text='Add the content of your post.')
    body_html = models.TextField(editable=False, blank=True)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    # Slug prepopulated from title in admin.py
    slug = models.SlugField(unique_for_date='pub_date', help_text="Suggested value automatically generated from title. Must be unique.")
    enable_comments = models.BooleanField(default=True)
    featured = models.BooleanField(default=False, help_text="Make this post featured. Will provide additional sorting.")
    status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
    categories = models.ManyToManyField(Category)
    tags = TagField()
   
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"

    def __unicode__(self):
        return self.title

    # Saves body into body_html and excerpt into excerpt_html using Markdown dependancy 
    def save(self):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save()

    def get_absolute_url(self):
        return "/weblog/%s/%s/" % (self.pub_date.strftime("%Y/%b/%d").lower(), self.slug)
