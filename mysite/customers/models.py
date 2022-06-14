from django.db import models


class Customer(models.Model):
    ho_va_ten = models.CharField(max_length=250, blank=False)
    email = models.CharField(max_length=250, blank=False)
    profile_image = models.ImageField(default='customers_profile/default.jpg', upload_to='customers_profile')
    mat_khau = models.CharField(max_length=100, blank=False)
    dien_thoai = models.CharField(max_length=20)
    dia_chi = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.email
