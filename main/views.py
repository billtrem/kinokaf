from django.shortcuts import render
from cloudinary.uploader import upload
from cloudinary.exceptions import Error

def home(request):
    image_url = None

    if request.method == "POST" and request.FILES.get("image"):
        file = request.FILES["image"]
        try:
            result = upload(file)
            image_url = result.get("secure_url")
        except Error as e:
            print("Cloudinary error:", e)

    return render(request, "main/index.html", {"image_url": image_url})
