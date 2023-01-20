from regxon.html import RegxonHTML
regxon_html = RegxonHTML()
regxon_html.excluded_attributes.update({
    'img': regxon_html.excluded_attributes['img'] + ['onerror'],
})
html = regxon_html.get_sanitized_content('<img onload="alert(1)" onerror="hey" src="http://example.com" /><script>alert(1)</script>')
