import json
import pandas as pd

null = ""
data = [
    {
        "uid": "1675836612299_61064",
        "askiKodu": "6DAFH",
        "yapi_kimlik_no": "131817678",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Akpınar_Merkez",
        "sokak": "512<Br>Susam",
        "binaNo": "512 SOKAK NO: 3<br>SUSAM SOKAK NO: 19A",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": [
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52150454",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52150453",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52150452",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52150455"
        ]
    },
    {
        "uid": "1676013351697_8573",
        "askiKodu": "8YDPM",
        "yapi_kimlik_no": "134390798",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Aksaray",
        "sokak": "Mustafa İspir",
        "binaNo": "MUSTAFA İSPİR SOKAK NO: 39<br>MUSTAFA İSPİR SOKAK NO: 39/1",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": [
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52318358",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52318344",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52318353",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52318343",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52318349"
        ]
    },
    {
        "uid": "1675948811779_18709",
        "askiKodu": "F72ZU",
        "yapi_kimlik_no": "129374294",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Çarşı_Merkez",
        "sokak": "Dar<Br>Hürriyet",
        "binaNo": "DAR SOKAK NO: 1A<br>DAR SOKAK NO: 1<br>HÜRRİYET SOKAK NO: 42B<br>HÜRRİYET SOKAK NO: 42C<br>HÜRRİYET SOKAK NO: 42A",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": [
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52282585",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52268906",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52268943",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52269081",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52269101",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52275262"
        ]
    },
    {
        "uid": "1677833878034_42008",
        "askiKodu": "P3UB2",
        "yapi_kimlik_no": "139685820",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Çarşı_Merkez",
        "sokak": "Hürriyet",
        "binaNo": "HÜRRİYET SOKAK NO: 66<br>HÜRRİYET SOKAK NO: 66A<br>HÜRRİYET SOKAK NO: 66B",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677927936667_62309",
        "askiKodu": "26C78",
        "yapi_kimlik_no": null,
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Çarşı_Merkez",
        "sokak": "Hürriyet Sokak",
        "binaNo": "HÜRRİYET SOKAK NO: 72",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677854078045_26843",
        "askiKodu": "6N4J2",
        "yapi_kimlik_no": "125885780",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Çarşı_Merkez",
        "sokak": "Kutlu Sokak",
        "binaNo": "Kutlu SOKAK NO: 37",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677852178937_17098",
        "askiKodu": "Z3FHR",
        "yapi_kimlik_no": "138784756",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Çarşı_Merkez",
        "sokak": "Kutlu Sokak",
        "binaNo": "Kutlu SOKAK NO: 39",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677524205929_63078",
        "askiKodu": "UKVZF",
        "yapi_kimlik_no": "121128375",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Gümüş Kavak",
        "sokak": "Ara Sokak Sokak",
        "binaNo": "Ara sokak SOKAK NO: 6",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677523857279_21536",
        "askiKodu": "UC4B2",
        "yapi_kimlik_no": null,
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Gümüş Kavak",
        "sokak": "Arif Sokak Sokak",
        "binaNo": "Arif sokak SOKAK NO: 10",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677523857279_21536",
        "askiKodu": "UC4B2",
        "yapi_kimlik_no": null,
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Gümüş Kavak",
        "sokak": "Arif Sokak Sokak",
        "binaNo": "Arif sokak SOKAK NO: 10",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677524466196_33009",
        "askiKodu": "8ZH88",
        "yapi_kimlik_no": null,
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Gümüş Kavak",
        "sokak": "Arif Sokak Sokak",
        "binaNo": "Arif sokak SOKAK NO: 16",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677419075040_40514",
        "askiKodu": "YTVNF",
        "yapi_kimlik_no": "130284029",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Gümüş Kavak",
        "sokak": "Hikmet<Br>Sivrice",
        "binaNo": "HİKMET SOKAK NO: 10<br>SİVRİCE SOKAK NO: 49",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677419208587_67018",
        "askiKodu": "BCV3H",
        "yapi_kimlik_no": "139909063",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Gümüş Kavak",
        "sokak": "Sivrice",
        "binaNo": "SİVRİCE SOKAK NO: 47",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677749408094_61873",
        "askiKodu": "82YHM",
        "yapi_kimlik_no": "131774820",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Kızılay",
        "sokak": "Uluova",
        "binaNo": "ULUOVA SOKAK NO: 14",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677747982962_71296",
        "askiKodu": "RHHN8",
        "yapi_kimlik_no": "131706194",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Kızılay",
        "sokak": "Uluova",
        "binaNo": "ULUOVA SOKAK NO: 8",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1675782183802_20431",
        "askiKodu": "GV7U8",
        "yapi_kimlik_no": "123545717",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Merkez",
        "mahalle": "Nail Bey",
        "sokak": "Yenice Sokak",
        "binaNo": "YENİCE SOKAK NO: 3",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": [
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52680060",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52680285",
            "https://hasartespitresim.csb.gov.tr/images/1000/50/files/52679899"
        ]
    },
    {
        "uid": "1677403251563_84986",
        "askiKodu": "RAVEP",
        "yapi_kimlik_no": "173223462",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Alacakaya",
        "mahalle": "Sularbaşı",
        "sokak": "Sularbaşı",
        "binaNo": "SULARBAŞI SOKAK NO: 70",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677577113439_83852",
        "askiKodu": "4KAFR",
        "yapi_kimlik_no": "179148994",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Alacakaya",
        "mahalle": "Sularbaşı",
        "sokak": "Sularbaşı",
        "binaNo": "SULARBAŞI SOKAK NO: 93",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678181987477_85492",
        "askiKodu": "3DYTN",
        "yapi_kimlik_no": "185437035",
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Kovancılar",
        "mahalle": "Topağaç Güneşli",
        "sokak": "Topağaç",
        "binaNo": "TOPAĞAÇ SOKAK NO: 41",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677669481855_25432",
        "askiKodu": "F7NKB",
        "yapi_kimlik_no": "184833952",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Baskil",
        "mahalle": "Altınuşağı Şahinler",
        "sokak": "Dallıca",
        "binaNo": "DALLICA SOKAK NO: 12",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677666746395_27586",
        "askiKodu": "2P47J",
        "yapi_kimlik_no": "199461450",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Baskil",
        "mahalle": "Altınuşağı Şahinler",
        "sokak": "Doğanlar",
        "binaNo": "DOĞANLAR SOKAK NO: 5",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678112775118_7014",
        "askiKodu": "MM3GT",
        "yapi_kimlik_no": "171554413",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Çan",
        "sokak": "Çan",
        "binaNo": "ÇAN SOKAK NO: 13",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678098958435_82889",
        "askiKodu": "46EGD",
        "yapi_kimlik_no": "172429490",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Çan",
        "sokak": "Çan",
        "binaNo": "ÇAN SOKAK NO: 60",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678098787897_56038",
        "askiKodu": "MYVK8",
        "yapi_kimlik_no": "178869616",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Çan",
        "sokak": "Çan",
        "binaNo": "ÇAN SOKAK NO: 66",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678265486124_51824",
        "askiKodu": "6EZZ4",
        "yapi_kimlik_no": "171593874",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Kuşbayırı Kubatlı",
        "sokak": "Kubatlı",
        "binaNo": "KUBATLI SOKAK NO: 50",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678263345665_91597",
        "askiKodu": "HZCHG",
        "yapi_kimlik_no": "170263495",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Kuşbayırı Kubatlı",
        "sokak": "Kubatlı",
        "binaNo": "KUBATLI SOKAK NO: 65",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678267539989_33028",
        "askiKodu": "N7ABY",
        "yapi_kimlik_no": "null",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Kuşbayırı Kubatlı",
        "sokak": "Kuşbayırı Köyü Kubatlı Mezrası Sokak",
        "binaNo": "Kuşbayırı köyü kubatlı mezrası SOKAK NO: 29",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678451336161_46349",
        "askiKodu": "DYNKA",
        "yapi_kimlik_no": "172065419",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Pilavtepe",
        "sokak": "Pilavtepe Köyü Sokak",
        "binaNo": "Pilavtepe köyü SOKAK NO: 12",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1678453185874_99222",
        "askiKodu": "FZCDU",
        "yapi_kimlik_no": "177981446",
        "yapi_kimlik_no_kaynak_adi": "null",
        "il": "Elazığ",
        "ilce": "Karakoçan",
        "mahalle": "Pilavtepe",
        "sokak": "Pilavtepe Köyü Sokak",
        "binaNo": "Pilavtepe Köyü SOKAK NO: 16",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": "null",
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677326037034_59882",
        "askiKodu": "VKCZP",
        "yapi_kimlik_no": null,
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Arıcak",
        "mahalle": "Serinevler",
        "sokak": "404 Sokak",
        "binaNo": "404 SOKAK NO: 0",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    },
    {
        "uid": "1677325528892_29494",
        "askiKodu": "7BHB3",
        "yapi_kimlik_no": null,
        "yapi_kimlik_no_kaynak_adi": null,
        "il": "Elazığ",
        "ilce": "Arıcak",
        "mahalle": "Serinevler",
        "sokak": "404 Sokak",
        "binaNo": "404 SOKAK NO: 46",
        "aciklama": "Acil Yıktırılacak",
        "itirazSonucu": null,
        "deprem_adi": "Kahramanmaraş Pazarcık",
        "deprem_siddeti": "7.7",
        "deprem_tarihi": "06/02/2023",
        "fotograflar": []
    }
]

# JSON verilerini Pandas DataFrame'e dönüştür
df = pd.DataFrame(data)

# Excel dosyasına yaz
df.to_excel("acil-yikilacak-elazig.xlsx", index=False)


# null = "null"
# for i in data:
#     s=dict(data[i])
#     il=s['il']
#     ilce=s['ilce']
#     mahalle = s['mahalle']
#     dosya_adi = f"{il}-{ilce}-{mahalle}.xlsx"
#     df = pd.DataFrame(data)
#     df.to_excel(dosya_adi, index=False)