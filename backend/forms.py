from django import forms


class UserForm(forms.Form):
        my_field = forms.CharField(label='My Field', max_length=100)
        
        
        
def get_all(request):
        return JsonResponse(list(Users.objects.all().values()), safe=False)

