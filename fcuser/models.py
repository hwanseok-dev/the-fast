from django.db import models


class Fcuser(models.Model):
    email = models.EmailField(max_length=256, verbose_name="이메일", unique=True)
    level = models.CharField(max_length=8, verbose_name="등급",
                             choices=(
                                 ('admin', 'admin'),
                                 ('admin', 'user')
                             ))
    password = models.CharField(max_length=256, verbose_name="비밀번호")
    register_date = models.DateTimeField(auto_now_add=True, verbose_name="등록 날짜")

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'fastcampus_fcuser'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'
