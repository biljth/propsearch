import scrapy
# import selenium
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import time
# from googletrans import Translator
import re

# jual_sewa = "sewa"
# kota = "tangerang"
# wilayah = ""
# tipe = "rumah"
# max_luas_tanah = "500"
# min_luas_tanah = "10"
# max_luas_bangunan = "500"
# min_luas_bangunan = "10"
# max_harga = "500000000"
# min_harga = "450000000"
# kata_kunci = ""

"https://halorumah.id/search-results/page/5/?status%5B0%5D=jual&keyword=tangerang&type%5B0%5D=rumah&max-area=1000&min-area=10&min-price=400000000&max-price=1000000"
"https://www.rumah123.com/jual/tangerang/rumah/?maxLandArea=1000&maxPrice=500000000&minLandArea=10&minPrice=100000000"
# rumah123_lease = f"{jual_sewa}/" if jual_sewa else ""
# rumah123_city = f"{kota}/"
# rumah123_type = f"{tipe}/?" if wilayah else f"{tipe}/?"
# rumah123_subdistrict = f"{wilayah}/" if wilayah else ""
# rumah123_max_land_area = f"maxLandArea={max_luas_tanah}&" if max_luas_tanah else ""
# rumah123_min_land_area = f"minLandArea={min_luas_tanah}&" if min_luas_tanah else ""
# rumah123_max_builtup_size = f"maxBuiltupSize={max_luas_bangunan}&" if max_luas_bangunan else ""
# rumah123_min_builtup_size = f"minBuiltupSize={min_luas_bangunan}&" if min_luas_bangunan else ""
# rumah123_max_price = f"maxPrice={max_harga}&" if max_harga else ""
# rumah123_min_price = f"minPrice={min_harga}&" if min_harga else ""
# rumah123_keyword = f"q={kata_kunci}" if kata_kunci else ""

# nineco_lease = f"{jual_sewa}/" if jual_sewa else ""
# nineco_city = f"{kota}/" if wilayah else f"{kota}?"
# nineco_type = f"{tipe}/"
# nineco_subdistrict = f"{wilayah}?" if wilayah else ""
# nineco_max_land_area = f"luas_tanah_maks={max_luas_tanah}&" if max_luas_tanah else ""
# nineco_min_land_area = f"luas_tanah_min={min_luas_tanah}&" if min_luas_tanah else ""
# nineco_max_builtup_size = f"luas_bangunan_maks={max_luas_bangunan}&" if max_luas_bangunan else ""
# nineco_min_builtup_size = f"luas_bangunan_min={min_luas_bangunan}&" if min_luas_bangunan else ""
# nineco_max_price = f"harga_maks={max_harga}&" if max_harga else ""
# nineco_min_price = f"harga_min={min_harga}&" if min_harga else ""
# nineco_keyword = ""

# lamudi_lease = f"{jual_sewa}/" if jual_sewa else ""
# lamudi_city = f"{kota}/" if kota else ""
# lamudi_type = f"{tipe}/" if tipe else ""
# lamudi_subdistrict = f"{wilayah}/" if wilayah else ""
# lamudi_min_price = f"min-price={min_harga}&" if min_harga else ""
# lamudi_max_price = f"max-price={max_harga}&" if max_harga else ""
# lamudi_min_area = f"minArea={min_luas_bangunan}&" if min_luas_bangunan else ""
# lamudi_max_area = f"maxArea={max_luas_bangunan}&" if max_luas_bangunan else ""
# lamudi_min_plot = f"minPlotArea={min_luas_tanah}&" if min_luas_tanah else ""
# lamudi_max_plot = f"maxPlotArea={max_luas_tanah}&" if max_luas_tanah else ""
# lamudi_currency = "priceCurrency=IDR&"
# lamudi_keyword = f"q={kata_kunci}&" if kata_kunci else ""

# pinhome_base = f"https://www.pinhome.id/{jual_sewa}/{tipe}?"
# pinhome_max_building = f"maxSpecifications.building_area={max_luas_bangunan}&" if max_luas_bangunan else ""
# pinhome_min_building = f"minSpecifications.building_area={min_luas_bangunan}&" if min_luas_bangunan else ""
# pinhome_max_land = f"maxSpecifications.surface_area={max_luas_tanah}&" if max_luas_tanah else ""
# pinhome_min_land = f"minSpecifications.surface_area={min_luas_tanah}&" if min_luas_tanah else ""
# pinhome_max_price = f"maxPrice={max_harga}&" if max_harga else ""
# pinhome_min_price = f"minPrice={min_harga}&" if min_harga else ""
# pinhome_keyword = f"q={kata_kunci}&" if kata_kunci else ""

# rumah123_url = ("https://www.rumah123.com/" + rumah123_lease + rumah123_city + rumah123_subdistrict +
#                 rumah123_type + rumah123_max_land_area + rumah123_min_land_area +
#                 rumah123_max_builtup_size + rumah123_min_builtup_size + rumah123_max_price +
#                 rumah123_min_price + rumah123_keyword)

# nineco_url = ("https://www.99.co/id/" + nineco_lease + nineco_type + nineco_city + nineco_subdistrict +
#               nineco_min_price + nineco_max_price + nineco_min_land_area + nineco_min_builtup_size +
#               nineco_max_builtup_size + nineco_max_land_area + nineco_keyword)

# lamudi_url = ("https://www.lamudi.co.id/" + lamudi_lease + lamudi_city + lamudi_subdistrict + lamudi_type + "?" + 
#               lamudi_min_price + lamudi_max_price + lamudi_currency + lamudi_min_area + lamudi_max_area + lamudi_min_plot + 
#               lamudi_max_plot + lamudi_keyword)

# pinhome_url = ( pinhome_base + pinhome_max_building + pinhome_min_building + pinhome_max_land + pinhome_min_land 
#                + pinhome_max_price + pinhome_min_price + pinhome_keyword).rstrip("&")

class WebScrape(scrapy.Spider):
    name = "web_crawl"
    rumah123_page_number = 1
    nineco_page_number = 1
    lamudi_page_number = 1
    pinhome_page_number = 1
    passhouse_page_number = 1
    

    def __init__(self, jual_sewa=None, kota=None, wilayah=None, tipe=None,
                 max_luas_tanah=None, min_luas_tanah=None,
                 max_luas_bangunan=None, min_luas_bangunan=None,
                 max_harga=None, min_harga=None, kata_kunci=None, *args, **kwargs):

        super().__init__(*args, **kwargs)

        # assign values (fallback if empty)
        self.jual_sewa = jual_sewa or ""
        self.kota = kota or ""
        self.wilayah = wilayah or ""
        self.tipe = tipe or ""
        self.max_luas_tanah = max_luas_tanah or ""
        self.min_luas_tanah = min_luas_tanah or ""
        self.max_luas_bangunan = max_luas_bangunan or ""
        self.min_luas_bangunan = min_luas_bangunan or ""
        self.max_harga = max_harga or ""
        self.min_harga = min_harga or ""
        self.kata_kunci = kata_kunci or ""

        # build URLs here (IMPORTANT)
        self.build_urls()
        self.debug_urls = []
    
    def clean_param(self, key, value):
        if value in [None, "", "None"]:
            return ""
        return f"{key}={value}&"    
    
    def build_urls(self):
        pinhome_city = ''
        passhouse_city = ''

        if self.kota == "dki-jakarta":
            pinhome_city = f"{self.tipe}/dki-jakarta"
            passhouse_city = f"jakarta"

        elif self.kota == "tangerang":
            pinhome_city = f"{self.tipe}/banten/tangerang"
            passhouse_city = f"{self.kota}/"

        elif self.kota == "tangerang-selatan":
            pinhome_city = f"{self.tipe}/banten/tangerang-selatan"
            passhouse_city = f"{self.kota}/"

        elif self.kota == "jakarta-selatan":
            pinhome_city = f"{self.tipe}/dki-jakarta/jakarta-selatan"
            passhouse_city = f"{self.kota}/"

        elif self.kota == "jakarta-barat":
            pinhome_city = f"{self.tipe}/dki-jakarta/jakarta-barat"
            passhouse_city = f"{self.kota}/"

        elif self.kota == "jakarta-timur":
            pinhome_city = f"{self.tipe}/dki-jakarta/jakarta-timur"
            passhouse_city = f"{self.kota}/"

        elif self.kota == "jakarta-utara":
            pinhome_city = f"{self.tipe}/dki-jakarta/jakarta-utara"
            passhouse_city = f"{self.kota}/"

        elif self.kota == "jakarta-pusat":
            pinhome_city = f"{self.tipe}/dki-jakarta/jakarta-pusat"
            passhouse_city = f"{self.kota}/"

        else:
            pinhome_city = f"{self.tipe}-di-{self.kota}"
            passhouse_city = f"{self.kota}/"
        
        pinhome_keyword = self.kata_kunci.lower().replace(" ", "+")
        passhouse_keyword = f"omnisearch={self.kata_kunci.lower().replace(" ", "+")}"

        rumah123_lease = f"{self.jual_sewa}/" if self.jual_sewa else ""
        rumah123_city = f"{self.kota}/"
        rumah123_type = f"{self.tipe}/?" if self.tipe else "" 
        rumah123_subdistrict = f"{self.wilayah}/" if self.wilayah else ""
        rumah123_max_land_area = self.clean_param("maxLandArea", self.max_luas_tanah)
        rumah123_min_land_area = self.clean_param("minLandArea", self.min_luas_tanah)
        rumah123_max_builtup_size = self.clean_param("maxBuiltupSize", self.max_luas_bangunan)
        rumah123_min_builtup_size = self.clean_param("minBuiltupSize", self.min_luas_bangunan)
        rumah123_max_price = self.clean_param("maxPrice", self.max_harga)
        rumah123_min_price = self.clean_param("minPrice", self.min_harga)
        rumah123_keyword = self.clean_param("q", self.kata_kunci)

        nineco_lease = f"{self.jual_sewa}/" if self.jual_sewa else ""
        nineco_city = f"{self.kota}/" if self.wilayah else f"{self.kota}?"
        nineco_type = f"{self.tipe}/" if self.tipe else ""
        nineco_subdistrict = f"{self.wilayah}?" if self.wilayah else ""
        nineco_max_land_area = self.clean_param("luas_tanah_maks", self.max_luas_tanah)
        nineco_min_land_area = self.clean_param("luas_tanah_min", self.min_luas_tanah)
        nineco_max_builtup_size = self.clean_param("luas_bangunan_maks", self.max_luas_bangunan)
        nineco_min_builtup_size = self.clean_param("luas_bangunan_min", self.min_luas_bangunan)
        nineco_max_price = self.clean_param("harga_maks", self.max_harga)
        nineco_min_price = self.clean_param("harga_min", self.min_harga)
        nineco_keyword = self.clean_param("q", self.kata_kunci)

        lamudi_lease = f"{self.jual_sewa}/" if self.jual_sewa else ""
        lamudi_city = f"{self.kota}/" if self.kota else ""
        lamudi_type = f"{self.tipe}/" if self.tipe else ""
        lamudi_subdistrict = f"{self.wilayah}/" if self.wilayah else ""
        lamudi_min_price = self.clean_param("min-price", self.min_harga)
        lamudi_max_price = self.clean_param("max-price", self.max_harga)
        lamudi_min_area = self.clean_param("minArea", self.min_luas_bangunan)
        lamudi_max_area = self.clean_param("maxArea", self.max_luas_bangunan)
        lamudi_min_plot = self.clean_param("minPlotArea", self.min_luas_tanah)
        lamudi_max_plot = self.clean_param("maxPlotArea", self.max_luas_tanah)
        lamudi_currency = "priceCurrency=IDR&"
        lamudi_keyword = ""

        pinhome_base = f"https://www.pinhome.id/{self.jual_sewa}/{pinhome_city}/?"
        pinhome_max_building = self.clean_param("maxSpecifications.building_area", self.max_luas_bangunan)
        pinhome_min_building = self.clean_param("minSpecifications.building_area", self.min_luas_bangunan)
        pinhome_max_land = self.clean_param("maxSpecifications.surface_area", self.max_luas_tanah)
        pinhome_min_land = self.clean_param("minSpecifications.surface_area", self.min_luas_tanah)
        pinhome_max_price = self.clean_param("maxPrice", self.max_harga)
        pinhome_min_price = self.clean_param("minPrice", self.min_harga)
        pinhome_keyword = self.clean_param("keyword", self.kata_kunci)

        passhouse_jual_sewa = {
            "jual": "dijual",
            "sewa": "disewa"
        }.get(self.jual_sewa, "dijual")
        passhouse_base = f"https://pashouses.id/{self.tipe}-{passhouse_jual_sewa}/area/"
        # passhouse_city = f"{self.kota}/"
        passhouse_min_price = f"?sortBy=recommendation&{self.clean_param("minPrice", self.min_harga)}"
        passhouse_max_price = self.clean_param("maxPrice", self.max_harga)
        passhouse_min_land = self.clean_param("minLandSize", self.min_luas_tanah)
        passhouse_max_land = self.clean_param("maxLandSize", self.max_luas_tanah)
        passhouse_min_building = self.clean_param("minBuildingSize", self.min_luas_bangunan)
        passhouse_max_building = self.clean_param("maxBuildingSize", self.max_luas_bangunan)
        
        self.rumah123_url = ("https://www.rumah123.com/" + rumah123_lease + rumah123_city + rumah123_subdistrict +
                rumah123_type + rumah123_max_land_area + rumah123_min_land_area +
                rumah123_max_builtup_size + rumah123_min_builtup_size + rumah123_max_price +
                rumah123_min_price + rumah123_keyword).rstrip("&")
        
        self.nineco_url = ("https://www.99.co/id/" + nineco_lease + nineco_type + nineco_city + nineco_subdistrict +
              nineco_min_price + nineco_max_price + nineco_min_land_area + nineco_min_builtup_size +
              nineco_max_builtup_size + nineco_max_land_area + nineco_keyword).rstrip("&")

        self.lamudi_url = ("https://www.lamudi.co.id/" + lamudi_lease + lamudi_city + lamudi_subdistrict + lamudi_type + "?" + 
                    lamudi_min_price + lamudi_max_price + lamudi_currency + lamudi_min_area + lamudi_max_area + lamudi_min_plot + 
                    lamudi_max_plot + lamudi_keyword).rstrip("&")

        self.pinhome_url = ( pinhome_base + pinhome_keyword + pinhome_max_building + pinhome_min_building + pinhome_max_land + pinhome_min_land 
               + pinhome_max_price + pinhome_min_price).rstrip("&")
        
        self.passhouse_url = ( passhouse_base + passhouse_city + passhouse_min_price + passhouse_max_price + passhouse_min_land +
                              passhouse_max_land + passhouse_min_building + passhouse_max_building + passhouse_keyword).rstrip("&")
        
    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }

        urls = [
            self.rumah123_url,
            self.nineco_url,
            self.lamudi_url,
            self.pinhome_url,
            self.passhouse_url
        ]

        for url in urls:
            if 'rumah123' in url:
                yield scrapy.Request(url, callback=self.rumah123) #, headers={'User-Agent': 'DataCrawl (https://www.rumah123.com)'})
            elif '99.co' in url:
                yield scrapy.Request(url, callback=self.nineco, headers=headers) #, headers={'User-Agent': 'DataCrawl (https://www.99.co/id)'})
            elif 'lamudi' in url:
                yield scrapy.Request(url, callback=self.lamudi)
            elif 'pinhome' in url:
                yield scrapy.Request(url, callback=self.pinhome)
            elif 'pashouses.id' in url:
                yield scrapy.Request(url, callback=self.passhouse)

        self.debug_urls.append(url)

    def rumah123(self, response):
        cards = response.css("div[data-test-id^='property-card']")

        for card in cards:
            title = card.css("h2::text").get()
            price = card.css("[data-testid='ldp-text-price']::text").get()
            location = card.css("p.text-greyText.text-sm::text").get()
            link = card.css("a[href*='/properti/']::attr(href)").get()

            if link:
                link = response.urljoin(link)

            data = {
                "title": title,
                "price": price,
                "location": location,
                "link": link,
                "source": "Rumah123"
            }

            yield data
        
        # Get all page numbers from pagination
        pages = response.css('[data-test-id="srp-pagination"] a::attr(aria-label)').getall()

        # Extract numbers like "Page 19"
        page_numbers = []
        for p in pages:
            match = re.search(r'Page (\d+)', p)
            if match:
                page_numbers.append(int(match.group(1)))

        max_page = max(page_numbers) if page_numbers else 1

        # Increment page
        WebScrape.rumah123_page_number += 1

        if WebScrape.rumah123_page_number <= max_page and WebScrape.rumah123_page_number <= 4:
            next_page = f"{self.rumah123_url}&page={WebScrape.rumah123_page_number}"
            self.logger.info(f"NEXT PAGE URL: {next_page}")

            yield response.follow(
                next_page,
                callback=self.rumah123,
            )
        else:
            self.logger.info("Reached last page. Stopping pagination.")

    def nineco(self, response):
        cards = response.css("div.cardSecondary__info-detail")

        for card in cards:
            title = card.css("h2::text").get(default="").strip()
            price = card.css(".price__tag strong::text").get(default="").strip()
            location = card.css("address::text").get(default="").strip()
            link = card.css("a[href*='/properti/']::attr(href)").get()

            if link:
                link = response.urljoin(link)

            data = {
                "title": title,
                "price": price,
                "location": location,
                "link": link,
                "source": "99.co"
            }

            yield data
        
        # Get all page numbers from pagination
        pages = response.css(".ui-atomic-pagination__page a::text").getall()
        page_numbers = [int(p) for p in pages if p.isdigit()]

        max_page = max(page_numbers) if page_numbers else 1

        WebScrape.nineco_page_number += 1
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://www.99.co/"
        }

        if WebScrape.nineco_page_number <= max_page and WebScrape.nineco_page_number <= 4:
            next_page = f"{self.nineco_url}&hlmn={WebScrape.nineco_page_number}"
            self.logger.info(f"NEXT PAGE URL: {next_page}")

            yield response.follow(
                next_page,
                callback=self.nineco,
                headers=headers,
                dont_filter=True
            )
        else:
            self.logger.info("Reached last page. Stopping pagination.")

    def lamudi(self, response):
        cards = response.css("div.snippet.js-snippet")

        for card in cards:
            title = card.css(".snippet__content__title::text").get(default="").strip()
            price = " ".join(card.css(".snippet__content__price::text").getall()).strip()            
            location = card.css('[data-test="snippet-content-location"]::text').get(default="").strip()
            link = card.css("a::attr(href)").get()

            if link:
                link = response.urljoin(link)

            data = {
                "title": title,
                "price": price,
                "location": location,
                "link": link,
                "source": "Lamudi"
            }

            yield data

        # Get max page from Lamudi pagination text
        page_text = response.css(".pagination__pages .sort-text::text").get(default="")
        match = re.search(r'dari\s+(\d+)', page_text)
        max_page = int(match.group(1)) if match else 1
        # Increment page
        WebScrape.lamudi_page_number += 1

        if WebScrape.lamudi_page_number <= max_page and WebScrape.lamudi_page_number <= 4:
            next_page = f"{self.lamudi_url}&page={WebScrape.lamudi_page_number}"
            self.logger.info(f"NEXT PAGE URL: {next_page}")

            yield response.follow(
                next_page,
                callback=self.lamudi,
            )
        else:
            self.logger.info("Reached last page. Stopping pagination.")

    def pinhome(self, response):
        
        cards = response.css("div[class^='pin-card__info']")

        for card in cards:
            title = card.css("h2 a::text").get()
            price = card.css("div[class^='pin-card__price']::text").get()
            location = card.css("div[class^='pin-card__location-info']::text").get()
            link = card.css("h2 a::attr(href)").get()

            if link:
                link = response.urljoin(link)

            data = {
                "title": title,
                "price": price,
                "location": location,
                "link": link,
                "source": "PinHome"
            }

            yield data
        
        #pagination
        pages = response.css("a.pin-pagination__number___ee5yp::text").getall()
        page_numbers = [int(p) for p in pages if p.isdigit()]
        max_page = max(page_numbers) if page_numbers else 1
        self.logger.info(f"MAX PAGE: {max_page}")

        WebScrape.pinhome_page_number += 1
        if WebScrape.pinhome_page_number <= max_page and WebScrape.pinhome_page_number <= 4:
            next_page = f"{self.pinhome_url}&page={WebScrape.pinhome_page_number}"
            print(next_page, "---------------------------------------------------------------------------------------------------------------------")

            self.logger.info(f"NEXT PAGE URL: {next_page}")

            yield response.follow(
                next_page,
                callback=self.pinhome,
            )
        else:
            self.logger.info("Reached last page. Stopping pagination.")
    
    def passhouse(self, response):

        print("=" * 50)
        print("PASSHOUSE URL:", response.url)

        property_count = response.xpath(
            "//span[contains(text(),'properti')]/text()"
        ).get()

        print("PROPERTY COUNT:", repr(property_count))

        no_result = response.css("p::text").getall()
        print("P TAGS:", no_result[:20])
    
        cards = response.css("a.w-full.bg-white.rounded-b-xl")
        print("CARDS FOUND:", len(cards))

        for card in cards:
            title = card.css("h2::text").get()
            price = card.css("span.ph-property-list__card-body__price::text").get()
            location = card.css("p.text-\\[\\#565757\\].my-2::text").get()

            link = card.attrib.get("href")

            if link:
                link = response.urljoin(link)

            data = {
                "title": title.strip() if title else None,
                "price": price.strip() if price else None,
                "location": location.strip() if location else None,
                "link": link,
                "source": "Passhouse"
            }

            yield data
        
        # Get all pagination numbers
        pages = response.css("nav[aria-label='Page navigation'] a::text").getall()

        # Keep only numeric pages
        page_numbers = [int(p.strip()) for p in pages if p.strip().isdigit()]

        max_page = max(page_numbers) if page_numbers else 1

        # Increment page number
        WebScrape.passhouse_page_number += 1

        if (
            WebScrape.passhouse_page_number <= max_page
            and WebScrape.passhouse_page_number <= 4
        ):

            # Example:
            # /rumah-dijual/area/jakarta/2
            next_page = f"{self.passhouse_url}/{WebScrape.passhouse_page_number}"

            self.logger.info(f"NEXT PAGE URL: {next_page}")

            yield response.follow(
                next_page,
                callback=self.passhouse,
            )

        else:
            self.logger.info("Reached last page. Stopping pagination.")

    def closed(self, reason):
        import json

        with open("debug_urls.json", "w") as f:
            json.dump(self.debug_urls, f, indent=2)

"""""
.\.venv\Scripts\Activate
python -m scrapy crawl web_crawl -a kota=jakarta -a min_harga=100000000 -a max_harga=500000000 -o results.json
python -m scrapy crawl web_crawl
https://www.rumah123.com/properti/tangerang/hos16629440/
https://halorumah.id/search-results/page/5/?status%5B0%5D=jual&keyword=tangerang&type%5B0%5D=rumah&max-area=1000&min-area=10&min-price=400000000&max-price=1000000
"""""