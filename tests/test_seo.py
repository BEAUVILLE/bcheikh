import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
URL="https://bcheikh.digiylyfe.com/"

class SeoTest(unittest.TestCase):
    def test_page(self):
        page=(ROOT/"index.html").read_text(encoding="utf-8")
        self.assertIn('<link rel="canonical" href="'+URL+'"/>',page)
        self.assertIn('name="robots" content="index,follow',page)
        self.assertIn('"@type":"Store"',page)
        self.assertIn("acces-proprietaire.html",page)
    def test_sitemap(self):
        root=ET.parse(ROOT/"sitemap.xml").getroot()
        self.assertEqual([x.text for x in root.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")],[URL])
    def test_robots(self):
        text=(ROOT/"robots.txt").read_text(encoding="utf-8")
        self.assertIn("Allow: /",text)
        self.assertIn("Sitemap: "+URL+"sitemap.xml",text)
if __name__=="__main__": unittest.main()
