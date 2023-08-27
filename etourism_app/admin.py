from django.contrib import admin
from .models import hotel,login,package,feedback,inquiry,bookings,place_detail
# Register your models here.
class showbooking(admin.ModelAdmin):
    list_display = ('package_id','login_id','first_name','last_name','email','phone','departure_Date','arrival_date','guest','certificate','b_status','timestamp')

class showcovid_cases(admin.ModelAdmin):
    list_display = ('active_cases', 'total_cases', 'current_cases', 'total_death','timestamp')

class showcovid_vaccinated_certificate(admin.ModelAdmin):
    list_display = ('login_id','certificate')

class showhotel(admin.ModelAdmin):
    list_display = ('package_id','hotel_name','address_link','time','location')

class showpackage(admin.ModelAdmin):
    list_display = ('name','details','schemes','prices')


class showfeedback(admin.ModelAdmin):
    list_display = ('login_id','user_name','ratting','comment')

class showinqury(admin.ModelAdmin):
    list_display = ('login_id','name','phone','message','i_status')

class showdetail(admin.ModelAdmin):
    list_display = ('package_id','place_name','desc','video')

admin.site.register(hotel,showhotel)
admin.site.register(package,showpackage)
admin.site.register(bookings,showbooking)
admin.site.register(feedback,showfeedback)
admin.site.register(inquiry,showinqury)
admin.site.register(place_detail,showdetail)
admin.site.register(login)