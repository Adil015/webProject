from django.contrib import admin
from portfolio.models import Contact 
from portfolio.models import Intro
from portfolio.models import Edu
from portfolio.models import Project
from portfolio.models import Skill
from portfolio.models import Exp


class PortfolioAdmin(admin.ModelAdmin):
    list_display=('Intro_Name','Intro_par')
# Register your models here.
admin.site.register(Contact)
admin.site.register(Intro,PortfolioAdmin)
admin.site.register(Edu)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Exp)