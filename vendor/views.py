from django.shortcuts import render, redirect
from .forms import SellerRequestForm

def seller_request_view(request):
    from cart.models import CartItem  # واردات داخل تابع

    user = request.user if request.user.is_authenticated else None
    countcart = CartItem.objects.filter(cart__user=user).count() if user else 0

    if request.method == 'POST':
        form = SellerRequestForm(request.POST, request.FILES)
        if form.is_valid():
            seller_request = form.save(commit=False)
            seller_request.user = request.user
            seller_request.save()

            return redirect('success_page')  # هدایت به صفحه‌ی موفقیت
    else:
        form = SellerRequestForm()

    return render(request, 'vendor/seller_request.html', {'form': form,'countcart':countcart})
