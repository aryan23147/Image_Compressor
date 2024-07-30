
from django.shortcuts import render
from django.core.files.storage import default_storage
from .forms.imgform import ImageUploadForm
from .image_compression import compress_image

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            type=form.cleaned_data['type']
            path = default_storage.save('uploads/' + image.name, image)
            compressed_image_path = compress_image(default_storage.path(path),type)
            return render(request, 'compressor/compressed_image.html', {'compressed_image_path': default_storage.url(compressed_image_path)})
    else:
        form = ImageUploadForm()
    return render(request, 'compressor/upload.html', {'form': form})
