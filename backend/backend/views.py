from django.shortcuts import render

def landing_page(request):
    """Renders the site's landing page."""
    return render(request, 'landing_page.html')