from app.model import Mess


def VIEW_MENU(request):

    Menu = Mess.objects.all()
    context = {
        'day': Menu,
    }
    return render(request, 'owner/view_menu.html', context)


def ADD_MENU(request):
    if request.method == 'POST':
        day = request.POST.get('day')
        breakfast = request.POST.get('breakfast')
        lunch = request.POST.get('lunch')
        dinner = request.POST.get('dinner')
        mess = Mess(day=day, breakfast=breakfast, lunch=lunch, dinner=dinner)
        mess.save()
        messages.success(request, 'Menu is successfully added')
    # got error of else: removed and fixed
    return render(request, 'owner/add_menu.html')

# edit menu table


def EDIT_MENU(request):
    # Menu = Mess.objects.get(id=id)
    Menu = Mess.objects.all()
    context = {
        'day': Menu,
    }
    return render(request, 'owner/edit_menu.html', context)
