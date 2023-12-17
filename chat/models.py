from django.db import models

from users.models import User 

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='to_receiver', on_delete=models.CASCADE)
    message_text = models.TextField('Текст сообщения')
    message_image = models.ImageField('Изображение', blank=True, upload_to='images/messages/')
    message_time = models.DateTimeField('Время отправления')
    is_readed = models.BooleanField('Прочитано', default=False)
    sender_visibility = models.BooleanField('Отображение у отправителя', default=True)
    receiver_visibility = models.BooleanField('Отображение у получателя', default=True)

    def __str__(self):
    	return f'{self.sender} -> {self.receiver}: {self.message_text}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
