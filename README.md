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
regxon.is_email('xyz@.com') # False
regxon.is_email('xyz@cpx.com') # True
```

### Validate Domain
```python
from regxon.common import Regxon
regxon = Regxon()
regxon.is_domain('xyzcom') # False
regxon.is_domain('xyz.com') # True
```

### Validate URL
```python
from regxon.common import Regxon
regxon = Regxon()
regxon.is_url('xyz.com') # False
regxon.is_url('https://xyz.com') # True
```

### Validate IP
```python
from regxon.common import Regxon
regxon = Regxon()
regxon.is_ipv4('http://xxz.com') # False
regxon.is_ipv4('http://127.0.0.1') # True
regxon.is_ipv4('127.0.0.1', schema='') # True
regxon.is_ipv4('http://127.0.0.1', schema='') # False
```

### Validate Phone Number
```python
from regxon.common import Regxon
regxon = Regxon()
regxon.is_phone('+91 1234567890') # True
```

## HTML Sanitization and Validation
HTML Validation includes validation of 

```python
from regxon.html import RegxonHTML
regxon_html = RegxonHTML()
html_content = """
<img onload="alert(1)" onerror="hey" src="http://example.com" />
<script>alert(1)</script>
"""
html = regxon_html.get_sanitized_content(html_content)
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

Returned HTML will be
```html
<img/>
```