from django.shortcuts import render

def index(request):
    return render(request, 'netsalaryapp/index.html')

def result(request):
    if request.method == 'POST':
        name = request.POST['name']
        gross = float(request.POST['gross_salary'])
        tax = float(request.POST['tax'])
        bonus = float(request.POST['bonus'])

        net_salary = gross - (gross * tax / 100) + (gross * bonus / 100)

        return render(request, 'netsalaryapp/result.html', {
            'name': name,
            'net_salary': net_salary
        })
    return render(request, 'netsalaryapp/index.html')

def jumble_word(request):
    jumbled = ""
    word = ""
    if request.method == 'POST':
        word = request.POST['word']
        import random
        jumbled = ''.join(random.sample(word, len(word)))

    return render(request, 'netsalaryapp/jumble.html', {
        'original': word,
        'jumbled': jumbled
    })
