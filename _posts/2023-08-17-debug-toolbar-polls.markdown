---
layout: post
title:  "Displaying the Django Debug Toolbar in the Demo Polls App"
date:   2023-08-17 00:00:00 +0000
categories: python django
permalink: /django-debug-toolbar-polls-app/
---

I've been going through [Writing your first Django app](https://docs.djangoproject.com/en/4.2/intro/tutorial01/) recently. I was looking for a simple website/project I could look at scaling and push the limits of, what better than the polls app! Step one of any efforts is to measure, so I tried adding the [Django debug toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/). No matter what I tried from the installation steps I couldn't get it to show.

### You need valid html!

Long story short here - add <html> and <body> tags to your template. Turns out that the debug toolbar looks for these and then injects itself onto the page from there. If it can't find them it won't show!

The version of the polls app I went through didn't have these elements included.

### Adding a base page

To solve this I added a reusable base page. Create a file called base_page.html in polls/templates/polls with the following.

```
{% load static %}

<html>
   <head>
        <link rel="stylesheet" href="{% static 'polls/style.css' %}">
   </head>
   <body>
        {% block content %}{% endblock content %}
   </body>
</html>
```

Then update index.html in polls/templates/polls to use the new base page.

```
{% extends "polls/base_page.html" %}

{% block content %}
    {% if latest_question_list %}
        <ul>
        {% for question in latest_question_list %}
            <li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
        {% endfor %}
        </ul>
    {% else %}
        <p>No polls are available.</p>
    {% endif %}
{% endblock content %}
```

And that's it! You should now see the debug toolbar on the index page. If you want to see it on the other pages too, just add the base_page there too.

![Page with toolbar](/assets/images/debug_toolbar.png)
