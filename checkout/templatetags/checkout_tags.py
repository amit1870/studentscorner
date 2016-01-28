from django import template
register = template.Library()

@register.inclusion_tag("catalog/tags/form_table_row.html")
def form_table_row(form_field):
	return {'form_field':form_field}








# 274406