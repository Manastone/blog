from playwright.sync_api import sync_playwright

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px;
    height: 1080px;
    background: linear-gradient(160deg, #e0f4ff 0%, #b3d9f5 50%, #87bfe8 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    position: relative;
    overflow: hidden;
  }
  .bg-circle1 {
    position: absolute;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    background: rgba(255,255,255,0.12);
    top: -150px;
    right: -150px;
  }
  .bg-circle2 {
    position: absolute;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    background: rgba(255,255,255,0.08);
    bottom: -100px;
    left: -100px;
  }
  .center {
    text-align: center;
    z-index: 10;
    padding: 60px;
  }
  .badge {
    display: inline-block;
    background: rgba(21, 101, 192, 0.15);
    border: 2px solid rgba(21, 101, 192, 0.3);
    color: #1565C0;
    font-size: 28px;
    font-weight: 700;
    padding: 10px 30px;
    border-radius: 40px;
    margin-bottom: 40px;
    letter-spacing: 2px;
  }
  .main-title {
    font-size: 96px;
    font-weight: 900;
    color: #1a2e3a;
    line-height: 1.1;
    margin-bottom: 30px;
    letter-spacing: -2px;
  }
  .main-title span {
    color: #1565C0;
  }
  .sub-title {
    font-size: 44px;
    font-weight: 700;
    color: #2a4a60;
    margin-bottom: 40px;
    line-height: 1.4;
  }
  .helper {
    font-size: 30px;
    color: #4a7090;
    font-weight: 400;
    letter-spacing: 0.5px;
  }
  .divider {
    width: 80px;
    height: 4px;
    background: #1565C0;
    margin: 30px auto;
    border-radius: 2px;
  }
  .accent {
    position: absolute;
    bottom: 60px;
    right: 70px;
    font-size: 120px;
    opacity: 0.18;
  }
  .accent2 {
    position: absolute;
    top: 60px;
    left: 70px;
    font-size: 80px;
    opacity: 0.12;
  }
  .number-badge {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    background: #1565C0;
    color: white;
    font-size: 32px;
    font-weight: 800;
    padding: 14px 36px;
    border-radius: 50px;
    margin-top: 40px;
  }
</style>
</head>
<body>
  <div class="bg-circle1"></div>
  <div class="bg-circle2"></div>
  <div class="accent">🔧</div>
  <div class="accent2">🚗</div>
  <div class="center">
    <div class="badge">출장 자동차 정비</div>
    <div class="main-title"><span>카수리</span> 출장정비</div>
    <div class="divider"></div>
    <div class="sub-title">정비소 방문보다 좋은 점<br>5가지</div>
    <div class="helper">집 앞에서 40분 완성 · 전국 출장</div>
    <div class="number-badge">⭐ 고객만족도 99.5%</div>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1080})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\thumbnail.png", full_page=False)
    browser.close()
print("thumbnail.png 완료")
