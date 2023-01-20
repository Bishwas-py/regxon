# RegXon
RegXon is a powerful validator, sanitizer and content parser that you're searching for decades.

## Installation
```bash
pip install regxon
```

## Usage

```python
from regxon.common import Regxon
regxon = Regxon()
```
## General Validation
General validation includes email, domain, url and ipv4.

### Validate Email

```python
from regxon.common import Regxon

regxon = Regxon()
regxon.is_email('xyz@.com')  # None
regxon.is_email('xyz@cpx.com')  # returns a proper Match object; you can grab the match with `.string`
```

### Validate Domain

```python
from regxon.common import Regxon

regxon = Regxon()
regxon.is_domain('xyzcom')  # None
regxon.is_domain('xyz.com')  # returns a proper Match object; you can grab the match with `.string`
```

### Validate URL

```python
from regxon.common import Regxon

regxon = Regxon()
regxon.is_url('xyz.com')  # None
regxon.is_url('https://xyz.com')  # returns a proper Match object
```

### Validate HTTP URL

```python
from regxon.common import Regxon

regxon = Regxon()
regxon.is_http_url('xyz.com')  # None; returns None if the url is not http
regxon.is_http_url('ftp://xyz.com')  # None; returns None if the url is not http
regxon.is_http_url('http://django.c') # None; returns None because `.c` is not a valid domain 
regxon.is_http_url('https://xyz.com')  # returns a proper Match object; you can grab the match with `.string`
```

### Validate IP

```python
from regxon.common import Regxon

regxon = Regxon()

# 1, 2 both are same and return a proper Match, as default schema is ""
regxon.is_ipv4('127.0.0.1')                 # 1
regxon.is_ipv4('127.0.0.1', schema='')      # 2; matches because 127.0.0.1 has no schema

regxon.is_ipv4('http://127.0.0.1')  # returns None as schema is not matched; "http" != ""
regxon.is_ipv4('http://127.0.0.1', schema='')  # returns None as schema is not matched; "http" != ""

regxon.is_ipv4('http://127.0.0.1', schema='http')  # returns a proper Match
regxon.is_ipv4('https://127.0.0.1', schema='http')  # returns None as schema is not matched; "https" != "http"
```

### Validate Phone Number

```python
from regxon.common import Regxon

regxon = Regxon()
regxon.is_phone('+91 1234567890')  # returns a proper Match object; you can grab the match with `.string`
```

## HTML Sanitization and Validation
RegXon provides a powerful HTML sanitizer and validator that you're searching for decades. 
It's a combination of [html5lib](https://pypi.org/project/html5lib/) and
[beautifulsoup4](https://pypi.org/project/beautifulsoup4/).

You "how to remove an attribute from HTML tag" problem is solved now. Or
another problem of "how to remove a tag from HTML" is also solved.

```python
from regxon.html import RegxonHTML

regxon_html = RegxonHTML()
html_content = """
<img onload="alert(1)" onerror="hey" src="http://example.com" />
<script>alert(1)</script>
"""
html = regxon_html.get_sanitized_content(html_content)

print(html)
```

The above code will print the following output

```html
<img onerror="hey"/>
```

### Add custom excluded attributes for any tag you want

```python
from regxon.html import RegxonHTML

regxon_html = RegxonHTML()
html_content = """
<img onload="alert(1)" onerror="hey" src="http://example.com" />
<script>alert(1)</script>
"""

# Add custom excluded attributes for any tag you want
regxon_html.excluded_attributes.update({
    'img': regxon_html.excluded_attributes['img'] + ['onerror'],
})
```

The above code will print the following output
```html
<img/>
```

## Purpose of RegXon
-[x] Sanitize HTML; remove unwanted tags and attributes; XSS prevention
-[x] Validate IP, URL, Domain; SSRF prevention
-[x] Validate Email; Email spoofing prevention
-[x] Validate Phone Number; Phone number spoofing prevention


## License
[MIT](https://choosealicense.com/licenses/mit/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors
- [Bishwas Bhandari](https://github.com/bishwas-py) from [Webmatrices](https://webmatrices.com)

## Acknowledgements
- [html5lib](https://pypi.org/project/html5lib/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [RegExr](https://regexr.com/)
