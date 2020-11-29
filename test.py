import xml.etree.ElementTree as ET
urls = [
    "https://www.yahoo.co.jp/",
    "https://www.google.com/",
    "https://www.facebook.com/",
    "https://twitter.com/",
    "https://paymap.jp",
]

urlset = ET.Element('urlset')
urlset.set("xmlns", "http://www.sitemaps.org/schemas/sitemap/0.9")
tree = ET.ElementTree(element=urlset)


for url in urls:
    url_element = ET.SubElement(urlset, 'url')
    loc = ET.SubElement(url_element, 'loc')
    loc.text = url
    lastmod = ET.SubElement(url_element, 'lastmod')
    lastmod.text = "2019-01-12"

tree.write('sitemap.xml', encoding='utf-8', xml_declaration=True)

