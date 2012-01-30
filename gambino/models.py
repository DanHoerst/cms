from django.db import models
from django.contrib.auth.models import User
import datetime
from tagging.fields import TagField
from markdown import markdown
from django.conf import settings
from django.core.urlresolvers import reverse

class Category(models.Model):
    title = models.CharField(max_length=250, help_text='Maximum 250 characters.')
    # Slug prepopulated from title in admin.py
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    description = models.TextField()
    # Meta
    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categories"
    # Unicode
    def __unicode__(self):
        return self.title
    # Status get_absolute_url
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
    # Foreign Key
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
    # Meta
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = "Entries"
    # Unicode
    def __unicode__(self):
        return self.title
    # Saves body into body_html and excerpt into excerpt_html using Markdown dependancy 
    def save(self):
        self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        super(Entry, self).save()
    # get_absolute_url set up this way to use with urls.py
    def get_absolute_url(self):
        return ('gambino_entry_detail', (), { 'year': self.pub_date.strftime("%Y"),
                                              'month': self.pub_date.strftime("%b").lower(),
                                              'day': self.pub_date.strftime("%d"),
                                              'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
    title = models.CharField(max_length=250)
    # Description for plain text, description_html for html
    description = models.TextField(blank=True)
    description_html = models.TextField(blank=True)
    url = models.URLField(unique=True)
    # Foreign Key
    posted_by = models.ForeignKey(User)
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    # slug will prepopulate from title in admin.py
    slug = models.SlugField(unique_for_date='pub_date')
    tags = TagField()
    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to del.icio.us', default=True)
    via_name = models.CharField('Via', max_length=250, blank=True, help_text='The name of the person whose site you spotted the link on. Optional.')
    via_url = models.URLField('Via URL', blank=True, help_text='The URL of the site that you spotted the link on. Optional.')
    # Meta
    class Meta:
        ordering = ['-pub_date']
    # Unicode
    def __unicode__(self):
        return self.title
    # Custom Save - If anything was filled in description field, Markdown will save it in description_html. If post_elsewhere is True - link will be posted to external site
    def save(self):
        if self.description:
            self.description_html = markdown(self.description)
        if not self.id and self.post_elsewhere:
            # import pydelicious dependancy to send to del.icio.us
            import pydelicious
            # import smart_str to change unicode to str to send over web API
            from django.utils.encoding import smart_str
            pydelicious.add(settings.DELICIOUS_USER, settings.DELICIOUS_PASSWORD,
                            smart_str(self.url), smart_str(self.title),
                            smart_str(self.tags))
        super(Link, self).save()
    # get_absolute_url with permalink to enable reverse loopup in URLconf
    def get_absolute_url(self):
        return ('gambino_link_detail', (), { 'year': self.pub_date.strftime('%Y'),
                                             'month': self.pub_date.strftime('%b').lower(),
                                             'day': self.pub_date.strftime('%d'),
                                             'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
    
