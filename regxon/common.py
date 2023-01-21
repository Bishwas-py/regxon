import re
import typing


class Regxon:
    """
    General validation includes email, domain, url, phone and ipv4.
    """

    def is_email(self, email) -> typing.Union[re.Match, None]:
        """
        Validate email address.
        """

        email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}"
        return re.match(email_regex, email)

    def is_domain(self, domain) -> typing.Union[re.Match, None]:
        """
        Validate domain name without schema.
        """
        domain_regex = r'^[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}$'
        return re.match(domain_regex, domain)

    def is_http_domain(self, domain) -> typing.Union[re.Match, None]:
        domain_regex = re.compile(r'^(https?://)?(www\.)?([a-zA-Z0-9]+)\.([a-zA-Z0-9]+)')
        return re.match(domain_regex, domain)

    def is_url(self, url, schema='') -> typing.Union[re.Match, None]:
        """
        Validate url based on custom schema; `://abc.com` is counted as valid if schema is empty.
        """
        url_regex = r'^%s://[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}(:[0-9]+)?(/.*)?$' % schema
        return re.match(url_regex, url)

    def is_http_url(self, url) -> typing.Union[re.Match, None]:
        """
        Validate http url; http and https are counted as valid.
        """
        http_url_regex = r'^https?://[a-zA-Z0-9-]{3,255}\.[a-zA-Z0-9-.]{2,}(:[0-9]+)?(/.*)?$'
        return re.match(http_url_regex, url)

    def is_ipv4(self, ipv4, schema='') -> typing.Union[re.Match, None]:
        """
        Validate ipv4 based on schema.
        """
        ipv4_regex = r'^%s(\d{1,3}\.){3}\d{1,3}$' % schema
        return re.match(ipv4_regex, ipv4)

    def is_http_ip(self, ip) -> typing.Union[re.Match, None]:
        """
        Validate http ip.
        """
        http_ip_regex = r'^https?://(\d{1,3}\.){3}\d{1,3}(:[0-9]+)?(/.*)?$'
        return re.match(http_ip_regex, ip)

    def is_ipv6(self, ipv6) -> typing.Union[re.Match, None]:
        """
        Validate ipv6.
        """
        ipv6_regex = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
        return re.match(ipv6_regex, ipv6)

    def is_phone(self, phone) -> typing.Union[re.Match, None]:
        """
        Validate phone number.
        """
        phone_regex = r"^(\+\d{1,3}\s?)?((\(\d{3}\)\s?)|(\d{3})(\s|-?))" \
                      r"(\d{3}(\s|-?))(\d{4})(\s?(([E|e]xt[:|.|]?)|x|X)(\s?\d+))?$"
        return re.match(phone_regex, phone)
