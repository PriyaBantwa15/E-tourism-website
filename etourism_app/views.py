from django.shortcuts import render , redirect
from .models import login, package, hotel, place_detail, feedback, inquiry, bookings
from django.contrib import messages

# Create your views here.
def loginpage(request):
    return render(request,'login.html')

def Package(request):
    fetchpackage = package.objects.all()
    return render(request,'Package.html',{'package':fetchpackage})

def index1(request):
    return render(request,'index1.html')

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def book(request):
    return render(request, 'book.html')

def book1(request , id):
    pid = id
    return render(request, 'book.html',{'id':pid})


def dobookings(request):
    if request.method == 'POST':
        uid = request.session['log_id']
        uemail = request.session['log_user']
        pid = request.POST.get("pid")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        number = request.POST.get("number")
        d_date = request.POST.get("d_date")
        a_date = request.POST.get("a_date")
        guest = request.POST.get("guest")
        file = request.FILES['file1']
        query = bookings(package_id=package(id=pid),login_id=login(id=uid),first_name=fname,last_name=lname,email=email,phone=number,departure_Date=d_date,arrival_date=a_date,guest=guest,certificate=file,b_status=1)
        query.save()
        messages.error(request, 'Booking Done')

        try:

            print('aaa\naaa')
            import smtplib

            gmail_user = 'etourismm@gmail.com'
            gmail_password = 'phbs422923'

            sent_from = gmail_user
            to = [email]
            subject = 'Booking Successful'
            body = 'Booking Done Successfully. Thank you for visiting e-tourism portal.'


            email_text = """\
                   From: %s
                   To: %s
                   Subject: %s

                   %s
                   """ % (sent_from, ", ".join(to), subject, body)

            try:
                smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                smtp_server.ehlo()
                smtp_server.login(gmail_user, gmail_password)
                smtp_server.sendmail(sent_from, to, email_text)
                smtp_server.close()
                print("Email sent successfully!")
            except Exception as ex:
                print("Something went wrong", ex)

            return render(request, 'index.html')
        except:
            messages.info(request, 'Account does not exist on that email.')
            return render(request, 'ResetPasswordOTP.html')
    else:
        messages.error(request, 'Error Occured')
    return render(request,'index.html')




def inquiry_data(request):
    if request.method == 'POST':
        try:
            uid = request.session['log_id']
            user = login.objects.get(id=uid)

        except login.DoesNotExist:
            user = None
        name = request.POST.get("name")
        phone_no = request.POST.get("phone")
        msg = request.POST.get("issues")
        query = inquiry(login_id=user,name=name,phone=phone_no,message=msg,i_status=1)
        query.save()
    else:
        messages.error(request, 'please login')
        return render(request, 'inquiry.html')

    return render(request,'inquiry.html')

def detail1(request,id):
    print(id)
    fetchhotels = hotel.objects.all().filter(package_id=id)
    fetchdetails = place_detail.objects.all().filter(package_id=id)
    print(fetchdetails)
    print(fetchhotels)
    return render(request,'detail1.html',{'hotel':fetchhotels,'place_detail':fetchdetails , 'pid':id})


def gallery(request):
    return render(request,'gallery.html')


def login_signup(request):
    if request.method == 'POST':

        email_id = request.POST.get("email_id")
        password = request.POST.get("Password")
        phone_no = request.POST.get("phone")
        query = login(email_id=email_id,password=password,phone_no=phone_no,role=2,status=1)
        query.save()
        return redirect('login.html')
    else:
        messages.error(request, 'error occured')

    return render(request, 'login.html')

def checklogin(request):
    if request.method == 'POST':
        username = request.POST['email_id']
        password = request.POST['Password']

        try:
            user = login.objects.get(email_id=username, password=password)
            request.session['log_user'] = user.email_id
            request.session['log_id'] = user.id
            request.session.save()


        except login.DoesNotExist:
            user = None

        if user is not None:
            return render(request, 'index.html')

        else:
            messages.info(request, 'account done not exit plz sign in')
    return render(request,'login.html')

def dashboard(request):
    try:
        if request.session.is_empty():
            return render(request,'login.html')
        else:
            try:
                uid = request.session['log_id']
                user = login.objects.get(id=uid)

            except login.DoesNotExist:
                user = None
            return render(request, 'index.html')
    except:
        pass
    return render(request, 'login.html')

def contact(request):
    if request.method == 'POST':
        try:
            uid = request.session['log_id']
            user = login.objects.get(id=uid)

        except login.DoesNotExist:
            user = None

        name = request.POST.get("name")
        rate = request.POST.get("rate")
        review = request.POST.get("review")
        query = feedback(login_id=user,user_name=name,ratting=rate,comment=review)
        query.save()
    else:
        messages.error(request, 'Please login')
        return render(request, 'contact.html')
    return render(request,'contact.html')


def logout(request):
   try:
      del request.session['log_user']
      del request.session['log_id']
   except:
      pass
   return render(request,'login.html')


