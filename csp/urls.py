from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from crowdsourcing import views
from crowdsourcing.viewsets.project import *
from crowdsourcing.viewsets.user import UserViewSet, UserProfileViewSet, UserPreferencesViewSet
from crowdsourcing.viewsets.requester import RequesterRankingViewSet, RequesterViewSet, QualificationViewSet
from crowdsourcing.viewsets.worker import *
from crowdsourcing.viewsets.task import TaskViewSet, CurrencyViewSet


from rest_framework.routers import SimpleRouter
router = SimpleRouter(trailing_slash=True)
router.register(r'api/profile',UserProfileViewSet)
router.register(r'api/user', UserViewSet)
router.register(r'api/preferences', UserPreferencesViewSet)
router.register(r'api/requester-ranking', RequesterRankingViewSet)
router.register(r'api/requester', RequesterViewSet)
router.register(r'api/project', ProjectViewSet)
router.register(r'api/category', CategoryViewSet)
router.register(r'api/module', ModuleViewSet,base_name = 'module')
#router.register(r'api/modulereview', ModuleReviewViewSet,base_name = 'modulereview')
#router.register(r'api/modulerating', ModuleRatingViewSet,base_name = 'modulerating')
router.register(r'api/project-requester', ProjectRequesterViewSet)
router.register(r'api/worker-skill', WorkerSkillViewSet)
router.register(r'api/worker', WorkerViewSet)
router.register(r'api/skill', SkillViewSet)
router.register(r'api/task', TaskViewSet)
router.register(r'api/task-worker', TaskWorkerViewSet)
router.register(r'api/worker-module-application', WorkerModuleApplicationViewSet)
router.register(r'api/qualification', QualificationViewSet)
router.register(r'api/currency', CurrencyViewSet)


urlpatterns = patterns('',
                       url(r'^api/v1/auth/forgot-password/$',views.ForgotPassword.as_view()),
                       url(r'^api/v1/auth/reset-password/(?P<reset_key>\w+)/(?P<enable>[0-1]*)/$',views.reset_password),
                       url(r'^api/v1/auth/registration-successful',views.registration_successful),
                       url(r'^api/v1/auth/logout/$', views.Logout.as_view()),
                       url(r'^/account-activation/(?P<activation_key>\w+)/$', views.activate_account),
                       url(r'^api/oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
                       url(r'^api/oauth2-ng/token', views.Oauth2TokenView.as_view()),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'', include(router.urls)),
                       url('^.*$', views.home, name='home'),
                       )

urlpatterns += staticfiles_urlpatterns()
