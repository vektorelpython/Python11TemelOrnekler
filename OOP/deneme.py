from OOP1 import HarfSayaci

sesli = HarfSayaci()
noktalama = HarfSayaci()
sessiz = HarfSayaci()
HarfSayaci.kelimesor()
noktalama.sesli_harfler = "*/-.;,:!'"
noktalama.mesaj = "Noktalama"
sesli.mesaj = "Sesli"
sessiz.mesaj = "Sessiz"
sessiz.sesli_harfler = "sdfghyrkljmncvbçxzğqwt"
sesli.calistir()
sessiz.calistir()
noktalama.calistir()
