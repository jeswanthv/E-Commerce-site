from django.db import migrations
from api.user.models import CustomUser

class Migration(migrations.Migration):
    def seed_data(apps, schema_editor):
        user = CustomUser(name="jeswanth",
                          email="jeswanth@gmail.com",
                          is_staff=True,
                          is_superuser=True,
                          phone="987654321",
                          gender="male"
                            )
        user.set_password("jeswanth")
        user.save()

    dependencies =[

    ]

    operations = [
        migrations.RunPython(seed_data),
    ]