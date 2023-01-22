from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime
from bs4 import BeautifulSoup
import re
class Message(models.Model):
    body = RichTextUploadingField(editable=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.body

    def src(self):
        soup = BeautifulSoup(str(self.body), "html.parser")
        img = soup.find("img")
        if img:
            return img['src']
        return ""
    def save(self, *args, **kwargs):
        m = re.search(r"style=\"+.{1,}\"", self.body)
        if m:
            self.body = self.body.replace(m.group(0), "")

        super().save(*args, **kwargs)