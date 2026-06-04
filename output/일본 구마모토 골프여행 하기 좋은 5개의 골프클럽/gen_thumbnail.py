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
    background: linear-gradient(160deg, #1a2e1a 0%, #0d1f0d 60%, #0a180a 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    position: relative;
    overflow: hidden;
  }
  .bg-circle {
    position: absolute;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(201,168,76,0.08) 0%, transparent 70%);
  }
  .bg-circle-1 { width: 800px; height: 800px; top: -200px; right: -200px; }
  .bg-circle-2 { width: 600px; height: 600px; bottom: -150px; left: -150px; }
  .flag-accent {
    position: absolute;
    top: 60px;
    left: 60px;
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .flag-line {
    width: 60px;
    height: 3px;
    background: #c9a84c;
  }
  .flag-text {
    color: #c9a84c;
    font-size: 18px;
    letter-spacing: 3px;
    font-weight: 400;
    text-transform: uppercase;
  }
  .golf-symbol {
    position: absolute;
    bottom: 70px;
    right: 80px;
    font-size: 120px;
    opacity: 0.12;
    line-height: 1;
  }
  .content {
    text-align: center;
    z-index: 10;
    padding: 0 80px;
  }
  .label {
    display: inline-block;
    background: rgba(201,168,76,0.15);
    border: 1px solid rgba(201,168,76,0.4);
    color: #c9a84c;
    font-size: 16px;
    letter-spacing: 4px;
    padding: 8px 24px;
    border-radius: 2px;
    margin-bottom: 40px;
  }
  .main-title {
    color: #ffffff;
    font-size: 88px;
    font-weight: 700;
    line-height: 1.1;
    margin-bottom: 20px;
    text-shadow: 0 4px 20px rgba(0,0,0,0.5);
    letter-spacing: -2px;
  }
  .sub-title {
    color: #c9a84c;
    font-size: 42px;
    font-weight: 600;
    margin-bottom: 36px;
    letter-spacing: 1px;
  }
  .divider {
    width: 80px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #c9a84c, transparent);
    margin: 0 auto 36px;
  }
  .desc {
    color: rgba(245,240,224,0.75);
    font-size: 24px;
    font-weight: 300;
    letter-spacing: 3px;
    line-height: 1.8;
  }
  .bottom-bar {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, #c9a84c, #f0d98a, #c9a84c);
  }
</style>
</head>
<body>
  <div class="bg-circle bg-circle-1"></div>
  <div class="bg-circle bg-circle-2"></div>
  <div class="flag-accent">
    <div class="flag-line"></div>
    <span class="flag-text">Golf Travel Guide</span>
  </div>
  <div class="golf-symbol">⛳</div>
  <div class="content">
    <div class="label">KUMAMOTO · JAPAN</div>
    <div class="main-title">구마모토<br>골프여행</div>
    <div class="sub-title">가봐야 할 클럽 5곳</div>
    <div class="divider"></div>
    <div class="desc">아소산 · 온천 · 인천에서 1시간 33분</div>
  </div>
  <div class="bottom-bar"></div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 1080})
    page.set_content(html)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\일본 구마모토 골프여행 하기 좋은 5개의 골프클럽\images\thumbnail.png", full_page=False)
    browser.close()
    print("thumbnail.png 생성 완료")
