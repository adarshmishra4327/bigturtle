from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Property(models.Model):
    version = models.CharField(max_length=20)

    def __str__(self):
        return self.version


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(
        "Post", related_name="comments", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(default=None)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default=None)
    # comment_count = models.IntegerField(default = 0)
    # view_count = models.IntegerField(default = 0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    property_type = models.ManyToManyField(Property)
    featured = models.BooleanField()
    previous_post = models.ForeignKey(
        "self",
        related_name="previous",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    next_post = models.ForeignKey(
        "self",
        related_name="next",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
    
    @classmethod
    def test(self):
        print('test')

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("post-update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("post-delete", kwargs={"pk": self.pk})

    @property
    def get_comments(self):
        # return self.comments.all().order_by("-timestamp")
        print("test2")

    @property
    def comment_count(self):
        return Comment.objects.filter(post=self).count()

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()
