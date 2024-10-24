from django.shortcuts import render, redirect
from django.apps import apps
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages
from .utils import get_custom_models
from uploads.models import Upload


def import_data(request):
    models = get_custom_models()
    context={'custom_models': models}
    if request.POST:
        file_path = request.FILES.get('uploaded_file')
        model_name = request.POST.get('model_name')
        # store file in Upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        # get relative file path
        file_path = str(settings.BASE_DIR) + '' + str(upload.file.url)
        try:
            call_command('importdata', file_path, model_name)
            messages.success(request, 'Data imported successfully!')
        except Exception as e:
            messages.error(request, e)
        return redirect('import_data')
    else:
        pass
    return render(request, 'dataentry/import.data.html', context)