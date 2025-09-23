from django.db import models
from src.apps.news.models import Article
from src.apps.common.models import TimestampModel
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(TimestampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="replies",
        null=True,
        blank=True,
    )
    content = models.TextField()
    is_approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.user} on {self.article}"


class Reaction(TimestampModel):
    REACTIONS = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('love', 'Love'),
        ('surprised', 'Surprised'),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_reactions"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="reactions"
    )
    reaction_type = models.CharField(max_length=20, choices=REACTIONS)

    class Meta:
        unique_together = ("user", "article", "reaction_type")

    def __str__(self):
        return f"{self.user} {self.reaction_type} {self.article}"


class CommentReaction(TimestampModel):
    REACTIONS = (
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('angry', 'Angry'),
        ('love', 'Love'),
        ('surprised', 'Surprised'),
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_reactions")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="reactions")
    reaction_type = models.CharField(max_length=20, choices=REACTIONS)

    class Meta:
        unique_together = ("user", "comment", "reaction_type")

    def __str__(self):
        return f"{self.user} {self.reaction_type} {self.comment}"
