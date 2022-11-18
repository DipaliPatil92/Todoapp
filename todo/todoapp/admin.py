from django.contrib import admin
from todoapp.models import Task,Course

# Register your models here.
admin.site.register(Task)
#admin.site.register(Course)


'''
Method 1: ModelAdmin class
#step1: define ModelAdminclass
class CourseAdmin(admin.ModelAdmin):

    #list_display=['id','cname','cdur','ccat','cprice']
    #list_display=('id','cname','cdur','ccat','cprice')
    list_display=('cname',)

#step to register

admin.site.register(Course,CourseAdmin)
'''
'''
Method 2: By using decorator

step 1: Register
syntax:
     @admin.register(modelname)

step 2: Define ModelAdminClass
'''
'''
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    
    list_display=['id','cname','cdur','ccat','cprice']
'''
'''
#Adding filter to admin interface for a model
@admin.register(Course)

class CourseAdmin(admin.ModelAdmin):
    
    list_display=['id','cname','cdur','ccat','cprice']
    list_filter=['ccat','cprice']
'''
#custom filter
class FeesFilter(admin.SimpleListFilter):
    title='Course Fees'
    parameter_name='Course Fees'
    def lookups(self,request,model_admin):
        return(('high','Fees>=20000'),('low','Fees<20000'))
    def queryset(self,request,queryset):
        if self.value()=='high':
            return queryset.filter(cprice__gte=20000)
        elif self.value()=='low':
            return queryset.filter(cprice__lt=20000)
        else:
            return queryset.all()

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['cname','cdur','ccat','cprice']
    list_filter=['ccat',FeesFilter]

