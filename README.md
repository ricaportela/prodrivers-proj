mkdir proj-scrapy-prodrivers
git clone https://github.com/ricaportela/prodrivers-proj.git
pip install scrapy
scrapy shell 'https://www.prodrivers.com/jobs/?City=&State=Florida'