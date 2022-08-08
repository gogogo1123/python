from django.shortcuts import render


def home(request): # request => 전달하는값들
    # templeate == > 템플릿을 해석해서 html 코드를 작성해주는 형식 html code
    return render(request,'index.html')
