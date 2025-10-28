from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register,name='register'),
    path('submit_complaint',views.submit_complaint,name='submit_complaint'),
    path('allcomplaints',views.allcomplaints,name='allcomplaints'),
    path('filtercity',views.filtercity,name='filtercity'),
    path('mycomplaints',views.mycomplaints,name='mycomplaints'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('complaintdetails/<int:id>',views.complaintdetails,name='complaintdetails'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)