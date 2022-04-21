import os.path

from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=200)
    uploadedFile = models.FileField(upload_to="Uploaded Files")
    dateTimeOfUpload = models.DateTimeField(auto_now=True)


    def get_file_name(self):
        return os.path.basename(self.uploadedFile.name)