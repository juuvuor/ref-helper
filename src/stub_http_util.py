"""
Toteuttaa testausta varten http_util tyngän
"""

from robot.api.deco import keyword

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

@keyword("Http Get Url")
def http_get_url(url: str, mime_type="text/html", timeout=5000):
    """
    Hakee URL:ta ja mime_typeä vastaavan dokumentin halutussa formaatissa.
    :param mime_type: defaultisti text/html
    :returns: Muotoa: (MIME_TYPE, CONTENT)
    """
    result = mappings.get(url + "|" + mime_type)
    if result is None:
        raise RuntimeError(f"No mapping found for URL")
    return "application/x-bibtex", result
