from playwright.sync_api import sync_playwright

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px;
    background: linear-gradient(160deg, #1a2e1a 0%, #0d1f0d 100%);
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    padding: 60px 70px;
    min-height: 660px;
  }
  .header {
    text-align: center;
    margin-bottom: 50px;
  }
  .header-label {
    display: inline-block;
    background: rgba(201,168,76,0.15);
    border: 1px solid rgba(201,168,76,0.4);
    color: #c9a84c;
    font-size: 14px;
    letter-spacing: 3px;
    padding: 6px 20px;
    border-radius: 2px;
    margin-bottom: 18px;
  }
  .header-title {
    color: #ffffff;
    font-size: 40px;
    font-weight: 700;
    letter-spacing: -1px;
  }
  .header-divider {
    width: 60px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #c9a84c, transparent);
    margin: 16px auto 0;
  }
  .cards-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
  }
  .card {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(201,168,76,0.2);
    border-radius: 12px;
    padding: 36px 32px;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 14px;
    transition: all 0.3s;
  }
  .card-icon {
    font-size: 40px;
    line-height: 1;
  }
  .card-title {
    color: #c9a84c;
    font-size: 16px;
    font-weight: 600;
    letter-spacing: 1px;
  }
  .card-value {
    color: #ffffff;
    font-size: 28px;
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.5px;
  }
  .card-desc {
    color: rgba(245,240,224,0.65);
    font-size: 15px;
    font-weight: 300;
    line-height: 1.5;
  }
  .card-accent {
    width: 40px;
    height: 2px;
    background: #c9a84c;
    border-radius: 1px;
  }
  .bottom-bar {
    height: 4px;
    background: linear-gradient(90deg, #c9a84c, #f0d98a, #c9a84c);
    margin-top: 50px;
    border-radius: 2px;
  }
</style>
</head>
<body>
  <div class="header">
    <div class="header-label">OVERVIEW</div>
    <div class="header-title">구마모토 골프여행 한눈에 보기</div>
    <div class="header-divider"></div>
  </div>
  <div class="cards-grid">
    <div class="card">
      <div class="card-icon">✈️</div>
      <div class="card-accent"></div>
      <div class="card-title">비행 소요시간</div>
      <div class="card-value">1시간 33분</div>
      <div class="card-desc">인천 → 구마모토<br>국내선보다 짧은 거리</div>
    </div>
    <div class="card">
      <div class="card-icon">⛳</div>
      <div class="card-accent"></div>
      <div class="card-title">추천 골프클럽</div>
      <div class="card-value">5개 코스</div>
      <div class="card-desc">아소산 칼데라 배경<br>다양한 스타일의 코스</div>
    </div>
    <div class="card">
      <div class="card-icon">💴</div>
      <div class="card-accent"></div>
      <div class="card-title">그린피 (평일)</div>
      <div class="card-value">6,700~13,000엔</div>
      <div class="card-desc">한국 절반 이하 수준<br>카트·락카 포함 상품도 있음</div>
    </div>
    <div class="card">
      <div class="card-icon">♨️</div>
      <div class="card-accent"></div>
      <div class="card-title">라운딩 후</div>
      <div class="card-value">구로카와 온천</div>
      <div class="card-desc">코스+자연+온천 한 묶음<br>피로 회복 완벽 마무리</div>
    </div>
  </div>
  <div class="bottom-bar"></div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\일본 구마모토 골프여행 하기 좋은 5개의 골프클럽\images\body-1.png", full_page=True)
    browser.close()
    print("body-1.png 생성 완료")
