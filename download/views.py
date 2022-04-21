import os

from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.shortcuts import render
from . import models


def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]

        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title=fileTitle,
            uploadedFile=uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "download/upload-file.html", context={
        "files": documents
    })

def downloadFile(request):
    file_path = os.path.abspath("media/Uploaded Files/")
    file_name = os.path.basename("media/Uploaded Files/2-2.요구사항정의서샘플.pdf")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name, 'rb'),
                            content_type='application/vnd.pdf')
    response['Content-Disposition'] = 'attachment; filename="ceil.pdf"'

    return response


