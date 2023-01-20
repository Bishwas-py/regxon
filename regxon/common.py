import re


class Regxon:
    """
    General validation includes email, domain, url, phone and ipv4.
    """

    def is_email(self, email):
        """
        Validate email address.
        """
        return re.match(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', email)

    def is_domain(self, domain):
        """
        Validate domain name.
        """
        return re.match(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$', domain)

    def is_url(self, url, schema):
        """
        Validate url based on schema.
        """
        return re.match(r'^%s://[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+(:[0-9]+)?(/.*)?$' % schema, url)

    def is_ipv4(self, ipv4, schema=''):
        """
        Validate ipv4 based on schema.
        """
        return re.match(r'^%s://[0-9]+(\.[0-9]+){3}(:[0-9]+)?(/.*)?$' % schema, ipv4)

    def is_phone(self, phone, prefix=''):
        """
        Validate phone number.
        ```
        regxon.is_phone('+91 1234567890') # True
        regxon.is_phone('+91 1234567890', prefix='') # False
        regxon.is_phone('+91 1234567890', prefix='+91') # True
        ```
        """
        return re.match(r'^%s[0-9]{10}$' % prefix, phone)
