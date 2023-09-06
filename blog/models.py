from django.conf import settings
from django.db import models
from django.utils import timezone
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel


class HomePage(Page):
    pass



class BlogIndexPage(Page):
    # add the get_context method:
    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        # blogpages = self.get_children().live().order_by('-first_published_at')
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        context['posts'] =posts
        return context


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title