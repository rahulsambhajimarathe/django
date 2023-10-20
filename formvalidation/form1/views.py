from django.shortcuts import render

# Create your views here.
def home(request):
    print(request)
    data = request.GET
    name = request.GET.get('name')
    email = request.GET.get('email')
    city = request.GET.get('city')
    error = {}
    submit = request.GET.get('submit')
    
    if submit == "submit":
        if name == "" or name == None:
            error["name_err"] = "Please enter your name"
        if email == "" or email == None:
            error["email_err"] = "Please enter your email"
        if city == "" or city == None:
            error["city_err"] = "Please enter your city"
        if len(error) == 0:
            error["sucess"] = "submit successfully"
        
    
    return render(request, 'form.html', {"mail":data, "err":error})