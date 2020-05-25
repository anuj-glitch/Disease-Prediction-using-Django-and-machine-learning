from django.urls import path , re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path('admin_ui', views.admin_ui , name='admin_ui'),

    path('patient_ui', views.patient_ui , name='patient_ui'),
    path('checkdisease', views.checkdisease, name="checkdisease"),
    path('pviewprofile/<str:patientusername>', views.pviewprofile , name='pviewprofile'),
    path('pconsultation_history', views.pconsultation_history , name='pconsultation_history'),
    path('consult_a_doctor', views.consult_a_doctor , name='consult_a_doctor'),
    path('make_consultation/<str:doctorusername>', views.make_consultation , name='make_consultation'),
    path('rate_review/<int:consultation_id>', views.rate_review , name='rate_review'),


    path('dconsultation_history', views.dconsultation_history , name='dconsultation_history'),
    path('dviewprofile/<str:doctorusername>', views.dviewprofile , name='dviewprofile'),
    path('doctor_ui', views.doctor_ui , name='doctor_ui'),
    
    
    
    path('consultationview/<int:consultation_id>', views.consultationview , name='consultationview'),
    path('close_consultation/<int:consultation_id>', views.close_consultation , name='close_consultation'),

    
    path('post', views.post, name='post'),
    path('chat_messages', views.chat_messages, name='chat_messages'),
    


]  
