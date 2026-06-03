from student.models import Cart,WishList

def cart_count(request):
    if request.user.is_authenticated:
        cnt=Cart.objects.filter(student_object=request.user).count()
        return {"cart_count":cnt}
    else:
        return {"cart_count":0}

def wish_count(request):
    if request.user.is_authenticated:
        cnt=WishList.objects.filter(student_object=request.user).count()
        return {"wish_count":cnt}
    else:
        return {"wish_count":0}