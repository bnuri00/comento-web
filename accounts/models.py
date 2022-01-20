from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

# velog.io/@mmy789 포스팅 참고
# 정규식 이용, 유효성 검사
class CustomUser(AbstractUser):
    fullNameRegex = RegexValidator(regex=r'^[가-힣]+$')
    fullname = models.CharField(validators=[fullNameRegex], max_length=20)
    nickname = models.CharField(max_length=50, unique=True, blank=True, null=True)

    phoneNumberRegex = RegexValidator(regex=r'^01([0|1|6|7|8|9]?)-?([0-9]{3,4})-?([0-9]{4})$')
    phone = models.CharField(validators=[phoneNumberRegex], max_length=13, unique=True)

    # 우편번호, 도로명주소, 상세주소
    zipcodeRegex = RegexValidator(regex=r'^[0-9]+$')
    zipcode = models.CharField(validators=[zipcodeRegex], max_length=5, blank=True)
    addr1 = models.CharField(max_length=100, blank=True)
    addr2 = models.CharField(max_length=100, blank=True)

    def clean(self):
        if self.nickname == "":
            self.nickname = None
