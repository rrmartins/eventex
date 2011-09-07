#-*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ungettext
from django.utils.translation import ugettext as _
import datetime

# Create your models here.

class Media(models.Model):
    MEDIAS = (
        ('SL', 'SlideShare'),
        ('YT', 'Youtube'),
    )
    talk = models.ForeignKey('Talk')
    type = models.CharField(max_length=3, choices=MEDIAS)
    title = models.CharField(u'Título', max_length=255)
    media_id = models.CharField(max_length=255)

    def __unicode__(self):
        return u'%s - %s' % (self.talk.title, self.title)


class PeriodManager(models.Manager):
    midday = datetime.time(12)

    def at_morning(self):
        qs = self.filter(start_time__lt=self.midday)
        qs = qs.order_by('start_time')
        return qs
   
    def at_afternoon(self):
        qs = self.filter(start_time__gte=self.midday)
        qs = qs.order_by('start_time')
        return qs

class Session(models.Model):
    #title = models.CharField(max_length=200)
    #description = models.TextField()
    #start_time = models.TimeField(blank=True)

    #objects = PeriodManager()
	
    class Meta:
        abstract = True

def __unicode__(self):
    return unicode(self.title)


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.TimeField(blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_('palestrante'))

    objects = PeriodManager()
    
    def __unicode__(self):
        return unicode(self.title)

class Course(Talk):
    slots = models.IntegerField()
    notes = models.TextField()

    objects = PeriodManager()

class CodingCourse(Course):
    class Meta:
        proxy = True
    def do_some_python_stuff(self):
        return "Let's hack! at %s" % self.title


class KindContactManager(models.Manager):
    def __init__(self, kind):
        super(KindContactManager, self).__init__()
        self.kind = kind
    
    def get_query_set(self):
        qs = super(KindContactManager, self).get_query_set()
        qs = qs.filter(kind=self.kind)
        return qs

class Speaker(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField()
    url  = models.URLField(verify_exists = False)
    description = models.TextField(blank = True)
    avatar = models.FileField(upload_to = 'palestrantes', blank = True, null = True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
        ('P', _('Telefone')),
        ('E', _('E-mail')),
        ('F', _('Fax')),
    )

    speaker = models.ForeignKey('Speaker', verbose_name = _('Palestrante'))
    kind = models.CharField(max_length = 1, choices = KINDS)
    value = models.CharField(max_length = 255)
    
    objects = models.Manager()
    phones  = KindContactManager('P') #PhoneContactManager()
    emails  = KindContactManager('E') #EmailContactManager()
    faxes   = KindContactManager('F') #FaxContactManager()

class PhoneContactManager(models.Manager):
    def get_query_set(self):
        qs = super(PhoneContactManager, self).get_query_set()
        qs = qs.filter(kind='P')
        return qs
    
class EmailContactManager(models.Manager):
    def get_query_set(self):
        qs = super(EmailContactManager, self).get_query_set()
        qs = qs.filter(kind='E')
        return qs
    
class FaxContactManager(models.Manager):
    def get_query_set(self):
        qs = super(FaxContactManager, self).get_query_set()
        qs = qs.filter(kind='F')
        return qs
