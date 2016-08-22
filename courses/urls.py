from django.conf.urls import url
from .import views


urlpatterns = [
    # View course list
    url(r'^mine/$',
        views.ManageCourseListView.as_view(),
        name='manage_course_list'),
    # Create course
    url(r'^create/$',
        views.CourseCreateView.as_view(),
        name='course_create'),
    # Edit course
    url(r'^(?P<pk>\d+)/edit/$',
        views.CourseUpdateView.as_view(),
        name='course_edit'),
    # Delete course
    url(r'^(?P<pk>\d+)/delete/$',
        views.CourseDeleteView.as_view(),
        name='course_delete'),
    # Update course modules
    url(r'^(?P<pk>\d+)/module/$',
        views.CourseModuleUpdateView.as_view(),
        name='course_module_update'),
    # Create course module content
    url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/create/$',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_create'),
    # Update module content
    url(r'^module/(?P<module_id>\d+)/content/(?P<model_name>\w+)/(?P<id>\d+)/$',
        views.ContentCreateUpdateView.as_view(),
        name='module_content_update'),
    # Delete module content
    url(r'^content/(?P<id>\d+)/delete/$',
        views.ContentDeleteView.as_view(),
        name='module_content_delete'),
    # Show module content
    url(r'^module/(?P<module_id>\d+)/$',
        views.ModuleContentListView.as_view(),
        name='module_content_list'),
    # Order modules
    url(r'^module/order/$',
        views.ModuleOrderView.as_view(),
        name='module_order'),
    # Order content
    url(r'^content/order/$',
        views.ContentOrderView.as_view(),
        name='content_order'),
    # Show course list by subject
    url(r'^subject/(?P<subject>[\w-]+)/$',
        views.CourseListView.as_view(),
        name='course_list_subject'),
    # Show course detail view
    url(r'^(?P<slug>[\w-]+)/$',
        views.CourseDetailView.as_view(),
        name='course_detail'), 
]
