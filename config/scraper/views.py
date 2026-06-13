import subprocess
import json
import os
from django.shortcuts import render
from .models import Property
from properties.models import InternalProperty
from .forms import ScraperForm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SCRAPY_DIR = os.path.join(BASE_DIR, "..", "crawler")
OUTPUT_FILE = os.path.join(SCRAPY_DIR, "results.json")

def run_scraper(request):
    form = ScraperForm(request.POST or None)

    if request.method == "POST" and form.is_valid():

        data = form.cleaned_data
        internal_properties = InternalProperty.objects.filter(
            location=data.get("kota"),
            property_type=data.get("jual_sewa"),
            property_category=data.get("tipe"),
            status="active"
        )

        output_file = "../crawler/results.json"
        debug_file = "../crawler/debug_urls.json"

        # 🔥 delete old files (IMPORTANT)
        if os.path.exists(output_file):
            os.remove(output_file)

        if os.path.exists(debug_file):
            os.remove(debug_file)

        subprocess.run([
            "python", "-m", "scrapy",
            "crawl", "web_crawl",

            "-a", f"kota={data.get('kota','')}",
            "-a", f"wilayah={data.get('wilayah','')}",
            "-a", f"kata_kunci={data.get('kata_kunci','')}",

            "-a", f"jual_sewa={data.get('jual_sewa','')}",
            "-a", f"tipe={data.get('tipe','')}",

            "-a", f"min_harga={data.get('min_harga','')}",
            "-a", f"max_harga={data.get('max_harga','')}",

            "-a", f"min_luas_tanah={data.get('min_luas_tanah','')}",
            "-a", f"max_luas_tanah={data.get('max_luas_tanah','')}",

            "-a", f"min_luas_bangunan={data.get('min_luas_bangunan','')}",
            "-a", f"max_luas_bangunan={data.get('max_luas_bangunan','')}",

            "-O", "results.json"
        ], cwd=SCRAPY_DIR)

        # ===============================
        # ✅ LOAD SCRAPED DATA
        # ===============================
        scraped_data = []
        if os.path.exists(output_file):
            try:
                with open(output_file, "r", encoding="utf-8") as f:
                    scraped_data = json.load(f)
            except Exception as e:
                print("JSON ERROR:", e)

        # ===============================
        # ✅ LOAD DEBUG URLS
        # ===============================
        debug_urls = []
        if os.path.exists(debug_file):
            try:
                with open(debug_file, "r", encoding="utf-8") as f:
                    debug_urls = json.load(f)
            except Exception as e:
                print("DEBUG JSON ERROR:", e)

        Property.objects.all().delete()

        # for item in scraped_data:
        #     Property.objects.create(
        #         title=item.get("title"),
        #         price=item.get("price"),
        #         location=item.get("location"),
        #         link=item.get("link"),
        #         source=item.get("source")
        #     )

        return render(request, "scraper/results.html", {
            "internal_properties": internal_properties,
            "scraped_properties": scraped_data,
            "debug_urls": debug_urls,
            "form": form
        })

    return render(request, "scraper/run.html", {
        "form": form
    })