# Generated by Django 5.1.3 on 2024-12-14 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_rename_books_book"),
    ]

    operations = [
        migrations.RenameField(
            model_name="borrowbook",
            old_name="book_id",
            new_name="book",
        ),
        migrations.RenameField(
            model_name="borrowbook",
            old_name="member_id",
            new_name="member",
        ),
    ]
