from fastapi import FastAPI
from search import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
async def main(query:str = None):
    korpus = {
        "BSU Kemnaker: Pengertian, Cara Cek Daftar Penerima, dan Proses Pencairan": '''
        Dilansir dari CNBC, BSU Kemnaker atau Bantuan Subsidi Upah dari Kementerian Ketenagakerjaan tahap I tahun 2022 sudah mulai disalurkan sejak Senin, 12 September 2022.

Besaran BSU yang dapat diberikan untuk para pekerja adalah sebesar Rp600.000 per bulan.

Program ini merupakan lanjutan dari program subsidi serupa tahun 2021 namun dengan skema dan nominal bantuan yang berbeda.

Siapa sajakah yang berhak mendapatkan BSU dan bagaimana cara mencairkannya?

Pelajari selengkapnya dari rangkuman Glints berikut!
        ''',
        "Harga BBM Naik, Ini Dampak bagi Pekerja dan 5 Cara Menghadapinya": '''
            Pemerintah mengumumkan bahwa harga BBM resmi naik terhitung sejak hari Sabtu, tanggal 3 September 2022.

Dilansir dari Kompas, harga Pertalite naik dari Rp7.650 per liter menjadi Rp10.000 per liter. Selain itu, harga solar bersubsidi juga naik menjadi Rp6.800 per liter dari harga sebelumnya Rp5.150.

Pertamax nonsubsidi juga tak luput dari kenaikan harga dari Rp12.500 per liter menjadi Rp14.500 per liter.

Kenaikan harga BBM ini tentunya memiliki dampak hampir ke seluruh lapisan masyarakat, tak terkecuali kaum pekerja.

Apa yang menyebabkan harga BBM naik di saat harga minyak dunia turun?

Lalu, apa yang bisa dilakukan kita sebagai pekerja untuk menghadapi kenaikan harga BBM ini?

Yuk, baca pembahasan dari Glints berikut ini!
        ''',
        "Job Hopping: Pengertian, Kelebihan, Kekurangan, dan Pertimbangannya": '''Job hopping adalah fenomena sering berpindah kerja yang sering terjadi di kalangan karyawan muda saat ini.

Ada yang mengatakan bahwa hal ini berdampak buruk untuk karier. Namun, banyak juga yang menganggap hal ini perlu dilakukan.

Uniknya, job hopping lebih sering dilakukan oleh kalangan pekerja yang lebih muda seperti generasi milenial.

Jika diperhatikan, karyawan senior atau baby boomer dapat bekerja di sebuah perusahaan dengan jangka waktu yang panjang.

Jadi, apakah job hopping itu? Mengapa bisa terjadi fenomena seperti ini?

Berikut ulasan dari Glints mengenai fenomena job hopping!

''',
        "Panduan Work from Anywhere: Mengenal WFA, Tren, dan Tips Suksesnya": '''Pandemi Covid-19 telah memaksa dunia kerja untuk beradaptasi, salah satunya adalah lewat work from anywhere (WFA). Seiring dengan menurunnya wabah, sistem ini diprediksi akan tetap merebak.

WFA sendiri adalah cara bagi karyawan untuk bisa bebas memilih lokasi kerja dan mengatur work-life balance-nya lebih baik.

Tentunya, perubahan ini juga dapat dilihat di Indonesia. Berdasarkan data Glints, terjadi pertumbuhan pesat lowongan kerja WFA sejak awal 2020 hingga Maret 2022:

fakta wfa glints

Hal ini menunjukkan bahwa peluang kerja dengan sistem WFA terbuka lebar untukmu.

Penasaran seperti apa tren work from anywhere di Indonesia? Mau tahu cara mendapatkan beragam pekerjaannya?
        ''',
        "Panduan dan Tips Sukses Negosiasi Gaji (Plus Template Latihan Gratis)": '''Pada Maret 2022, Glints melakukan survei tentang kebiasaan para follower Glints mengenai negosiasi gaji.

Polling terhadap 514 responden di akun Instagram @glintsid menunjukkan bahwa:

75% followers melakukan negosiasi gaji saat melamar kerja
25% followers tidak negosiasi gaji saat melamar kerja
Saat ini, kamu termasuk yang mana?

Baik yang sudah berani negosiasi gaji maupun yang belum, panduan Glints ini sama-sama wajib kamu baca.

Pasalnya, negosiasi gaji tidak bisa dilakukan sembarangan.

Yuk, pelajari bagaimana opini langsung dari pakar di bidang HR tentang negosiasi gaji, etika melakukannya, serta tips-tipsnya. Hal ini agar kamu dapat meyakinkan rekruter dengan baik saat proses rekrutmen.
 ''',
        "Customer Obsession: Arti, Manfaat, dan Cara Membangunnya": '''Supaya konsumen setia dan hanya ingin membeli suatu produk atau layanan yang ditawarkan brand-mu, maka hal utama yang harus dibentuk adalah customer obsession.

Hal ini didasari oleh rasa kesukaan dan kepercayaan mereka terhadap brand, produk, atau layanan dari perusahaan.

Tentu, hal tersebut memberikan keuntungan besar bagi perusahaan.

Adanya obsesi dari seorang konsumen membuat perusahaan tidak perlu terlalu khawatir mereka akan berpaling ke kompetitor.

Nah, berikut Glints beri penjelasan singkat seputar obsesi konsumen kepadamu. Simak artikelnya berikut ini, ya.
        ''',
    }
    result = getDataSearch(korpus, query)

    return {"result": result}