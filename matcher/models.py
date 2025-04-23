from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

SPORT_CHOICES = [
    ('Football', 'Football'),
    ('Cricket', 'Cricket'),
    ('Basketball', 'Basketball'),
    ('Tennis', 'Tennis'),
]

class Profile(models.Model):
    SKILL_LEVELS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Professional', 'Professional'),
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', default='default_profile.png')
    favorite_sports = models.JSONField(default=list, blank=True)
    skill_level = models.CharField(max_length=20, choices=SKILL_LEVELS, default='Intermediate')

    def __str__(self):
        return f"{self.user.username}'s Profile"

class SportSkill(models.Model):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='sport_skills')
    sport = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=20)  # This exists but your form is using 'proficiency'
    
    def __str__(self):
        return f"{self.profile.user.username} - {self.sport} ({self.skill_level})"  


class Game(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    game_name = models.CharField(max_length=100)
    sport = models.CharField(choices=SPORT_CHOICES, max_length=20)
    location = models.CharField(max_length=100)
    time = models.DateTimeField()
    players = models.ManyToManyField(User, related_name='joined_games', blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

