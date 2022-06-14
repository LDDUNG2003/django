from django import forms
from customers import models


class FormDangKy(forms.ModelForm):
    ho_va_ten = forms.CharField(max_length=250, label='Họ và tên', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Nhập họ và tên",
    }))
    email = forms.CharField(max_length=250, label='Email', widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Nhập Email",
    }))
    mat_khau = forms.CharField(max_length=100, label='Mật khẩu', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Nhập mật khẩu",
    }))
    xac_nhan_mat_khau = forms.CharField(max_length=100, label='Nhập lại mật khẩu', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Nhập lại mật khẩu",
    }))
    dien_thoai = forms.CharField(max_length=20, label='Điện thoại', widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Nhập số điện thoại"
    }))
    dia_chi = forms.CharField(label='Địa chỉ', widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "Nhập địa chỉ",
        "rows": 2,
        "style": "resize:none",
    }))
  

    class Meta:
        model = models.Customer
        fields = '__all__'


class FormDangNhap(forms.ModelForm):
    email = forms.CharField(max_length=250, label='Email', widget=forms.EmailInput(attrs={
        "class": "form-control",
        "placeholder": "Tên tài khoản hoặc Email",
        "required": "required",
    }))
    mat_khau = forms.CharField(max_length=100, label='Mật khẩu', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "placeholder": "Mật khẩu",
        "required": "required",
    }))

    class Meta:
        model = models.Customer
        fields = ['email', 'mat_khau']


class FormThongTin(forms.ModelForm):
    ho_va_ten = forms.CharField(max_length=250, label='Họ và tên:', widget=forms.TextInput(attrs={
        "class": "form-control",
        "readonly": "readonly",
    }))
    email = forms.CharField(max_length=250, label='Email:', widget=forms.EmailInput(attrs={
        "class": "form-control",
        "readonly": "readonly",
    }))
    dien_thoai = forms.CharField(max_length=20, label='Số điện thoại', widget=forms.TextInput(attrs={
        "class": "form-control",
    }))
    dia_chi = forms.CharField(max_length=2000, label='Địa chỉ', widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 2,
        "style": "resize:none",
    }))
    profile_image = forms.ImageField(required=False, label='Ảnh đại diện', widget=forms.FileInput(attrs={
        "class": "form-control-file",
    }))

    class Meta:
        model = models.Customer
        fields = ['ho_va_ten', 'email', 'dien_thoai', 'dia_chi', 'profile_image']


class FormDoiMatKhau(forms.ModelForm):
    mat_khau = forms.CharField(max_length=100, label='Mật khẩu cũ:', widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    mat_khau_moi = forms.CharField(max_length=100, label='Mật khẩu mới:', widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))
    xac_nhan_mat_khau = forms.CharField(max_length=100, label='Xác nhận mật khẩu:', widget=forms.PasswordInput(attrs={
        "class": "form-control",
    }))

    class Meta:
        model = models.Customer
        fields = ['mat_khau']

