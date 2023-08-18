from django.db import models
from django_quill.fields import QuillField
from datetime import datetime
from bs4 import BeautifulSoup
import re


class Message(models.Model):
    body = QuillField(null=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{str(self.id).zfill(3)} - {self.created_at}"

    def as_p(self):
        soup = BeautifulSoup(str(self.body.html), "html.parser")
        img = soup.find("img")
        if img:
            return "<a href = \"" + img['src'] + "\">" + self.body.html + "</a>"
        print(str(self.body.html))

        return str(self.body.html)

    def get_time(self):
        return "<h6 class=\"time\">" + f"{self.created_at.strftime('%H:%M')} </h6>"

    def save(self, *args, **kwargs):
        self.created_at = datetime.now()
        super().save(*args, **kwargs)
