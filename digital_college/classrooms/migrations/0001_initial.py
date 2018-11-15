# Generated by Django 2.1.2 on 2018-11-15 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.IntegerField()),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
            ],
        ),
        migrations.CreateModel(
            name='matching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('match1', models.CharField(max_length=100)),
                ('match2', models.CharField(max_length=100)),
                ('match3', models.CharField(max_length=100)),
                ('match4', models.CharField(max_length=100)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Courses')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
            ],
        ),
        migrations.CreateModel(
            name='multiplechoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Courses')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
            ],
        ),
        migrations.CreateModel(
            name='quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_quiz', models.CharField(max_length=50)),
                ('instructions', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('total_marks', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Courses')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
            ],
        ),
        migrations.CreateModel(
            name='singlechoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('answer', models.IntegerField()),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Courses')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.quiz')),
            ],
        ),
        migrations.CreateModel(
            name='truefalse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('option1', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=100)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Courses')),
                ('college_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Registered_College')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.quiz'),
        ),
        migrations.AddField(
            model_name='matching',
            name='quiz_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.quiz'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classrooms.multiplechoice'),
        ),
    ]
