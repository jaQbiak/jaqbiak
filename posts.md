---
layout: default
permalink: /posts
nav_active: posts
---

<div id="content">
    <table>
        {% for post in site.posts %}
            <tr>
                <td>{{ post.date | date: "%Y-%m-%d %H:%M" }}</td><td><a href="{{ post.url | relative_url }}" {% if forloop.first %}id="first_post"{% endif %}>{{ post.title }} 👾</a></td>
            </tr>
        {% endfor %}
    </table>
</div>