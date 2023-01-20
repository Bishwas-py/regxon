from bs4 import BeautifulSoup


class RegxonHTML:
    excluded_tags = [
        'script'
    ]

    excluded_attributes = {
        'img': ['onload', 'src'],
    }

    def __init__(self, excluded_tags=None, excluded_attributes=None):
        if excluded_tags:
            self.excluded_tags = excluded_tags
        if excluded_attributes:
            self.excluded_attributes = excluded_attributes

    def get_sanitized_content(self, html):
        """
        Validate html.
        """
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all():
            if tag.name in self.excluded_tags:
                tag_soup = BeautifulSoup(str(tag), 'html.parser')
                print(tag_soup.new_string(''))
                tag.replace_with(tag_soup.new_string(''))

            if tag.name in self.excluded_attributes.keys():
                for attribute in self.excluded_attributes[tag.name]:
                    if tag.has_attr(attribute):
                        del tag[attribute]

        return soup.prettify()
