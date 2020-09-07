from django.shortcuts import render , redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Chat , Feedback
from main_app.views import patient_ui, doctor_ui
from main_app.models import patient , doctor

# Create your views here.



def post_feedback(request):
    
  if request.method == "POST":

      feedback = request.POST.get('feedback', None)
      if feedback != '':  
        f = Feedback(sender=request.user, feedback=feedback)
        f.save()        
        print(feedback)   

        try:
           if (request.user.patient.is_patient == True) :
              return HttpResponse("Feedback successfully sent.")
        except:
          pass
        if (request.user.doctor.is_doctor == True) :
           return HttpResponse("Feedback successfully sent.")

      else :
        return HttpResponse("Feedback field is empty   .")



def get_feedback(request):
    
    if request.method == "GET":

      obj = Feedback.objects.all()
      
      return redirect(request, 'consultation/chat_body.html',{"obj":obj})





#-----------------------------chatting system ---------------------------------------------------


# def post(request):
#     if request.method == "POST":
#         msg = request.POST.get('msgbox', None)

#         consultation_id = request.session['consultation_id'] 
#         consultation_obj = consultation.objects.get(id=consultation_id)

#         c = Chat(consultation_id=consultation_obj,sender=request.user, message=msg)

#         #msg = c.user.username+": "+msg

#         if msg != '':            
#             c.save()
#             print("msg saved"+ msg )
#             return JsonResponse({ 'msg': msg })
#     else:
#         return HttpResponse('Request must be POST.')



# def messages(request):
#    if request.method == "GET":

#          consultation_id = request.session['consultation_id'] 

#          c = Chat.objects.filter(consultation_id=consultation_id)
#          return render(request, 'consultation/chat_body.html', {'chat': c})
