from django.shortcuts import render, redirect
from .forms import FormDangKy, FormDangNhap, FormThongTin, FormDoiMatKhau
from .models import Customer
from myshop.my_module import check_session
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.template import RequestContext

def login(request):
    session_status = check_session(request, 'sessionKhachHang')
    if session_status:
        return redirect('myshop:index')

    # Đăng ký
    form_dk = FormDangKy()
    result_register = ''
    if request.POST.get('btnDangKy'):
        form_dk = FormDangKy(request.POST)

        # Kiểm tra email tồn tại hay chưa
        email = request.POST.get('email')
        khach_hang = Customer.objects.filter(email=email)
        if khach_hang.count() > 0:
            result_register = '''
                <div class="alert alert-warning alert-dismissible fade show" role="alert">
                    Email đã tồn tại. Vui lòng kiểm tra lại
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            '''
        else:
            if form_dk.is_valid() and form_dk.cleaned_data['mat_khau'] == form_dk.cleaned_data['xac_nhan_mat_khau']:
                hasher = PBKDF2PasswordHasher()
                request.POST._mutable = True
                post = form_dk.save(commit=False)
                post.ho_va_ten = form_dk.cleaned_data['ho_va_ten']
                post.email = form_dk.cleaned_data['email']
                post.mat_khau = hasher.encode(form_dk.cleaned_data['mat_khau'], '123')
                post.dien_thoai = form_dk.cleaned_data['dien_thoai']
                post.dia_chi = form_dk.cleaned_data['dia_chi']
                post.save()
                result_register = '''
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    Đăng ký thông tin thành công.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''

    # Đăng nhập
    form_dn = FormDangNhap()
    result_login = ''
    if request.POST.get('btnDangNhap'):
        email = request.POST.get('email')
        mat_khau = request.POST.get('mat_khau')
        hasher = PBKDF2PasswordHasher()
        encoded = hasher.encode(mat_khau, '123')

        khach_hang = Customer.objects.filter(email=email, mat_khau=encoded)
        if khach_hang.count() > 0:
            request.session['sessionKhachHang'] = khach_hang.values()[0]
            print(request.session['sessionKhachHang'])
            return redirect('myshop:index')
        else:
            result_login = '''
                <div class="alert alert-danger alert-dismissible fade show" role="alert">
                    Đăng nhập thất bại.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                '''
    context = {
        "login_page": "active",
        'form_dk': form_dk,
        'result_register': result_register,
        'form_dn': form_dn,
        'result_login': result_login,


    }
    return render(request, 'customers/login.html', context)


def customer_info(request):
    session_status = check_session(request, 'sessionKhachHang')
    if not session_status:
        return redirect('customers:login')
    customer = Customer.objects.get(id=request.session['sessionKhachHang']['id'])
    update_msg = ''
    form_thongtin = FormThongTin(instance=customer)
    form_doimatkhau = FormDoiMatKhau()
    change_password_msg = ''

    if request.POST.get('btnCapNhat'):
        form_thongtin = FormThongTin(request.POST, request.FILES, instance=customer)
        if form_thongtin.is_valid():
            form_thongtin.save()
            update_msg = '''
                <div class="alert alert-success alert-dismissible fade show" id="myAlert" role="alert">
                    Cập nhật thông tin thành công.
                    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            '''

    if request.POST.get('btnDoiMatKhau'):
        form_doimatkhau = FormDoiMatKhau(request.POST)
        if form_doimatkhau.is_valid():
            form_doimatkhau.save()
            hasher = PBKDF2PasswordHasher()
            mat_khau = hasher.encode(form_doimatkhau.cleaned_data['mat_khau'], '123')
            if mat_khau == request.session['sessionKhachHang']['mat_khau']:
                if form_doimatkhau.cleaned_data['mat_khau_moi'] == form_doimatkhau.cleaned_data['xac_nhan_mat_khau']:
                    khach_hang = Customer.objects.get(email=request.session['sessionKhachHang']['email'])
                    khach_hang.mat_khau = hasher.encode(form_doimatkhau.cleaned_data['mat_khau_moi'], '123')
                    khach_hang.save()
                    khach_hang_dict = khach_hang.__dict__
                    del(khach_hang_dict['_state'])
                    del(khach_hang_dict['profile_image'])
                    request.session['sessionKhachHang'] = khach_hang_dict
                    change_password_msg = '''
                        <div class="alert alert-success alert-dismissible fade show" id="myAlert" role="alert">
                            Đổi mật khẩu thành công.
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                    '''
            else:
                change_password_msg = '''
                        <div class="alert alert-secondary alert-dismissible fade show" id="myAlert" role="alert">
                            Đổi mật khẩu thất bại.
                            <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                    '''

    context = {
        "customer_page": "active",
        "form_thongtin": form_thongtin,
        "update_msg": update_msg,
        "form_doimatkhau": form_doimatkhau,
        "change_password_msg": change_password_msg,
    }

    return render(request, 'customers/customer_info.html', context)


def logout(request):
    if request.session.get('sessionKhachHang'):
        del request.session['sessionKhachHang']
    return redirect('customers:login')
