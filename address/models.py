from django.db import models

# claa 클래스이름(상위클래스) 상속!!
class Address(models.Model):
    # 필드명 = 자료형
    idx = models.AutoField(primary_key=True) # 자동증가 일련번호
    name = models.CharField(max_length=50,blank=True,null=True)
    tel = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)


    # class Address   class Address 클래스 생성하는 부분, models.Model models 내장객체에서 Model 사용
    # models.AutoField = mysql 에서 Autoincreament 같은 자동증가
    # charField = > varchar 문자형 타입
    # max_lenght = > 최대글자 , blank = 공백가능 , null = null 값 가능