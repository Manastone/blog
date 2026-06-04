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
  }
  .club-number {
    color: rgba(201,168,76,0.3);
    font-size: 72px;
    font-weight: 700;
    line-height: 0.9;
    letter-spacing: -4px;
  }
  .title-section { margin-bottom: 36px; }
  .club-name-en {
    color: rgba(201,168,76,0.6);
    font-size: 14px;
    letter-spacing: 3px;
    margin-bottom: 10px;
  }
  .club-name {
    color: #ffffff;
    font-size: 40px;
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
  }
  .info-value {
    color: #ffffff;
    font-size: 20px;
    font-weight: 600;
    line-height: 1.3;
  }
  .info-sub {
    color: rgba(245,240,224,0.55);
    font-size: 13px;
    margin-top: 6px;
  }
  .fee-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 24px;
  }
  .fee-card {
    background: rgba(201,168,76,0.06);
    border: 1px solid rgba(201,168,76,0.2);
    border-radius: 10px;
    padding: 22px 24px;
  }
  .fee-type {
    color: #c9a84c;
    font-size: 13px;
    letter-spacing: 1px;
    margin-bottom: 6px;
  }
  .fee-amount {
    color: #ffffff;
    font-size: 26px;
    font-weight: 700;
  }
  .fee-desc {
    color: rgba(245,240,224,0.5);
    font-size: 13px;
    margin-top: 4px;
  }
  .rating-bar {
    background: rgba(201,168,76,0.08);
    border-left: 4px solid #c9a84c;
    border-radius: 0 8px 8px 0;
    padding: 18px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 20px;
  }
  .rating-left {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .rating-icon { font-size: 24px; }
  .rating-text {
    color: #f5f0e0;
    font-size: 16px;
    line-height: 1.5;
  }
  .rating-score {
    text-align: right;
  }
  .score-value {
    color: #c9a84c;
    font-size: 36px;
    font-weight: 700;
    line-height: 1;
  }
  .score-label {
    color: rgba(245,240,224,0.5);
    font-size: 13px;
    margin-top: 4px;
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
    <div class="badge">공항 10분 · 최고 접근성</div>
    <div class="club-number">04</div>
  </div>
  <div class="title-section">
    <div class="club-name-en">KUMAMOTO AIRPORT COUNTRY CLUB</div>
    <div class="club-name">구마모토 공항 컨트리클럽</div>
    <div class="club-tagline">도착하자마자 바로 티샷 — 공항에서 차로 10~15분</div>
  </div>
  <div class="divider"></div>
  <div class="info-grid">
    <div class="info-item">
      <div class="info-label">개장 / 규모</div>
      <div class="info-value">1974년 개장</div>
      <div class="info-sub">7,091야드 · PAR 72 · 18홀</div>
    </div>
    <div class="info-item">
      <div class="info-label">그린 타입</div>
      <div class="info-value">2그린</div>
      <div class="info-sub">벤트그라스 + 고려잔디</div>
    </div>
    <div class="info-item">
      <div class="info-label">코스 형태</div>
      <div class="info-value">구릉형 코스</div>
      <div class="info-sub">여자프로 토너먼트 개최 이력</div>
    </div>
  </div>
  <div class="fee-grid">
    <div class="fee-card">
      <div class="fee-type">평일 캐디 포함</div>
      <div class="fee-amount">13,000엔</div>
      <div class="fee-desc">4볼 기준 · 주말 18,800엔</div>
    </div>
    <div class="fee-card">
      <div class="fee-type">월·화 셀프 라운딩</div>
      <div class="fee-amount">7,700엔~</div>
      <div class="fee-desc">평일 초반 유연한 일정에 최적</div>
    </div>
  </div>
  <div class="rating-bar">
    <div class="rating-left">
      <div class="rating-icon">⭐</div>
      <div class="rating-text">라쿠텐 GORA 평점 — 953건 리뷰 기반<br>여자프로 토너먼트 개최 이력으로 코스 관리 신뢰도 높음</div>
    </div>
    <div class="rating-score">
      <div class="score-value">4.1</div>
      <div class="score-label">/ 5.0</div>
    </div>
  </div>
  <div class="tags">
    <span class="tag">공항 10~15분</span>
    <span class="tag">2그린 시스템</span>
    <span class="tag">여자프로 토너먼트</span>
    <span class="tag">라쿠텐 GORA 4.1점</span>
    <span class="tag">구릉형 코스</span>
  </div>
  <div class="bottom-bar"></div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\일본 구마모토 골프여행 하기 좋은 5개의 골프클럽\images\body-5.png", full_page=True)
    browser.close()
    print("body-5.png 생성 완료")
