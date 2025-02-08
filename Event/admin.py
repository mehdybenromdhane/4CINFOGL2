from django.contrib import admin,messages

# Register your models here.

from .models import Event,Participants


admin.site.register(Participants)




class numberOfParticipantsFilter(admin.SimpleListFilter):
    
    title="Number of participants"
    
    parameter_name='nbr'
    
    
    def lookups(self , request,model_admin):
        
        return (
            ('No',("No participants")),
            ('Yes',('There are participants')),
        )
        
    def queryset(self,request,queryset):
        if self.value() == "No":
            return queryset.filter(nbr_participants__exact=0)
        
        if self.value()=="Yes":
            return queryset.filter(nbr_participants__gt=0)
    
    

class ParticipationInline(admin.TabularInline):
    model = Participants
    extra=10




def accept_state(ModelAdmin,request,queryset):
    
    queryset.update(state=True)
    
    
    messages.success(request, "Events successfully updated")
    
    
def refuse_state(ModelAdmin,request,queryset):
    
    queryset.update(state=False)
    
    
    messages.success(request, "Events successfully updated")
    
    


accept_state.short_description = "Change state to true"
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    
    list_display = ('title','category','evt_date','state','nbr_participants','organisateur')
    
    # readonly_fields=('nbr_participants',)
    
    list_per_page=1
    
    search_fields=('title','category',)
    
    
    actions=[accept_state ,refuse_state]
    
    autocomplete_fields=['organisateur']
    
    
    list_filter=('category',numberOfParticipantsFilter)
    
    inlines=[ParticipationInline]