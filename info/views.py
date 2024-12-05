from django.http import JsonResponse
from .forms import MessageForm

def contact_view(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Your message has been sent successfully."})
        else:
            return JsonResponse({"success": False, "errors": form.errors})
    return JsonResponse({"success": False, "errors": "Invalid request method."})
