from django.shortcuts import render, redirect
from django.apps import apps
from django.conf import settings
from django.contrib import messages
from .utils import get_custom_models
from uploads.models import Upload
from .tasks import import_data_task


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
        # handle the imporrt task
        import_data_task.delay(file_path, model_name)

        #show message to use
        messages.success(request, "Your data is being imported, you will be notified once it's done")
        return redirect('import_data')
    else:
        pass
    return render(request, 'dataentry/import.data.html', context)