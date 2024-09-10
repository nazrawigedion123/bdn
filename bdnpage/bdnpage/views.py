from django.shortcuts import render, redirect
from contactUs.forms import SubscriberForm, CommentForm
from contactUs.models import Subscriber
from testimonial.models import Testimonials
from project.models import Project
from  personnel.models import Personnel
from package.models import Package, Notification


def homepage(request):
    testimonials = Testimonials.objects.all()[:3]
    projects= Project.objects.all()
    personnel= Personnel.objects.all()[:3]
    package=Package.objects.all()[:3]
    notifications = Notification.objects.filter(user=request.user, is_read=False)


    if 'name' in request.POST and 'phone' in request.POST :  # Another unique identifier for the subscription form
        comment_form = CommentForm(request.POST)

        if  comment_form.is_valid():
            comment_form.save()
            return redirect('contactUs:success_comment')
    elif 'email' in request.POST:
        subscriber_form = SubscriberForm(request.POST)
        if Subscriber.objects.filter(email=request.POST['email']).exists():
            subscriber_form.add_error('email', 'This email is already subscribed.')
        elif subscriber_form.is_valid():

            subscriber_form.save()
            return redirect('contactUs:success_subscription')

    context={'form': CommentForm,
               'form2': SubscriberForm,
             'testimonials': testimonials,
             'projects':projects,
             'personnels':personnel,
             'packages':package,
             'notifications':len(notifications),
             }
    return render(request,"index.html",context)