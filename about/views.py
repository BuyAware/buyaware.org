from django.shortcuts import render

def about_index(request):
    '''
    main about page.
    '''

    return render(request, 'about/about.html')

