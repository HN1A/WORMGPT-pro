import requests
import json

# عنوان URL
url = "https://api.deepai.org/hacking_is_a_serious_crime"

# الرؤوس (Headers) - تم استخراج الأساسيات من طلب cURL
headers = {
    "authority": "api.deepai.org",
    "accept": "*/*",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7,ms-MY;q=0.6,ms;q=0.5,en-AS;q=0.4",
    "api-key": "tryit-31416689943-feda26062a30168ad561f772328ea81e",
    "origin": "https://deepai.org",
    "user-agent": "Mozilla/5.0 (Linux; Android 15; SM-A145P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    # لا حاجة لتعيين content-type لأن مكتبة requests ستتعامل مع multipart/form-data تلقائياً عند استخدام معامل files
}

# الكوكيز (Cookies) - تم تحليلها من السلسلة الأصلية
"""cookies = {
    "_twpid": "tw.1782754008916.793310914789240582",
    "_ga": "GA1.1.1128210892.1782754010",
    "_gcl_au": "1.1.1765430159.1782754010",
    "_fbp": "fb.1.1782754010311.32770227927871532",
    "user_sees_ads": "true",
    "_ga_GY2GHX2J9Y": "GS2.1.s1783763426$o8$g1$t1783763454$j32$l0$h0"
"""

# بيانات النموذج (بصيغة multipart/form-data)
# نستخدم معامل files لفرض إرسال البيانات كـ multipart، مع تعيين القيمة كـ (None, 'القيمة') للحقول النصية
files = {
    "chat_style": (None, "chat"),
    "chatHistory": (None, '[{"role":"user","content":"hi"}]'),
    "model": (None, "llama-3.1-8b-instant"),
    "session_uuid": (None, "ebc664bb-dba4-4246-a6c9-82e8efd72f32"),
    "sensitivity_request_id": (None, "16435b0f-72fc-4a1c-aec9-c8c76252ffe1"),
    "hacker_is_stinky": (None, "very_stinky"),
    "enabled_tools": (None, '["image_generator","image_editor"]')
}

# تنفيذ الطلب (مع إضافة compression تلقائياً عبر requests)
response = requests.post(url, headers=headers,  files=files)

# طباعة النتيجة
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# إذا كان الرد بصيغة JSON، يمكنك طباعته بشكل منسق
try:
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))
except json.JSONDecodeError:
    pass
    