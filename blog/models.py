from django.db import models
from django.urls import reverse
# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="blogs/", blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post-detail", kwargs={"id": self.id})


# import pathlib
# import uuid
# def image_file_upload_handler(instance, filepath):
#     instance_id = instance.id
#     if not instance.id:
#         instance_id = "0"
#     filepath = pathlib.Path(filepath).resolve()
#     fname = str(uuid.uuid1())
#     ext = filepath.suffix
#     return f"blog/{instance_id}/{fname}/{filepath.name}"
