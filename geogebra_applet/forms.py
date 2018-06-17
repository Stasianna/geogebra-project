"""from django.shortcuts import render_to_response


class GeogebraAppletForm(forms.ModelForm):
    "Форма для загрузки архива""

    class Meta:
        model = GeogebraApplet
        fields = ['archive']


def main_page(request):
    # если в POST есть данные, значит это post-запрос и мы пытаемся загрузить архив
    if request.POST:
        # инициализируем форму с переданными данными
        form = GeogebraAppletForm(request.POST, request.FILES)
        # если в форме нет ошибок, сохраняем
        if form.is_valid():
            form.save()
    else:
        # get запрос, просто инициализируем форму, чтобы вывести на странице
        form = GeogebraAppletForm()

    # получаем все чертежи
    applet_list = GeogebraApplet.objects.all()
    # форму и список чертежей добавляем контекст, чтобы отрисовать в шаблоне
    context = {
        form: form, applet_list: applet_list
    }
    return render_to_response('index.html', context) """