from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
import authentication.views as views


urlpatterns = [
    path('', include('authentication.urls', namespace='authentication')),
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls', namespace='forum')),
    path('scheduler/', include('scheduler.urls', namespace='scheduler')),
    path('assignments/', include('assignments.urls', namespace='assignments')),
    path('courses/', include('courses.urls', namespace='courses')),
    path('clubs/', include('clubs.urls', namespace='clubs')),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('account_settings/', views.accountSettings, name='account_settings'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='authentication/changePassword.html'),
         name='password_change'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_change.html'),
         name='password_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)