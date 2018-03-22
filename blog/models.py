from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def temperaturez(self):
        "This should pop up."
        return "It workedz"

    def setdatetopublishdate(self):
        self.date = self.published_date
        self.save()

    @property
    def temperature(self):
        "This should pop up."
        #return "It worked"
        try:
            #return Temperature.objects.values('temperature', flat=True).get(pk=1)
            return Temperature.objects.values_list('temperature', flat=True).get(post=self.pk)
        except:
            return None

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class Temperature(models.Model):
    post = models.ForeignKey('blog.Post', related_name='temperatures')
    date = models.DateField()
    temperature = models.IntegerField(default = 1)

    def updatepostid(self):
        self.date = Post.objects.values_list('date', flat=True).get(id=self.post_id)
        self.save()



class DailyLog(models.Model):
    #author = models.ForeignKey('auth.User')
    #title = models.CharField(max_length=200)
    #text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    caffeine = models.DecimalField(max_digits=20, decimal_places=2)
    alcohol = models.DecimalField(max_digits=20, decimal_places=2)
    picking = models.TextField()

    def __str__(self):
        return self.date.strftime('%m/%d/%Y')