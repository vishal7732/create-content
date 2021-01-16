from django.contrib.sitemaps import Sitemap

from post.models import Post

class BlogSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.pub_date