from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class InternalProperty(models.Model):

    PROPERTY_TYPES = [
        ('jual', 'Jual'),
        ('sewa', 'Sewa'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('sold', 'Sold Out'),
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

    PROPERTY_CATEGORY_CHOICES = [
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

    

    # ======================
    # AGENT INFO
    # ======================

    owner = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name='properties',
            null=True,
            blank=True
            )
    # owner_username = models.CharField(max_length=100, blank=True, null=True)
    agent_name = models.CharField(max_length=100)
    agent_phone = models.CharField(max_length=30, blank=True, null=True)
    agent_whatsapp = models.CharField(max_length=30, blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='active'
    )

    # ======================
    # PROPERTY INFO
    # ======================

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.BigIntegerField()
    location = models.CharField(
        max_length=50,
        choices=KOTA_CHOICES
    )
    wilayah = models.CharField(
        max_length=255,
        blank=True
    )
    full_address = models.TextField(blank=True, null=True)
    google_drive_link = models.URLField(blank=True, null=True)
    property_type = models.CharField(max_length=10, choices=PROPERTY_TYPES)
    property_category = models.CharField(
        max_length=50,
        choices=PROPERTY_CATEGORY_CHOICES
    )
    area_surface = models.IntegerField(blank=True, null=True)
    area_building = models.IntegerField(blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)

    # ======================
    # OPTIONAL EXTRA INFO
    # ======================

    land_certificate = models.CharField(max_length=50, blank=True, null=True)
    building_year = models.IntegerField(blank=True, null=True)
    listing_status = models.CharField(max_length=20, default='available')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.id}")

            InternalProperty.objects.filter(
                pk=self.pk
            ).update(
                slug=self.slug
            )

    def __str__(self):
        return self.title


class PropertyImage(models.Model):

    property = models.ForeignKey(
        InternalProperty,
        related_name='images',
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return self.property.title