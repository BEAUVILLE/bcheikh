"""BCHEIKH : boutique et carte interactive à 10 langues (contrôles sans dépendances)."""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
HOME=(ROOT/"index.html").read_text(encoding="utf-8")
CARD=(ROOT/"carte/index.html").read_text(encoding="utf-8")
LANGS={"fr","en","es","pt","it","de","nl","ar","wo","zh"}

class TestTenLang(unittest.TestCase):
    def test_shop_has_all_ten_complete_dictionaries(self):
        start=HOME.index("const translations=")+len("const translations=")
        data,_=json.JSONDecoder().raw_decode(HOME[start:])
        self.assertEqual(set(data),LANGS)
        for lang in ("wo","zh"):
            self.assertEqual(set(data[lang]),set(data["fr"]))
            self.assertTrue(all(isinstance(v,str) and v.strip() for v in data[lang].values()))
            self.assertNotEqual(data[lang]["lead"],data["fr"]["lead"])
        opts=re.findall(r'<option value="([^"]+)"',HOME)
        self.assertEqual(set(opts),LANGS)
        self.assertIn('data-i18n="language">Langue</span><b>10</b>',HOME)
        self.assertIn('document.documentElement.lang=currentLang==="zh"?"zh-CN":currentLang',HOME)
        self.assertIn("const waveNumber=\"786523129\"",HOME)
        self.assertIn("const mainWhatsApp=\"221786523129\"",HOME)

    def test_living_card_same_languages_and_secure_owner(self):
        m=re.search(r'var TEXT=\{\s*wo:(\{.*?\}),\s*zh:(\{.*?\}),\s*fr:',CARD,re.S)
        self.assertIsNotNone(m)
        wo,zh=json.loads(m.group(1)),json.loads(m.group(2))
        self.assertEqual(set(wo),set(zh))
        self.assertEqual(len(wo),15)
        self.assertEqual(set(re.findall(r'<button class="lang[^"]*" type="button" data-lang="([^"]+)"',CARD)),LANGS)
        self.assertIn('document.documentElement.lang=lang===\'zh\'?\'zh-CN\':lang',CARD)
        self.assertIn("new URLSearchParams(location.search).get('lang')",CARD)
        self.assertIn('https://digiylyfe.com/acces-proprietaire.html',HOME)
        self.assertIn("var phone='+221771742749'",CARD)

    @unittest.skipUnless(shutil.which("node"),"Node not installed")
    def test_existing_owner_access_security(self):
        proc=subprocess.run(["node","--test","tests/bcheikh-owner-access-v1.test.cjs"],
             cwd=ROOT,check=False,capture_output=True,text=True)
        self.assertEqual(proc.returncode,0,proc.stderr+"\n"+proc.stdout)

if __name__=="__main__":
    unittest.main()
