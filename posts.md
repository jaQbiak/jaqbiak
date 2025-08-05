---
layout: default
permalink: /posts
nav_active: posts
---

<div id="content">
    {% for post in site.posts %}
        <table>
            <tr>
                <td>
                    <h2>{{ post.title }}</h2>
                    <small>{{ post.date | date: "%Y-%m-%d %H:%M" }}</small>
                </td>
            </tr>
            <tr>
                <td>{{ post.content }}</td>
            </tr>
        </table>
    {% endfor %}
</div>