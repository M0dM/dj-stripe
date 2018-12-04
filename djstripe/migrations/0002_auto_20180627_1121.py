# Generated by Django 2.0.6 on 2018-06-27 08:21

from django.db import migrations, models

import djstripe.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djstripe", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="business_name",
            field=models.CharField(help_text="The publicly visible name of the business", max_length=255, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="account",
            name="support_url",
            field=models.CharField(help_text="A publicly shareable URL that provides support for this account", max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="charge",
            name="receipt_number",
            field=models.CharField(help_text="The transaction number that appears on email receipts sent for this charge.", max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="deactivate_on",
            field=djstripe.fields.JSONField(help_text="An array of connect application identifiers that cannot purchase this product. Only applicable to products of `type=good`.", null=True, blank=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="images",
            field=djstripe.fields.JSONField(help_text="A list of up to 8 URLs of images for this product, meant to be displayable to the customer. Only applicable to products of `type=good`.", null=True, blank=True),
        ),
    ]
