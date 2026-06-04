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
    padding: 55px 70px;
  }
  .header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    margin-bottom: 40px;
  }
  .badge {
    background: linear-gradient(135deg, #c9a84c, #f0d98a);
    color: #1a2e1a;
    font-size: 13px;
    font-weight: 700;
    padding: 8px 20px;
    border-radius: 30px;
    letter-spacing: 1px;
    white-space: nowrap;
  }
  .header-right {
    text-align: right;
  }
  .club-number {
    color: rgba(201,168,76,0.3);
    font-size: 72px;
    font-weight: 700;
    line-height: 0.9;
    letter-spacing: -4px;
  }
  .title-section {
    margin-bottom: 36px;
  }
  .club-name-en {
    color: rgba(201,168,76,0.6);
    font-size: 14px;
    letter-spacing: 3px;
    margin-bottom: 10px;
  }
  .club-name {
    color: #ffffff;
    font-size: 42px;
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1.2;
    margin-bottom: 8px;
  }
  .club-tagline {
    color: rgba(245,240,224,0.6);
    font-size: 17px;
    font-weight: 300;
    letter-spacing: 1px;
  }
  .divider {
    width: 100%;
    height: 1px;
    background: rgba(201,168,76,0.2);
    margin-bottom: 36px;
  }
  .info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 20px;
    margin-bottom: 28px;
  }
  .info-item {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(201,168,76,0.15);
    border-radius: 10px;
    padding: 24px 22px;
  }
  .info-label {
    color: #c9a84c;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 10px;
    text-transform: uppercase;
  }
  .info-value {
    color: #ffffff;
    font-size: 22px;
    font-weight: 600;
    line-height: 1.3;
  }
  .info-sub {
    color: rgba(245,240,224,0.55);
    font-size: 13px;
    margin-top: 6px;
  }
  .highlight-bar {
    background: rgba(201,168,76,0.08);
    border-left: 4px solid #c9a84c;
    border-radius: 0 8px 8px 0;
    padding: 20px 28px;
    display: flex;
    align-items: center;
    gap: 20px;
    margin-bottom: 20px;
  }
  .highlight-icon { font-size: 28px; }
  .highlight-text {
    color: #f5f0e0;
    font-size: 18px;
    font-weight: 500;
    line-height: 1.5;
  }
  .tags {
    display: flex;
    gap: 10px;
    flex-wrap: wrap;
  }
  .tag {
    background: rgba(201,168,76,0.1);
    border: 1px solid rgba(201,168,76,0.25);
    color: #c9a84c;
    font-size: 13px;
    padding: 6px 16px;
    border-radius: 20px;
    letter-spacing: 0.5px;
  }
  .bottom-bar {
    height: 4px;
    background: linear-gradient(90deg, #c9a84c, #f0d98a, #c9a84c);
    margin-top: 44px;
    border-radius: 2px;
  }
</style>
</head>
<body>
  <div class="header">
    <div class="badge">No.1 한국인 방문 1위</div>
    <div class="club-number">01</div>
  </div>
  <div class="title-section">
    <div class="club-name-en">ASO RESORT GRANDVRIO HOTEL GOLF COURSE</div>
    <div class="club-name">아소 리조트 그랑브리오</div>
    <div class="club-tagline">아소산 절경 + 천연온천 — 구마모토 첫 방문자의 필수 코스</div>
  </div>
  <div class="divider"></div>
  <div class="info-grid">
    <div class="info-item">
      <div class="info-label">개장 / 설계</div>
      <div class="info-value">1990년</div>
      <div class="info-sub">설계: 아널드 파머</div>
    </div>
    <div class="info-item">
      <div class="info-label">규모</div>
      <div class="info-value">36홀 · PAR 143</div>
      <div class="info-sub">12,521야드 (동+서 코스)</div>
    </div>
    <div class="info-item">
      <div class="info-label">그린피 (카트+락카 포함)</div>
      <div class="info-value">약 102,000원~</div>
      <div class="info-sub">마이리얼트립 기준</div>
    </div>
  </div>
  <div class="highlight-bar">
    <div class="highlight-icon">♨️</div>
    <div class="highlight-text">라운딩 후 원천 노천탕(米塚温泉) 이용 가능 — 천연온천으로 피로 회복까지 한 번에</div>
  </div>
  <div class="highlight-bar">
    <div class="highlight-icon">🚗</div>
    <div class="highlight-text">아소서IC에서 차로 5분 · 동코스 절경 + 서코스 전략적 레이아웃 · 포테이토칩 그린</div>
  </div>
  <div class="tags">
    <span class="tag">한국인 방문 1위</span>
    <span class="tag">아소산 전망</span>
    <span class="tag">천연온천 구비</span>
    <span class="tag">36홀 대형 코스</span>
    <span class="tag">아널드 파머 설계</span>
  </div>
  <div class="bottom-bar"></div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\일본 구마모토 골프여행 하기 좋은 5개의 골프클럽\images\body-2.png", full_page=True)
    browser.close()
    print("body-2.png 생성 완료")
