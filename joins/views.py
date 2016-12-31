from django.shortcuts import render

from .forms import EmailForm, JoinForm
from .models import Join
# Create your views here.


def get_ip(request):
	# print request.META.get("REMOTE_ADDR")
	# print request.META.get("HTTP_X_FORWARDED_F")
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_F")
		if x_forward:
			ip = x_forward
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = "0.0.0.0"
	return ip




def home(request):	
	# print request.POST["email"], request.POST["email_2"]

	# this is using regular django form
	# form = EmailForm(request.POST or None)
	# if form.is_valid():
	# 	email = form.cleaned_data['email']
	# 	new_join, created = Join.objects.get_or_create(email=email)
	# 	print new_join, created
	# 	print new_join.timestamp
	# 	if created:
	# 		print "the obj was created" 


	# this is using model form
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
			new_join_old.ip_address = get_ip(request)
			new_join_old.save()
		#redirect here
		# new_join.ip_address = get_ip(request)
		# new_join.save()

	context = {"form":form}
	template = 'home.html'
	return render(request, template, context) 


