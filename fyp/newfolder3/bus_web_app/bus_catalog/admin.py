import atexit
from django.contrib import admin
from .models import Assigntrip
from  .models import AuthUser
from .models import Bookingtickets
from .models import  Buses
from .models import  Drivers
from .models import  Notifications
from .models import Operators
from .models import  Routes
from .models import Seat
from .models import Feedback

admin.site.register(Assigntrip)
admin.site.register(AuthUser)
admin.site.register(Bookingtickets)
admin.site.register(Buses)
admin.site.register(Drivers)
admin.site.register(Notifications)
admin.site.register(Operators)
admin.site.register(Routes)
admin.site.register(Seat)
admin.site.register(Feedback)



# Register your models here.
