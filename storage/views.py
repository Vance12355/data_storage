from django.http import JsonResponse, HttpResponse, FileResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import os
from .models import UploadedFile

@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    """Обработчик для регистрации"""
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not username or not password:
        return JsonResponse({"error": "Username and password are required"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Username already exists"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return JsonResponse({"message": "User registered successfully"}, status=201)

@csrf_exempt
@require_http_methods(["POST"])
def login_view(request):
    """Обработчик для авторизации"""
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"message": "Login successful"}, status=200)
    else:
        return JsonResponse({"error": "Invalid credentials"}, status=400)

@login_required
@csrf_exempt
@require_http_methods(["POST"])
def upload_file(request):
    """Обработчик для загрузки файлов"""
    if 'file' not in request.FILES:
        return JsonResponse({"error": "No file part"}, status=400)
    file = request.FILES['file']
    if file.size > settings.MAX_UPLOAD_SIZE:
        return JsonResponse({"error": "File size exceeds the allowed limit"}, status=400)
    uploaded_file = UploadedFile.objects.create(file=file)
    return JsonResponse({"message": "File uploaded successfully", "filename": uploaded_file.file.name}, status=201)

@login_required
@csrf_exempt
@require_http_methods(["GET"])
def download_file(request, filename):
    """Обработчик для скачивания файлов"""
    file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
    if default_storage.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        return response
    else:
        return JsonResponse({"error": "File not found"}, status=404)


@login_required
@csrf_exempt
@require_http_methods(["GET"])
def list_files(request):
    upload_dir = os.path.join(settings.MEDIA_ROOT, 'uploads')
    try:
        files = os.listdir(upload_dir)
    except FileNotFoundError:
        return JsonResponse({'error': 'Uploads directory not found'}, status=404)
    return JsonResponse({'files': files})
