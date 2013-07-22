from django.conf.urls import url, patterns
from django.contrib.sites.models import Site
from django.views.generic import DetailView, ListView

from galleries.models import Gallery

current_site = Site.objects.get_current()

urlpatterns = patterns(
    '',
    url(
        name="gallery_list",
        regex='^$',
        view=ListView.as_view(
            queryset=Gallery.objects.filter(published=True),
            template_name="galleries/gallery_list.html"
        )
    ),
    url(
        name="gallery_detail",
        regex=r'^(?P<slug>[-\w]+)/$',
        view=DetailView.as_view(
            queryset=Gallery.objects.all(),
            slug_field='slug',
            template_name="galleries/gallery_detail.html"
        )
    ),
)