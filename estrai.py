import urllib.request
import bs4


url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")


doc = bs4.BeautifulSoup(text, "html.parser")
elems = doc.find_all("table")
table = elems[3]


for tr in table.contents[2:-2]:
    if isinstance(tr, bs4.element.Tag):
        tds = tr.contents

       
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".",""))
        kmq = float(tds[4].get_text().replace(",", "."))
        dens_tabella = float(tds[4].get_text().replace(",", "."))
        sigl = tds[7].get_text()
        print(f"{prov:25s} {resi:9d} {sigl} {kmq:8.2f} ")
        
        dens_calcolata = resi / kmq

      
        if abs(dens_calcolata - dens_tabella) > 0.1: 
            discrepanza = "DISCREPANZA!"
        else:
            discrepanza = ""

        
        print(f"{sigl:3s} {prov:25s} {resi:9d} {kmq:8.2f} {dens_calcolata:8.2f} {discrepanza}")
