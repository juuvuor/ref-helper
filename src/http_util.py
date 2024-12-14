""" Toteuttaa utility-funktiot ulkoisia rajapintoja varten. """
import requests


def http_get_url(url: str, mime_type = "text/html", timeout = 5000):
    """
    Hakee URL:ta vastaavan dokumentin halutussa formaatissa.
    :param mime_type: defaultisti text/html
    :returns: Muotoa: (MIME_TYPE, CONTENT),
    missä MIME_TYPE tulee response headerista content-type
    ja CONTENT payloadista
    """
    headers = {"accept": mime_type}
    res = requests.get(url, headers=headers, timeout=timeout)
    return (res.headers.get("content-type"), res.text)
