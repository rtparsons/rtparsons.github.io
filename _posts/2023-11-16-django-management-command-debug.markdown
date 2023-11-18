---
layout: post
title:  "Debugging manage.py commands in VSCode with Docker"
date:   2023-11-16 00:00:00 +0000
categories: python django vscode docker
permalink: /django-debug-management-command-vscode-docker/
---

I tend to run my Django application in a Docker container for all the benefits it gives when working with a team or deploying the application. It does however introduce extra hundles in everyday development.

To debug the application I use [debugpy](https://londonappdeveloper.com/debugging-a-dockerized-django-app-with-vscode/). Whilst the application is running this allows me to attach a debugger to the container, and debug the the application. This only works however for web requests and will not intercept anything triggered from the command line. This sucks as I have loads of manage.py commands I trigger via the command line or cron!

## My Workaround

Template:
```
{% raw %}
<html>
    <body>
        <form method="post">
            {% csrf_token %}
            Command: <input type="text" name="command" />
            <input type="submit" value="run" />
        </form>
    </body>
</html>
{% endraw %}
```

View:
```
from django.core.management import call_command

def command_runner(request):
    if request.method == 'POST':
        to_run = request.POST.get('command', '')
        to_run = to_run.replace('python manage.py ', '')
        if to_run:
            command_name = to_run.split(' ')[0]
            call_command(command_name, *to_run.split(' ')[1:])
        return render(request, 'command_runner.html')
```

I created a simple page, in which you can enter the same manage.py command. By excecuting `call_command` from the web page we can still run the manage.py command, but from the web context allowing breakpoints to be hit!
