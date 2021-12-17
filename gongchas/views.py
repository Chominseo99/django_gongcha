from django.shortcuts import render, get_object_or_404, redirect  # 지름길 render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from .models import Category, Beverage, Topping, Receipt
from django.contrib import messages
from .forms import ToppingUpdate

# Create your views here.


def hello(request):
    category_list = Category.objects.prefetch_related('beverages').all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'gongchas/hello.html', context)


def order_page(request, bev_id):
    beverage = get_object_or_404(Beverage, pk=bev_id)
    # Beverage.objects.get(pk=bev_id)
    toppings = Topping.objects.filter(size=beverage.size)

    # Category.objects.get(pk=id)
    context = {
        'beverage': beverage,
        'toppings': toppings,
    }
    return render(request, 'gongchas/order_page.html', context)


def check(request, bev_id):
    beverage = get_object_or_404(Beverage, pk=bev_id)

    try:
        sugar = request.POST['sugar']
        ice = request.POST['ice']
        topping_id_list = request.POST.getlist('topping', [])
        selected_option = request.POST['option']
        # 1. 주어진것: topping_id=[1, 2, 3, 4]
        # 2. id가 1인것을 가져온다.
        # 3. 2, 3, 4도 동일하게 가져온다.
        # 4. 원하는 결과물: Topping의 리스트
        toppings = []
        # if topping_id:
        for topping_id in topping_id_list:
            toppings.append(Topping.objects.get(id=topping_id))
        # [<Topping (1)>, <Topping (3)>]
        # topping[0].name
        # for a in range(len(topping)):
        #   topping[a].name
        # for b in topping:
        #   b.name

        # else:
        #     topping = None
    except (KeyError, Topping.DoesNotExist):
        return HttpResponseRedirect(reverse('gongchas:hello'))

    else:
        if beverage.is_ice_only == 1 and selected_option == 'hot':
            messages.warning(request, 'ice only 메뉴입니다. 옵션을 ice로 선택해주세요.')
            return HttpResponseRedirect(reverse('gongchas:order_page', args=(bev_id,)))

        elif selected_option == 'hot' and ice != '0':
            messages.warning(request, 'hot을 선택하셨습니다. 얼음량을 "없음"으로 선택해주세요.')
            return HttpResponseRedirect(reverse('gongchas:order_page', args=(bev_id,)))

        elif selected_option == 'ice' and ice == '0':
            messages.warning(request, 'ice를 선택하셨습니다. 얼음량을 선택해주세요.')
            return HttpResponseRedirect(reverse('gongchas:order_page', args=(bev_id,)))

        totals = beverage.price
        top_price = 0
        receipt_base = {'beverage': beverage.name,
                        'size': beverage.size,
                        'sugar': sugar,
                        'ice': ice,
                        'option': selected_option}

        add_total = {'total': totals}
        receipt_base.update(add_total)
        # MyChoice.objects.create(beverage=beverage.name, size=beverage.size, sugar=sugar, ice=ice,
        #                         option=selected_option, total=totals)

        if toppings:
            topping_total = ''
            for topping in toppings:
                # top_price += topping.price
                topping_total = topping_total + topping.name + topping.size + '(+' + str(topping.price) + ')' + ' '
                top_price += topping.price

                # 밑에 3줄 밖으로 빼
                # totals = bev_price + top_price
                # add_topping_total = {'topping': topping_total,
                #                      'total': totals}
                # receipt_base.update(add_topping_total)
            totals += top_price
            add_topping_total = {'topping': topping_total,
                                 'total': totals}
            receipt_base.update(add_topping_total)
            # MyChoice.objects.create(beverage=beverage.name, size=beverage.size, sugar=sugar, ice=ice,
            #                         option=selected_option, topping=topping.name, topping_size=topping_size,
            #                         total=totals)

        Receipt.objects.create(**receipt_base)

    messages.success(request, '주문 성공입니다.')
    return HttpResponseRedirect(reverse('gongchas:hello'))


def receipt(request):
    receipt_list = Receipt.objects.values('id', 'beverage', 'total', 'order_date')
    context = {
        'receipt': receipt_list,
    }
    return render(request, 'gongchas/receipt.html', context)


def receipt_detail(request, rec_id):
    receipt = Receipt.objects.get(id=rec_id)
    return render(request, 'gongchas/receipt_detail.html', {'receipt': receipt})


def receipt_delete(request, rec_id):
    receipt = Receipt.objects.get(id=rec_id)
    receipt.delete()
    return HttpResponseRedirect(reverse('gongchas:receipt'))


def topping(request):
    topping_list = Topping.objects.all()
    context = {
        'topping_list': topping_list
    }
    return render(request, 'gongchas/topping.html', context)


def topping_detail(request, top_id):
    topping = Topping.objects.get(id=top_id)
    return render(request, 'gongchas/topping_detail.html', {'topping': topping})


def topping_update(request, top_id):
    selected_topping = Topping.objects.get(id=top_id)

    if request.method == 'POST':
        form = ToppingUpdate(request.POST)

        # 수정할 내가 나머지 친구들과 달라야 저장한다 name, size
        # 나 빼고(제외하고) 데리고 온것중에 내가 입력받은 이름, 사이즈가 같으면(존재하면) 저장 안된다
        # 필터

        if form.is_valid():
            if Topping.objects.exclude(id=top_id).filter(name=form.cleaned_data['name'], size=form.cleaned_data['size']).exists():
                messages.warning(request, '이름과 사이즈가 중복 됩니다. 다른 내용으로 입력해주세요.')
                return HttpResponseRedirect(reverse('gongchas:topping_update', args=(top_id,)))
            # selected_topping -> id가 1인 토핑

            selected_topping.name = form.cleaned_data['name']
            selected_topping.size = form.cleaned_data['size']
            selected_topping.price = form.cleaned_data['price']

            selected_topping.save()
            return HttpResponseRedirect(reverse('gongchas:topping'))

    else:
        # GET이면 instance=topping를 통해 기존의 해당 정보를 가지고 온다
        form = ToppingUpdate(instance=selected_topping)

        return render(request, 'gongchas/topping_update.html', {'form': form})
