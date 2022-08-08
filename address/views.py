from django.shortcuts import render,redirect # redirect 임포트 해야함
from address.models import Address

def home(request):
    # select * from addresss_address order by name;
    items = Address.objects.order_by('name')  # Adrress 클래스 . object 전체 셀렉트문
    return render(request,'address/list.html', \
                  {'items':items,'address_count':len(items)}) ## {변수명,값} {key,value}

def write(request):
    return render(request,'address/write.html')


def insert(request): ## 폼에 입력한 값들이 request 에 저장
    # #post방식으로 값전달 POST 방식으로 전달
    # request.GET['변수명'] GET 방식으로 전달된 데이터
    # Address= > 클래스임
    addr=Address(name=request.POST['name'],tel=request.POST['tel'],\
                 email=request.POST['email'],address=request.POST['address'])
    addr.save() # 내부적으로 insert 쿼리 실행 DB 레코드저장
    return redirect('/address')  # address 주소로 가기

def detail(request):
    id=request.GET['idx']
    addr = Address.objects.get(idx=id)
    return render(request,'address/detail.html',{'addr':addr})

def update(request):
    id=request.POST['idx']
    addr=Address(idx=id, name=request.POST['name'] ,tel=request.POST['tel'],
                 email=request.POST['email'],address=request.POST['address'])
    addr.save()
    return redirect('/address')


def delete(request):
    id=request.POST['idx']
    Address.objects.get(idx=id).delete()
    return redirect('/address')