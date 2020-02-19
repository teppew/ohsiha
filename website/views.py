from django.shortcuts import render
# from django.http import HttpResponse

# Something very random to text how the query should work
posts = [
    {
        'author': 'Teemu',
        'title': 'First post',
        'date': 'Feb 19, 2020',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    },
    {
        'author': 'Pertti',
        'title': 'Second post',
        'date': 'Feb 20, 2020',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    }
]


def home(request):
    context = {
        'posts' : posts
    }

    # Takes the html file from templates folder which is inside the website project folder
    return render(request, 'website/home.html', context)


def about(request):
    return render(request, 'website/about.html')
