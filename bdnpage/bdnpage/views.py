from django.db.models import Subquery, OuterRef, IntegerField
from django.db.models.functions import RowNumber
from django.shortcuts import render, redirect
from contactUs.forms import SubscriberForm, CommentForm
from contactUs.models import Subscriber
from django.views.generic import TemplateView
from testimonial.models import Testimonials
from project.models import Project
from  personnel.models import Personnel
from package.models import Package, Notification, Category,Feature



def homepage(request):
    testimonials = Testimonials.objects.all()[:3]

    personnel= Personnel.objects.all().reverse()
    packages = Package.objects.prefetch_related('features__category')
    categories = Category.objects.prefetch_related("feature_set").all()
    # Prepare package data with categorized features
    package_data = []
    for package in packages:
        categorized_features = {}

        for feature in package.features.all():
            category_name = feature.category.name if feature.category else "Other"
            if category_name not in categorized_features:
                categorized_features[category_name] = []
            categorized_features[category_name].append(feature)

        package_data.append({
            'package': package,
            'categorized_features': categorized_features
        })

    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
    else:
        notifications =Notification.objects.none()


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
    project_categories = Category.objects.prefetch_related("project_set").all()
    # Dictionary to store categories with their respective projects (max 3 each)
    category_projects = {}

    for category in project_categories:
        projects = category.project_set.all()[:3]  # Fetch only 3 projects per category
        category_projects[category] = projects



    uncategorized_projects = Project.objects.filter(category__isnull=True)
    projects = Project.objects.all()





    context={'form': CommentForm,
               'form2': SubscriberForm,
             'testimonials': testimonials,
             'projects':projects,
             'personnels':personnel,
             'packages':package_data,
             'notifications':len(notifications),
             'categories':categories,
             'project_categories':category_projects,
             'uncategorized_projects':uncategorized_projects,

             }
    return render(request,"index.html",context)

def about(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(user=request.user, is_read=False)
    else:
        notifications = Notification.objects.none()
    context={'form': CommentForm,
               'form2': SubscriberForm,

             'notifications':len(notifications),
             }
    return render(request,"about.html",context)

