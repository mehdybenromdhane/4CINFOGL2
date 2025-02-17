from django.contrib.auth.forms  import UserCreationForm

from django.contrib.auth import get_user_model

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        
        fields= ['cin', 'first_name', 'last_name', 'email','username', 'password1', 'password2']
        
    
    def save(self,commit=True):
        user = super(UserRegisterForm,self).save(commit=False)
        
        if commit: 
            user.save()
            
        return user