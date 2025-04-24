from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RequestForm
from .models import Request
from django.utils import timezone
from .models import VoiceRequest

def homepage(request):
    return render(request, "homepage.html")

def classify_severity(description):
    description = description.lower()
    keywords_high = ['emergency', 'urgent', 'accident', 'medical', 'disaster', 'critical', 'blood', 'fire']
    keywords_medium = ['support', 'shelter', 'food', 'water', 'aid']
    keywords_low = ['job', 'training', 'education', 'learning']

    if any(word in description for word in keywords_high):
        return 'High'
    elif any(word in description for word in keywords_medium):
        return 'Medium'
    else:
        return 'Low'

def request_submission_view(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.severity = classify_severity(req.description)
            req.save()
            return render(request, 'thank_you.html', {'severity': req.severity})
    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})

def admin_dashboard_view(request):
    text_requests = Request.objects.all()
    voice_requests = VoiceRequest.objects.all()

    # Sort both by severity
    severity_order = {'High': 1, 'Medium': 2, 'Low': 3}
    text_requests = sorted(text_requests, key=lambda x: severity_order.get(x.severity, 4))
    voice_requests = sorted(voice_requests, key=lambda x: severity_order.get(x.severity, 4))

    return render(request, 'admin_dashboard.html', {
        'text_requests': text_requests,
        'voice_requests': voice_requests
    })

def assign_severity_voice(description):
    desc = description.lower()
    if any(word in desc for word in ['emergency', 'urgent', 'medical', 'disaster', 'injury', 'accident']):
        return 'High'
    elif any(word in desc for word in ['need', 'help', 'issue', 'assistance']):
        return 'Medium'
    else:
        return 'Low'

def voice_report_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        transcribed_text = request.POST['transcription']
        severity = assign_severity_voice(transcribed_text)

        VoiceRequest.objects.create(
            name=name,
            email=email,
            transcribed_text=transcribed_text,
            severity=severity,
            submitted_at=timezone.now()
        )
        return redirect('submit_request')  # or a thank you page

    return render(request, 'voice_report.html')


