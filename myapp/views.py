from django.shortcuts import render
import razorpay
from .models import Coffee
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))

def paymentView(request):
    if request.method=="POST":
        name_ = request.POST.get('name')
        email_ = request.POST.get('email')
        amount_ = int(request.POST.get('amount')) * 100
        print(name_,amount_,'***')
        payment = client.order.create({
            'amount' : amount_,
            'currency' : 'INR',
            'payment_capture' : '1'
        })
        coffee = Coffee(
            name = name_,
            email = email_,
            amount = amount_,
            order_id = payment['id']

        )
        coffee.save()

        context = {
            'payment' : payment,
            'coffee' : coffee,
            'razorpay_key_id' : settings.RAZORPAY_KEY_ID
        }
        return render(request,'myapp/payment.html',context)
        

    return render(request,'myapp/payment.html')


@csrf_exempt
def paymentSuccessView(request):
    print("--------")
    if request.method=='POST':
        orders = request.POST
        print(orders)
        order_id = ''
        for key,value in orders.items():
            if key == 'razorpay_order_id':
                order_id = value
                break
        print(order_id,'*******')
        new = Coffee.objects.filter(order_id = order_id).first()
        new.paid = True
        new.save()

        msg_plain = render_to_string('myapp/email.txt')
        msg_html = render_to_string('myapp/email.html')

        send_mail('Your Payment Received',msg_plain,settings.EMAIL_HOST_USER,[new.email],html_message = msg_html)

    return render(request,'myapp/success.html')



