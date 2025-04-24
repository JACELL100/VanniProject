from django.urls import path
from .views import request_submission_view, admin_dashboard_view, voice_report_view
from .views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('submit-request/', request_submission_view, name='submit_request'),
    path('admin-dashboard/', admin_dashboard_view, name='admin_dashboard'),
    path('voice-report/', voice_report_view, name='voice_report'),
    
]
