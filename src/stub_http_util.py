"""
Toteuttaa testausta varten http_util tyngän
"""


mappings = {
    "http://dx.doi.org/10.1145/2380552.2380613|application/x-bibtex": """
@inproceedings{Luukkainen_2012,
    author = "Luukkainen, Matti and Vihavainen, Arto and Vikberg, Thomas",
    series = "SIGITE ’ 12",
    title = "Three years of design-based research to reform a software engineering curriculum",
    url = "http://dx.doi.org/10.1145/2380552.2380613",
    DOI = "10.1145/2380552.2380613",
    booktitle = "Proceedings of the 13th annual conference on Information technology education",
    publisher = "ACM",
    year = "2012",
    month = "October",
    pages = "209–214",
    collection = "SIGITE ’ 12"
}
"""
}


def http_get_url(url: str, mime_type = "text/html", timeout = 5000):
    """
    Hakee URL:ta ja mime_typeä vastaavan dokumentin halutussa formaatissa.
    :param mime_type: defaultisti text/html
    :returns: Muotoa: (MIME_TYPE, CONTENT)
    """
    return mappings.get(url + "|" + mime_type)
