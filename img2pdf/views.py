from django.shortcuts import render
from .forms import UploadFileForm
from django.http import HttpResponseRedirect,HttpResponse
from django.views.generic.edit import FormView
from django.core.files.uploadedfile import InMemoryUploadedFile
from .forms import UploadFileForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io
import imghdr
from reportlab.lib.utils import ImageReader
from PIL import Image as IMG
def generate_pdf(image_files, output_path):
    
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    for image_file in image_files:
        image_stream = io.BytesIO(image_file.read())
        image_reader = ImageReader(image_stream)
        img_width, img_height = image_reader.getSize()

        aspect = img_width / float(img_height)
        if aspect > 1:
            new_width = width
            new_height = width / aspect
        else:
            new_height = height
            new_width = height * aspect

        c.drawImage(image_reader, 0, height - new_height, width=new_width, height=new_height)
        c.showPage()

    c.save()
def chk_image(imageList) -> bool:
    valid_extensions = ['jpg', 'jpeg', 'png', 'gif', 'bmp']
    for image in imageList:
        if not image.name.split('.')[-1].lower() in valid_extensions:
            return False
    return True

def upload_file(request):
    if request.method == "POST":
        imageList = request.FILES.getlist('images')
        msg = ""
        if (chk_image(imageList) == False):
            msg = "Select only images"
        if len(imageList) == 0:
            msg = "Select at least 1 image"
        if msg != "":
            context = {
                "message":msg,
            }
            return render(request,"index.html",context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="generated.pdf"'
        generate_pdf(imageList, response)
        return response
    return render(request, "index.html")