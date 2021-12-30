from django.shortcuts import render

def index(request):
    data = {
        'title':'Главная страница',
        'head_text':'Главная страница!',
        'values': {
            'text':'Привет, я текст',
            'age': 20,
        },
    }
    return render(request,'mainApp/homepage.html', data)

def about(reques):
    return render(reques, 'about/aboutpage.html')

