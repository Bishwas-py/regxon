from regxon.html import RegxonHTML
from regxon.common import Regxon

regxon_html = RegxonHTML()
regxon_html.excluded_attributes.update({
    'img': regxon_html.excluded_attributes['img'] + ['onerror'],
})
html = regxon_html.get_sanitized_content('<img onload="alert(1)" onerror="hey" src="http://example.com" /><script>alert(1)</script>')
print(html)

regxon = Regxon()

email = regxon.is_email('bishwasbh@fmx.comx')
if email:
    print('Email is valid: ', email.string)
else:
    print('Email is invalid')

domain = regxon.is_domain('bishwasbh.com')
if domain:
    print('Domain is valid: ', domain.string)
else:
    print('Domain is invalid')

url = regxon.is_url('http://bishwasbh.com', 'http')
if url:
    print('Url is valid: ', url.string)
else:
    print('Url is invalid')

url = regxon.is_url('://abc.com', '')
if url:
    print('Url is valid: ', url.string)
else:
    print('Url is invalid')

ipv4 = regxon.is_ipv4('192.168.231.11')
if ipv4:
    print('IPv4 is valid: ', ipv4.string)
else:
    print('IPv4 is invalid')

ipv6 = regxon.is_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334')
if ipv6:
    print('IPv6 is valid: ', ipv6.string)
else:
    print('IPv6 is invalid')

invalid_ipv6 = regxon.is_ipv6('2001:0db8:85a3:0000:0000:8a2e:0370:7334:123')
if invalid_ipv6:
    print('IPv6 is valid: ', invalid_ipv6.string)
else:
    print('IPv6 is invalid')

phone = regxon.is_phone('+977-984-123-4567')
if phone:
    print('Phone is valid: ', phone.string)
else:
    print('Phone is invalid')