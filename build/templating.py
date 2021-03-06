# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
"""Templating operations for the snippets created by the build script."""

from __future__ import unicode_literals


def build_with_template(trigger, title, body, full_href):
    """
    Template generation.

    With all args give, transform body with param list and return
    a complete snippet.
    """
    # print trigger
    # print body
    if (isinstance(body, list)):
        processed_body = """"${{1:-}}" : {}""".format((body[0]).text_content())
    else:
        processed_body = """"${{1:-}}" : {}""".format((body))

    template = """
    <!-- Auto-generated from {} -->
    <snippet>
        <content><![CDATA[{}]]></content>
        <!--Optional: Set a tabTrigger to define how to trigger the snippet-->
        <tabTrigger>{}</tabTrigger>
        <!--Optional: Set a scope to limit where the snippet will trigger-->
        <scope>source.cloudformation</scope>
    </snippet>
    """.format(full_href, processed_body, title)

    transformed_template = transform(template)

    return transformed_template


def transform(template):
    """Transform the template to adapt the parameters of the template."""
    return template \
        .replace('JSON object', '[]') \
        .replace(': String', '""') \
        .replace(': Integer', '') \
        .replace(': Boolean', '${true | false}')
