# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class QuestionManager(models.Manager):
    @staticmethod
    def new():
        return Question.objects.all().order_by('-pk')

    @staticmethod
    def popular():
        return Question.objects.all().order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=255, verbose_name='заголовок вопроса')
    text = models.TextField(verbose_name='полный текст вопроса')
    added_at = models.DateField(blank=True, auto_now_add=True, verbose_name='дата добавления вопроса')
    rating = models.IntegerField(blank=True, default=0, verbose_name='рейтинг вопроса (число)')
    author = models.ForeignKey(User, related_name='question_author', verbose_name='автор вопроса')
    likes = models.ManyToManyField(User, blank=True, related_name='question_like_user', verbose_name='список пользователей, поставивших лайк')
    objects = QuestionManager()

    def get_url(self):
        return reverse('question_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    text = models.TextField(verbose_name='текст ответа')
    added_at = models.DateField(blank=True, auto_now_add=True, verbose_name='дата добавления ответа')
    question = models.ForeignKey(Question, verbose_name='вопрос, к которому относится ответ')
    author = models.ForeignKey(User, verbose_name='автор ответа')

    def __unicode__(self):
        return self.text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
