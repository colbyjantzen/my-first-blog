from blog.models import Temperature


for i in Temperature.objects.all():
    i.updatepostid()

# def setdatetopublishdate(self):
#     self.date = self.published_date
#     self.save()
#
#
# for i in Post.objects.all():
#     i.setdatetopublishdate()