import re


class Regxon:
    """
    General validation includes email, domain, url, phone and ipv4.
    """

    def is_email(self, email) -> re.Match | None:
        """
        Validate email address.
        """

        email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}"
        return re.match(email_regex, email)

    def is_domain(self, domain) -> re.Match | None:
        """
        Validate domain name.
        """
        domain_regex = r'^[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}$'
        return re.match(domain_regex, domain)

    def is_url(self, url, schema='') -> re.Match | None:
        """
        Validate url based on schema; `://abc.com` is counted as valid if schema is empty.
        """
        url_regex = r'^%s://[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}(:[0-9]+)?(/.*)?$' % schema
        return re.match(url_regex, url)

    def is_http_url(self, url) -> re.Match | None:
        """
        Validate http url; http and https are counted as valid.
        """
        http_url_regex = r'^https?://[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}(:[0-9]+)?(/.*)?$'
        return re.match(http_url_regex, url)

    def is_ipv4(self, ipv4, schema='') -> re.Match | None:
        """
        Validate ipv4 based on schema.
        """
        ipv4_regex = r'^%s(\d{1,3}\.){3}\d{1,3}$' % schema
        return re.match(ipv4_regex, ipv4)

    def is_ipv6(self, ipv6) -> re.Match | None:
        """
        Validate ipv6.
        """
        ipv6_regex = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return re.match(ipv6_regex, ipv6)

    def is_phone(self, phone) -> re.Match | None:
        """
        Validate phone number.
        """
        phone_regex = r"^(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))" \
                      r"(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?$"
        return re.match(phone_regex, phone)

