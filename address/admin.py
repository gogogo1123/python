from django.contrib import admin

from address.models import Address


class AddressAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 관리할 필드명 앞에서 만들 필드명!!
    # models 만들 필드명이랑 똑같이
    list_display = ('name','tel','email','address')

#그리고 등록 Address 랑 AdrdressAdmin 연결 등록
admin.site.register(Address, AddressAdmin)
