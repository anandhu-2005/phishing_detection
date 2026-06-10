from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='FeedbackReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=2048)),
                ('report_type', models.CharField(choices=[('false_positive', 'False positive'), ('missed_threat', 'Missed threat'), ('correct', 'Correct')], max_length=32)),
                ('notes', models.TextField(blank=True)),
                ('reported_timestamp', models.CharField(blank=True, max_length=64)),
                ('features', models.JSONField(blank=True, default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
