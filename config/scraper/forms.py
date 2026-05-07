from django import forms

TIPE_CHOICES = [
    ("rumah", "Rumah"),
    ("apartemen", "Apartemen"),
    ("tanah", "Tanah"),
    ("ruko", "Ruko"),
    ("pabrik", "Pabrik"),
    ("perkantoran", "Perkantoran"),
    ("ruang-usaha", "Ruang Usaha"),
    ("gudang", "Gudang"),
    ("villa", "Villa"),
    ("kost", "Kost"),
    ("hotel", "Hotel"),
    ("tempat-usaha", "Tempat Usaha"),
    ("kios", "Kios"),
]

KOTA_CHOICES = [
    ("dki-jakarta", "Jakarta"),
    ("jakarta-selatan", "Jakarta Selatan"),
    ("jakarta-barat", "Jakarta Barat"),
    ("jakarta-timur", "Jakarta Timur"),
    ("jakarta-utara", "Jakarta Utara"),
    ("jakarta-pusat", "Jakarta Pusat"),

    ("tangerang", "Tangerang"),
    ("tangerang-selatan", "Tangerang Selatan"),
    ("bekasi", "Bekasi"),
    ("depok", "Depok"),
    ("bogor", "Bogor"),

    ("bandung", "Bandung"),
    ("surabaya", "Surabaya"),
    ("medan", "Medan"),
    ("semarang", "Semarang"),
    ("yogyakarta", "Yogyakarta"),
    ("bali", "Bali"),
]

JUAL_SEWA_CHOICES = [
    ("jual", "Jual"),
    ("sewa", "Sewa"),
]

class ScraperForm(forms.Form):
    kota = forms.ChoiceField(
        choices=KOTA_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )
    wilayah = forms.CharField(required=False)
    kata_kunci = forms.CharField(required=False)

    jual_sewa = forms.ChoiceField(choices=JUAL_SEWA_CHOICES)
    tipe = forms.ChoiceField(choices=TIPE_CHOICES)

    min_harga = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'rupiah'
        })
    )

    max_harga = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'rupiah'
        })
    )

    min_luas_tanah = forms.IntegerField(required=False)
    max_luas_tanah = forms.IntegerField(required=False)

    min_luas_bangunan = forms.IntegerField(required=False)
    max_luas_bangunan = forms.IntegerField(required=False)
