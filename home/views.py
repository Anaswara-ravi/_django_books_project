from django.shortcuts import render


books = [
    {
        'id': 1,
        'title': 'Python Crash Course',
        'author': 'Eric Matthes',
        'category': 'Programming',
        'year': 2019
    },
    {
        'id': 2,
        'title': 'Django for Beginners',
        'author': 'W. S. Vincent',
        'category': 'Web',
        'year': 2022
    },
    {
        'id': 3,
        'title': 'Clean Code',
        'author': 'Robert Martin',
        'category': 'Programming',
        'year': 2008
    },
    {
        'id': 4,
        'title': 'Atomic Habits',
        'author': 'James Clear',
        'category': 'Self-help',
        'year': 2018
    },
    {
        'id': 5,
        'title': 'The Pragmatic Programmer',
        'author': 'Hunt & Thomas',
        'category': 'Programming',
        'year': 1999
    },
    {
        'id': 6,
        'title': 'Sapiens',
        'author': 'Yuval Harari',
        'category': 'History',
        'year': 2011
    }
]


def home(request):
    return render(request, 'home.html', {'featured': books[:3]})


def about(request):
    return render(request, 'about.html')


def book_list(request):
    return render(request, 'books.html', {'books': books})
def book_detail(request, book_id):

    for book in books:

        if book['id'] == book_id:

            return render(request, 'book_detail.html', {'book': book})

    return render(request, 'book_detail.html', {'book': None})