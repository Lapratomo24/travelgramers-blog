from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Django model for creating posts
    """
    title = models.CharField(max_length=140, unique=True)
    slug = models.SlugField(max_length=140, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    attractions = models.TextField()
    duration = models.CharField(max_length=10, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name="blog_likes", blank=True)

    class Meta:
        """
        Class to order posts in descending order
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Method used to return the title
        """
        return self.title
    
    def number_of_likes(self):
        """
        Method used to count the number of likes on a post
        """
        return self.likes.count()


class Comments(models.Model):
    """
    Django model for creating comments
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.CharField(max_length=140)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Class to order posts in descending order
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
