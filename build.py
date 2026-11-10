#!/usr/bin/env python3
"""Builds index.html (English) and vi/index.html (Vietnamese) from the CONTENT below.

Edit text here, then run:  python3 build.py
Both pages share one layout, so they always stay in sync. Text may contain HTML.
"""
import json
from pathlib import Path

SITE = "https://ds-kell.github.io"
GH = "https://github.com/ds-kell"
REPO = {"notify": "fix-noti-xiaomi", "convert": "convert-multi-file", "clicker": "kell-auto-clicker"}
PAYPAL = "https://paypal.me/truyennt"
BANK = ("VietinBank", "NGUYEN TUAN TRUYEN", "106879464361")

ICONS = {
    "notify": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 1 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/><path d="M19 3l1.5-1.5M5 3 3.5 1.5"/></svg>',
    "convert": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 0 1 15.5-6.2L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15.5 6.2L3 16"/><path d="M3 21v-5h5"/></svg>',
    "clicker": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 9l5 12 1.8-5.2L21 14Z"/><path d="M7.2 2.2 8 5.1M5.1 8l-2.9-.8M14 4.1 12 6.2M6.2 12l-2.1 2"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 8h1a4 4 0 1 1 0 8h-1"/><path d="M3 8h14v9a4 4 0 0 1-4 4H7a4 4 0 0 1-4-4Z"/><path d="M6 2v2M10 2v2M14 2v2"/></svg>',
    "download": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 10 5 5 5-5"/><path d="M5 21h14"/></svg>',
}
CURRENT = ' aria-current="true"'
ACCENT = {"notify": "a-orange", "convert": "a-blue", "clicker": "a-violet"}

CONTENT = {
  "en": {
    "path": "", "html_lang": "en", "og_locale": "en_US", "currency": "USD",
    "title": "Fix Xiaomi Notification Delay, Free File Converter &amp; Auto Clicker | ds-kell",
    "description": "Free open-source apps: HyperNotifyFix fixes late notifications on Xiaomi HyperOS/MIUI and puts Gemini, ChatGPT or Claude on the power button, without root; ConvertApp converts images, PDF, Word, Excel offline; Kell Auto Clicker records and replays mouse and keyboard.",
    "og_title": "Free tools: Xiaomi notification fix, file converter, auto clicker",
    "og_description": "No root, no ads, no account. Download for Android, Windows, macOS and Linux.",
    "nav": {"apps": "Apps", "support": "Support", "donate": "Buy me a coffee"},
    "cta_apps": "See the apps", "cta_donate": "Buy me a coffee",
    "after_download": "Saved you some time? <a href=\"#support\">Buy me a coffee ☕</a>",
    "pills": ["100% free", "Open source", "No ads", "No account"],
    "h1": "Small free tools that <em>just fix it</em>",
    "lead": "Fix late notifications on Xiaomi, convert files without uploading them, and automate repetitive clicks. Nothing is sent anywhere.",
    "go": "How to install →", "install": "How to install", "features": "What it does",
    "download_for": "Download", "source": "Source code", "your_system": "Your system",
    "apps": {
      "notify": {
        "name": "HyperNotifyFix", "card": "Fix late notifications on Xiaomi and replace Xiao AI with Gemini, ChatGPT or Claude",
        "h2": "HyperNotifyFix: fix delayed notifications on Xiaomi HyperOS &amp; MIUI, and swap Xiao AI for Gemini, ChatGPT or Claude",
        "chips": ["Android 8+", "Xiaomi · Redmi · POCO", "No root"],
        "problem": "<strong>Zalo, Messenger, Gmail, Telegram or WhatsApp notifications arrive late, or only when you open the app?</strong> HyperOS freezes apps and Google Play Services in the background to save battery. HyperNotifyFix finds what is blocking your notifications and fixes it, without root, through Shizuku.",
        "features": [
          "Turns off battery optimization (Doze) and background limits for the apps you pick",
          "Adds them to Xiaomi’s hidden MILLET and low-latency whitelists, refreshes MiPush and reconnects Google push (FCM)",
          "Every change is previewed, backed up and reversible. Dry Run is on by default",
          "<b>AI assistant on the power button:</b> replace Xiao AI with Gemini, ChatGPT, Claude or any installed assistant. After the first setup you can switch without Shizuku",
          "Keeps every fix after a reboot and after HyperOS rewrites it (HyperOS China resets the assistant on every boot)",
          "Tested on Xiaomi 15 Ultra (HyperOS 3). Other HyperOS / MIUI phones should work: please report your results",
        ],
        "steps": [
          "Download <code>HyperNotifyFix-&lt;version&gt;.apk</code> and install it (allow “Install unknown apps” if asked).",
          "Install <a href=\"https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api\">Shizuku</a> from Google Play.",
          "Settings → About phone → tap <b>OS version</b> 7 times. Then Additional settings → Developer options → turn on <b>Wireless debugging</b>.",
          "Open Shizuku → <b>Start via Wireless debugging</b> → pair with the code → <b>Start</b>.",
          "Open HyperNotifyFix → allow Shizuku → pick the apps with late notifications → <b>Run diagnostics</b> → turn off Dry Run → <b>Apply</b>.",
          "Optional: Settings → <b>Trợ lý AI cho nút nguồn</b> (AI assistant for the power key) → pick Gemini, ChatGPT, Claude… → <b>Apply</b>.",
        ],
        "note": "Battery use may rise slightly. No app can guarantee instant notifications: the sender’s server and your network matter too.",
        "button": "Download APK",
      },
      "convert": {
        "name": "ConvertApp", "card": "Convert images, PDF, Word, Excel offline",
        "h2": "ConvertApp: free offline file converter for Windows, Mac &amp; Linux",
        "chips": ["Windows 10/11", "macOS", "Linux", "English · Tiếng Việt"],
        "problem": "<strong>Convert many files at once without uploading them to some website.</strong> Drag files in, pick a format, done. On Windows, just right-click files → <b>Convert to ▸</b>.",
        "features": [
          "<b>Images:</b> PNG, JPG, WebP, GIF, BMP, TIFF, ICO, SVG, with resize, quality and EXIF auto-rotate",
          "<b>Merge</b> many images into one PDF or one long picture",
          "<b>Documents:</b> Markdown ↔ HTML, Markdown/HTML → Word or PDF, Word → Markdown/HTML, web page → PDF or full-page PNG",
          "<b>Office:</b> Word, Excel, PowerPoint (DOCX, XLSX, PPTX, ODT…) → PDF and between Office formats",
        ],
        "os": [
          ("windows", "Windows", "<code>ConvertApp_…_x64-setup.exe</code>", "SmartScreen warning? <b>More info → Run anyway</b>."),
          ("mac", "macOS", "<code>…_aarch64.dmg</code> (Apple M chip) or <code>…_x64.dmg</code> (Intel)", "Drag to Applications, then right-click → <b>Open</b>."),
          ("linux", "Linux", "<code>.deb</code> (Ubuntu/Debian) or <code>.AppImage</code>", "<code>chmod +x</code> the AppImage, then run it."),
        ],
        "note": "Images, Markdown and HTML work right away. For Word, PDF and Office the app tells you which free tool to install (Pandoc, LibreOffice, or Edge/Chrome).",
        "button": "Download ConvertApp",
      },
      "clicker": {
        "name": "Kell Auto Clicker", "card": "Record mouse &amp; keyboard, replay automatically",
        "h2": "Kell Auto Clicker: free auto clicker &amp; macro recorder",
        "chips": ["Windows", "macOS", "Linux", "Java included"],
        "problem": "<strong>Stop doing the same clicks over and over.</strong> Record mouse clicks, key presses, scrolls and drag-and-drops once, then replay them as many times as you want.",
        "features": [
          "Global hotkeys: <b>F9</b> record, <b>F7</b> play, <b>F8</b> stop, even while another app is in front",
          "Add steps by hand: click a point, press keys, scroll, drag-and-drop, comments",
          "Repeat N times or for a set duration, with natural random mouse paths",
          "Save and load macros. Nothing else to install",
        ],
        "os": [
          ("windows", "Windows", "<code>.msi</code>, or <code>auto-clicker-windows-portable.zip</code> (no install)", "SmartScreen warning? <b>More info → Run anyway</b>."),
          ("mac", "macOS", "<code>.dmg</code>: <code>arm64</code> (Apple M chip) or <code>x64</code> (Intel)", "Right-click → <b>Open</b>, then allow it in Privacy &amp; Security → <b>Accessibility</b>."),
          ("linux", "Linux", "<code>.deb</code> or <code>.tar.gz</code>", "Global hotkeys need an X11 session (not Wayland)."),
        ],
        "button": "Download Auto Clicker",
      },
    },
    "support": {
      "h2": "Buy me a coffee",
      "text": "All apps are free and will stay free. If one saved you time, a small tip keeps them maintained. Thank you!",
      "paypal": "Donate with PayPal", "bank_label": "Bank transfer (Vietnam, VietQR)",
      "qr_alt": "VietQR bank transfer QR code, VietinBank, NGUYEN TUAN TRUYEN",
      "kicker": "Free forever, supported by people like you", "or": "or scan with any banking app",
      "copy": "Copy", "copied": "Copied", "thanks": "Every coffee goes into fixes and new features.",
    },
    "footer": "Found a bug or have an idea? Open an issue on GitHub.",
  },
  "vi": {
    "path": "vi/", "html_lang": "vi", "og_locale": "vi_VN", "currency": "VND",
    "title": "Sửa thông báo trễ &amp; đổi trợ lý AI trên Xiaomi, chuyển đổi file, auto click miễn phí",
    "description": "App miễn phí, mã nguồn mở: HyperNotifyFix sửa thông báo Zalo, Messenger bị trễ trên Xiaomi HyperOS/MIUI và đổi trợ lý nút nguồn sang Gemini, ChatGPT, Claude, không cần root; ConvertApp chuyển ảnh, Word, PDF, Excel không cần mạng; Kell Auto Clicker tự động click chuột.",
    "og_title": "Sửa thông báo trễ Xiaomi, chuyển đổi file, auto click – miễn phí",
    "og_description": "Không root, không quảng cáo, không cần tài khoản. Tải cho Android, Windows, macOS, Linux.",
    "nav": {"apps": "Ứng dụng", "support": "Ủng hộ", "donate": "Mời cà phê"},
    "cta_apps": "Xem ứng dụng", "cta_donate": "Mời mình ly cà phê",
    "after_download": "Thấy có ích? <a href=\"#support\">Mời mình ly cà phê ☕</a>",
    "pills": ["Miễn phí 100%", "Mã nguồn mở", "Không quảng cáo", "Không cần tài khoản"],
    "h1": "Công cụ nhỏ, miễn phí, <em>sửa là chạy</em>",
    "lead": "Sửa thông báo bị trễ trên Xiaomi, chuyển đổi file không cần tải lên mạng, tự động hoá những cú click lặp lại. Không gửi dữ liệu đi đâu cả.",
    "go": "Xem cách cài →", "install": "Cách cài đặt", "features": "Làm được gì",
    "download_for": "Tải về", "source": "Mã nguồn", "your_system": "Máy của bạn",
    "apps": {
      "notify": {
        "name": "HyperNotifyFix", "card": "Sửa thông báo bị trễ trên Xiaomi, thay trợ lý AI mặc định bằng Gemini, ChatGPT, Claude",
        "h2": "HyperNotifyFix: sửa thông báo Zalo, Messenger bị trễ trên Xiaomi HyperOS, MIUI và đổi trợ lý AI sang Gemini, ChatGPT, Claude",
        "chips": ["Android 8+", "Xiaomi · Redmi · POCO", "Không cần root"],
        "problem": "<strong>Thông báo Zalo, Messenger, Gmail, Telegram đến muộn, hoặc chỉ hiện khi mở app?</strong> HyperOS “đóng băng” app và Google Play Services khi chạy nền để tiết kiệm pin, nên thông báo bị giữ lại. HyperNotifyFix tìm đúng nguyên nhân và gỡ các giới hạn đó, không cần root, thông qua Shizuku.",
        "features": [
          "Tắt tối ưu pin (Doze) và giới hạn chạy nền cho các app bạn chọn",
          "Thêm vào whitelist ẩn MILLET và low-latency của Xiaomi, làm mới MiPush, kết nối lại thông báo Google (FCM)",
          "Mọi thay đổi đều được xem trước, sao lưu và hoàn tác được. Chế độ chạy thử (Dry Run) bật sẵn",
          "<b>Trợ lý AI cho nút nguồn:</b> thay Xiao AI bằng Gemini, ChatGPT, Claude hoặc bất kỳ trợ lý nào đã cài. Sau lần cài đầu, đổi qua lại không cần Shizuku",
          "Tự giữ mọi thiết lập sau khi khởi động lại hoặc khi HyperOS ghi đè (HyperOS bản Trung Quốc xoá trợ lý sau mỗi lần khởi động)",
          "Đã thử trên Xiaomi 15 Ultra (HyperOS 3). Máy HyperOS / MIUI khác cũng dùng được: mong bạn báo lại kết quả",
        ],
        "steps": [
          "Tải file <code>HyperNotifyFix-&lt;phiên bản&gt;.apk</code> rồi cài (nếu máy hỏi thì cho phép “Cài ứng dụng không rõ nguồn gốc”).",
          "Cài <a href=\"https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api\">Shizuku</a> từ CH Play.",
          "Cài đặt → Giới thiệu điện thoại → bấm 7 lần vào <b>Phiên bản HĐH</b>. Sau đó Cài đặt bổ sung → Tùy chọn nhà phát triển → bật <b>Gỡ lỗi không dây</b>.",
          "Mở Shizuku → <b>Khởi động qua Gỡ lỗi không dây</b> → ghép nối bằng mã → <b>Bắt đầu</b>.",
          "Mở HyperNotifyFix → cho phép Shizuku → chọn app bị trễ thông báo → <b>Chẩn đoán</b> → tắt Dry Run → <b>Áp dụng</b>.",
          "Tuỳ chọn: Cài đặt → thẻ <b>Trợ lý AI cho nút nguồn</b> → chọn Gemini, ChatGPT, Claude… → <b>Áp dụng</b>.",
        ],
        "note": "Pin có thể hao hơn một chút. Không app nào đảm bảo thông báo đến ngay lập tức: còn tuỳ máy chủ của app gửi và mạng của bạn.",
        "button": "Tải APK",
      },
      "convert": {
        "name": "ConvertApp", "card": "Chuyển ảnh, PDF, Word, Excel không cần mạng",
        "h2": "ConvertApp: phần mềm chuyển đổi file miễn phí, không cần mạng",
        "chips": ["Windows 10/11", "macOS", "Linux", "Tiếng Việt · English"],
        "problem": "<strong>Chuyển đổi hàng loạt file một lúc, không phải tải lên trang web nào.</strong> Kéo file vào, chọn định dạng, xong. Trên Windows chỉ cần chuột phải vào file → <b>Chuyển sang ▸</b>.",
        "features": [
          "<b>Ảnh:</b> PNG, JPG, WebP, GIF, BMP, TIFF, ICO, SVG, đổi kích thước, chất lượng, tự xoay theo EXIF",
          "<b>Gộp</b> nhiều ảnh thành 1 file PDF hoặc 1 ảnh dài",
          "<b>Văn bản:</b> Markdown ↔ HTML, Markdown/HTML → Word hoặc PDF, Word → Markdown/HTML, trang web → PDF hoặc ảnh chụp cả trang",
          "<b>Office:</b> Word, Excel, PowerPoint (DOCX, XLSX, PPTX, ODT…) → PDF và đổi qua lại giữa các định dạng Office",
        ],
        "os": [
          ("windows", "Windows", "<code>ConvertApp_…_x64-setup.exe</code>", "SmartScreen cảnh báo? Bấm <b>More info → Run anyway</b>."),
          ("mac", "macOS", "<code>…_aarch64.dmg</code> (chip Apple M) hoặc <code>…_x64.dmg</code> (Intel)", "Kéo vào Applications, rồi chuột phải → <b>Open</b>."),
          ("linux", "Linux", "<code>.deb</code> (Ubuntu/Debian) hoặc <code>.AppImage</code>", "<code>chmod +x</code> file AppImage rồi chạy."),
        ],
        "note": "Ảnh, Markdown, HTML dùng được ngay. Với Word, PDF, Office, app sẽ chỉ rõ cần cài thêm công cụ miễn phí nào (Pandoc, LibreOffice, hoặc Edge/Chrome).",
        "button": "Tải ConvertApp",
      },
      "clicker": {
        "name": "Kell Auto Clicker", "card": "Ghi thao tác chuột, phím rồi tự phát lại",
        "h2": "Kell Auto Clicker: phần mềm auto click chuột, ghi macro miễn phí",
        "chips": ["Windows", "macOS", "Linux", "Không cần cài Java"],
        "problem": "<strong>Thôi click đi click lại cùng một việc.</strong> Ghi lại click chuột, phím bấm, cuộn và kéo thả một lần, rồi phát lại bao nhiêu lần tùy ý.",
        "features": [
          "Phím tắt toàn cục: <b>F9</b> ghi, <b>F7</b> chạy, <b>F8</b> dừng, kể cả khi đang mở app khác",
          "Tự thêm bước bằng tay: click vào điểm, bấm phím, cuộn, kéo thả, ghi chú",
          "Lặp N lần hoặc trong một khoảng thời gian, đường di chuột ngẫu nhiên tự nhiên",
          "Lưu và mở lại macro. Không phải cài gì thêm",
        ],
        "os": [
          ("windows", "Windows", "<code>.msi</code>, hoặc <code>auto-clicker-windows-portable.zip</code> (giải nén là chạy)", "SmartScreen cảnh báo? Bấm <b>More info → Run anyway</b>."),
          ("mac", "macOS", "<code>.dmg</code>: <code>arm64</code> (chip Apple M) hoặc <code>x64</code> (Intel)", "Chuột phải → <b>Open</b>, rồi cấp quyền ở Quyền riêng tư &amp; Bảo mật → <b>Trợ năng</b>."),
          ("linux", "Linux", "<code>.deb</code> hoặc <code>.tar.gz</code>", "Phím tắt toàn cục cần phiên X11 (không chạy trên Wayland)."),
        ],
        "button": "Tải Auto Clicker",
      },
    },
    "support": {
      "h2": "Mời mình ly cà phê",
      "text": "Các app đều miễn phí và sẽ luôn miễn phí. Nếu thấy có ích, một chút ủng hộ giúp mình có thêm thời gian duy trì và cập nhật. Cảm ơn bạn!",
      "paypal": "Ủng hộ qua PayPal", "bank_label": "Chuyển khoản / quét VietQR",
      "qr_alt": "Mã QR chuyển khoản VietQR VietinBank NGUYEN TUAN TRUYEN",
      "kicker": "Miễn phí mãi mãi, nhờ những người như bạn", "or": "hoặc quét mã bằng app ngân hàng bất kỳ",
      "copy": "Chép", "copied": "Đã chép", "thanks": "Mỗi ly cà phê là thêm thời gian để sửa lỗi và làm tính năng mới.",
    },
    "footer": "Gặp lỗi hoặc có ý tưởng? Tạo issue trên GitHub.",
  },
}

SCRIPT = """<script>
(function () {
  // Remember an explicit language choice; first-time Vietnamese visitors to the English page go to /vi/.
  var KEY = 'lang';
  function get() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  document.querySelectorAll('[data-lang]').forEach(function (a) {
    a.addEventListener('click', function () { try { localStorage.setItem(KEY, a.dataset.lang); } catch (e) {} });
  });
  if (document.documentElement.lang === 'en' && !get() && !/bot|crawl|spider/i.test(navigator.userAgent)
      && (navigator.languages || [navigator.language]).some(function (l) { return /^vi\\b/i.test(l); })) {
    location.replace('vi/' + location.hash);
  }
  // Highlight the download row for the visitor's OS.
  var ua = navigator.userAgent, os = /Windows/.test(ua) ? 'windows' : /Mac OS X|Macintosh/.test(ua) && !/iPhone|iPad/.test(ua) ? 'mac'
         : /Linux/.test(ua) && !/Android/.test(ua) ? 'linux' : null;
  if (os) document.querySelectorAll('.os[data-os="' + os + '"]').forEach(function (el) { el.classList.add('is-you'); });
  // Copy the bank account number.
  document.querySelectorAll('.copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var label = b.querySelector('span'), old = label.textContent;
      (navigator.clipboard ? navigator.clipboard.writeText(b.dataset.copy) : Promise.reject()).then(function () {
        label.textContent = b.dataset.done; setTimeout(function () { label.textContent = old; }, 1600);
      }, function () {});
    });
  });
  // Floating coffee button: show after the hero, hide while the donate section is on screen.
  var fab = document.querySelector('.float-donate'), hero = document.querySelector('.hero'),
      donate = document.getElementById('support');
  if (fab && 'IntersectionObserver' in window) {
    var past = false, atDonate = false;
    function sync() { fab.classList.toggle('show', past && !atDonate); }
    new IntersectionObserver(function (e) { past = !e[0].isIntersecting; sync(); }).observe(hero);
    new IntersectionObserver(function (e) { atDonate = e[0].isIntersecting; sync(); }).observe(donate);
  }
})();
</script>"""


def ld_json(c):
    items = []
    for key, app in c["apps"].items():
        items.append({
            "@context": "https://schema.org", "@type": "SoftwareApplication", "name": app["name"],
            "inLanguage": c["html_lang"], "description": strip(app["card"]),
            "operatingSystem": "Android 8+" if key == "notify" else "Windows, macOS, Linux",
            "applicationCategory": "UtilitiesApplication",
            "downloadUrl": f"{GH}/{REPO[key]}/releases/latest",
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": c["currency"]},
        })
    return json.dumps(items, ensure_ascii=False, indent=1)


def strip(s):
    return s.replace("&amp;", "&")


def app_section(key, app, c):
    root = "../" if c["path"] else ""
    if "steps" in app:
        install = '<ol class="steps">' + "".join(f"<li><span>{s}</span></li>" for s in app["steps"]) + "</ol>"
    else:
        install = '<div class="os-list">' + "".join(
            f'<div class="os" data-os="{os_id}"><div><b>{label}</b><span class="you">{c["your_system"]}</span></div>'
            f'<div class="file">{file}</div><div class="tip">{tip}</div></div>'
            for os_id, label, file, tip in app["os"]) + "</div>"
    note = f'<p class="note">{app["note"]}</p>' if app.get("note") else ""
    chips = "".join(f'<span class="chip">{x}</span>' for x in app["chips"])
    feats = "".join(f"<li><span>{f}</span></li>" for f in app["features"])
    return f'''
<section class="app {ACCENT[key]}" id="{key}">
  <div class="app-head"><div class="icon">{ICONS[key]}</div>
    <div><h2>{app["h2"]}</h2><div class="chips">{chips}</div></div></div>
  <p class="problem">{app["problem"]}</p>
  <div class="grid-2">
    <div><h3>{c["features"]}</h3><ul class="features">{feats}</ul></div>
    <div><h3>{c["install"]}</h3>{install}</div>
  </div>
  {note}
  <div class="actions">
    <a class="btn" href="{GH}/{REPO[key]}/releases/latest">{ICONS["download"]}{app["button"]}</a>
    <a class="btn ghost" href="{GH}/{REPO[key]}">{c["source"]}</a>
  </div>
  <p class="nudge">{ICONS["heart"]}<span>{c["after_download"]}</span></p>
</section>'''


def page(lang):
    c = CONTENT[lang]
    root = "../" if c["path"] else ""
    url = f"{SITE}/{c['path']}"
    cards = "".join(
        f'<a class="card {ACCENT[k]}" href="#{k}"><div class="icon">{ICONS[k]}</div>'
        f'<strong>{a["name"]}</strong><span>{a["card"]}</span><span class="go">{c["go"]}</span></a>'
        for k, a in c["apps"].items())
    pills = "".join(f'<span class="pill">{p}</span>' for p in c["pills"])
    apps = "".join(app_section(k, a, c) for k, a in c["apps"].items())
    s = c["support"]
    lang_switch = "".join(
        f'<a href="{root}{CONTENT[l]["path"]}" hreflang="{l}" lang="{l}" data-lang="{l}"'
        f'{CURRENT if l == lang else ""}>{l.upper()}</a>' for l in ("en", "vi"))
    return f'''<!doctype html>
<html lang="{c["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{c["title"]}</title>
<meta name="description" content="{c["description"]}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{SITE}/">
<link rel="alternate" hreflang="vi" href="{SITE}/vi/">
<link rel="alternate" hreflang="x-default" href="{SITE}/">
<meta property="og:type" content="website">
<meta property="og:locale" content="{c["og_locale"]}">
<meta property="og:title" content="{c["og_title"]}">
<meta property="og:description" content="{c["og_description"]}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#fbfaf8">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='.9em' font-size='90'%3E%E2%9C%A8%3C/text%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="{root}style.css">
<script type="application/ld+json">
{ld_json(c)}
</script>
</head>
<body>
<header class="bar"><div class="wrap">
  <a class="brand" href="{root}{c["path"]}"><span class="brand-mark">dk</span>ds-kell</a>
  <nav>
    <a class="link" href="#apps">{c["nav"]["apps"]}</a>
    <a class="link" href="{GH}">GitHub</a>
    <a class="nav-donate" href="#support">{ICONS["heart"]}<span>{c["nav"]["donate"]}</span></a>
    <span class="lang">{lang_switch}</span>
  </nav>
</div></header>

<main>
<section class="hero"><div class="wrap">
  <div class="pills">{pills}</div>
  <h1>{c["h1"]}</h1>
  <p class="lead">{c["lead"]}</p>
  <div class="hero-cta">
    <a class="btn dark" href="#apps">{c["cta_apps"]} ↓</a>
    <a class="btn coffee" href="#support">{ICONS["heart"]}{c["cta_donate"]}</a>
  </div>
  <div class="cards" id="apps">{cards}</div>
</div></section>

<div class="wrap">
{apps}

<section class="donate" id="support">
  <div class="donate-text">
    <span class="kicker">{s["kicker"]}</span>
    <h2>{ICONS["heart"]}{s["h2"]}</h2>
    <p>{s["text"]}</p>
    <a class="btn paypal" href="{PAYPAL}">{s["paypal"]} →</a>
    <div class="bank">
      <b>{s["bank_label"]}</b>
      <div class="bank-row"><span>{BANK[0]} · {BANK[1]}</span>
        <button class="copy" type="button" data-copy="{BANK[2]}" data-done="{s["copied"]}"><code>{BANK[2]}</code><span>{s["copy"]}</span></button></div>
    </div>
    <p class="thanks">{s["thanks"]}</p>
  </div>
  <figure class="qr">
    <img src="{root}assets/donate-vietqr.jpg" alt="{s["qr_alt"]}" width="220" height="391" loading="lazy">
    <figcaption>{s["or"]}</figcaption>
  </figure>
</section>
</div>
</main>

<a class="float-donate" href="#support" aria-label="{c["nav"]["donate"]}">{ICONS["heart"]}<span>{c["nav"]["donate"]}</span></a>
<footer class="wrap">{c["footer"]} · <a href="{GH}">github.com/ds-kell</a></footer>
{SCRIPT}
</body>
</html>
'''


if __name__ == "__main__":
    here = Path(__file__).parent
    for lang in CONTENT:
        out = here / CONTENT[lang]["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(lang), encoding="utf-8")
        print("wrote", out.relative_to(here))
