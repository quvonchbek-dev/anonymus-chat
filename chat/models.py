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

    def as_p(self):
        soup = BeautifulSoup(str(self.body), "html.parser")
        img = soup.find("img")
        if img:
            return "<a href = \"" + img['src'] + "\">" + self.body +"</a>"
        return self.body
    def get_time(self):
        return "<h6 class=\"time\">" + f"{self.created_at.strftime('%H:%M')} </h6>"
    
    def save(self, *args, **kwargs):
        m = re.search(r"style=\"+.{1,}\"", self.body)
        if m:
            self.body = self.body.replace(m.group(0), "")
        self.created_at = datetime.now()
        super().save(*args, **kwargs)