from myshop.my_module import check_session

from .models import Customer
from django.shortcuts import get_object_or_404


def check_authenticate(request):
    profile_image = 'customers_profile/default.jpg'

    session_status = check_session(request, 'sessionKhachHang')
    session_info = ''

    if session_status:
        session_info = request.session.get('sessionKhachHang')
        khach_hang = get_object_or_404(Customer, email=request.session['sessionKhachHang']['email'])
        # khach_hang = Customer.objects.get(email=request.session['sessionKhachHang']['email'])
        profile_image = khach_hang.profile_image

    return {
        'session_info': session_info,
        'session_status': session_status,
        'profile_image': profile_image,
    }