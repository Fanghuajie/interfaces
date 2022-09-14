
from requests_html import HTMLSession

class TestGetLink:

    def __init__(self):
        pass

    def get_text_link_from_sel(url, sel):
        """
        :param url:
        :param sel:
        :return:
        """
        my_list = []
        try:
            session = HTMLSession()
            r = session.get(url)
            results = r.html.find(sel)
            for result in results:
                my_text = result.text
                my_link = list(result.absolute_links)[0]
                my_list.append((my_text, my_link))
            return my_list
        except IOError:
            return None
