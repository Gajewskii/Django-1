from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    age = models.CharField(max_length=40)
    place = models.CharField(max_length=40)
    userphoto = models.ImageField(upload_to='images')
    photo = models.ImageField(upload_to='images')
    text = models.CharField(max_length=100, default='')
    create = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name + " " + self.surname 

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment on {self.created_at}'
    


class Like(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.comment.text}'