from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class TimeStampModel(models.Model):
    created_by = models.ForeignKey(User,
                                   on_delete=models.DO_NOTHING, )
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='Category Created Date')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='Category Updated Date')
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
