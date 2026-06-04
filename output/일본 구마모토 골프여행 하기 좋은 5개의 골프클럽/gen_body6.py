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
  .quote-box {
    background: rgba(201,168,76,0.06);
    border: 1px solid rgba(201,168,76,0.25);
    border-radius: 12px;
    padding: 28px 36px;
    margin-bottom: 36px;
    position: relative;
  }
  .quote-mark {
    color: rgba(201,168,76,0.3);
    font-size: 60px;
    line-height: 0.8;
    position: absolute;
    top: 16px;
    left: 24px;
    font-family: Georgia, serif;
  }
  .quote-text {
    color: #f5f0e0;
    font-size: 20px;
    font-weight: 400;
    line-height: 1.7;
    padding-left: 40px;
    font-style: italic;
  }
  .quote-source {
    color: rgba(201,168,76,0.7);
    font-size: 14px;
    margin-top: 12px;
    padding-left: 40px;
    letter-spacing: 1px;
  }
  .title-section { margin-bottom: 32px; }
  .club-name-en {
    color: rgba(201,168,76,0.6);
    font-size: 13px;
    letter-spacing: 2px;
    margin-bottom: 8px;
  }
  .club-name {
    color: #ffffff;
    font-size: 36px;
    font-weight: 700;
    letter-spacing: -1px;
    line-height: 1.2;
    margin-bottom: 8px;
  }
  .club-tagline {
    color: rgba(245,240,224,0.6);
    font-size: 16px;
    font-weight: 300;
    letter-spacing: 1px;
  }
  .divider {
    width: 100%;
    height: 1px;
    background: rgba(201,168,76,0.2);
    margin-bottom: 32px;
  }
  .info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 18px;
    margin-bottom: 24px;
  }
  .info-item {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(201,168,76,0.15);
    border-radius: 10px;
    padding: 22px 20px;
  }
  .info-label {
    color: #c9a84c;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 8px;
  }
  .info-value {
    color: #ffffff;
    font-size: 19px;
    font-weight: 600;
    line-height: 1.3;
  }
  .info-sub {
    color: rgba(245,240,224,0.55);
    font-size: 13px;
    margin-top: 5px;
  }
  .highlight-bars {
    display: flex;
    flex-direction: column;
    gap: 14px;
    margin-bottom: 22px;
  }
  .highlight-bar {
    background: rgba(201,168,76,0.07);
    border-left: 4px solid #c9a84c;
    border-radius: 0 8px 8px 0;
    padding: 16px 24px;
    display: flex;
    align-items: center;
    gap: 14px;
  }
  .highlight-icon { font-size: 22px; }
  .highlight-text {
    color: #f5f0e0;
    font-size: 15px;
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
    <div class="badge">Since 1952 · 구마모토 최고령</div>
    <div class="club-number">05</div>
  </div>
  <div class="quote-box">
    <div class="quote-mark">"</div>
    <div class="quote-text">불도저 등 기계를 전혀 쓰지 않고 자연 지형 그대로를 살려<br>손으로 만든 코스 — 어떤 설계자도 흉내 낼 수 없는 자연의 레이아웃</div>
    <div class="quote-source">구마모토 최고령(最古) 골프장 · 1952년 개장</div>
  </div>
  <div class="title-section">
    <div class="club-name-en">KUMAMOTO GOLF CLUB · ASO YUNOTANI COURSE</div>
    <div class="club-name">구마모토 골프 구락부 아소 유노타니 코스</div>
    <div class="club-tagline">자연 지형 그대로 · 북외륜산 전망 · 지진 딛고 완전 복흥</div>
  </div>
  <div class="divider"></div>
  <div class="info-grid">
    <div class="info-item">
      <div class="info-label">개장</div>
      <div class="info-value">1952년</div>
      <div class="info-sub">구마모토현 내 최고(最古)</div>
    </div>
    <div class="info-item">
      <div class="info-label">코스 특징</div>
      <div class="info-value">자연 지형</div>
      <div class="info-sub">기계 없이 손으로 조성</div>
    </div>
    <div class="info-item">
      <div class="info-label">접근</div>
      <div class="info-value">35~45분</div>
      <div class="info-sub">구마모토 공항에서 차로</div>
    </div>
  </div>
  <div class="highlight-bars">
    <div class="highlight-bar">
      <div class="highlight-icon">🏔️</div>
      <div class="highlight-text">모든 홀에서 아소 북외륜산(北外輪山) 조망 — 자연이 만든 언듈레이션</div>
    </div>
    <div class="highlight-bar">
      <div class="highlight-icon">🔄</div>
      <div class="highlight-text">2016년 구마모토 대지진 피해 → 4년 복구 → <strong style="color:#f0d98a;">2020년 재개장 · 2022년 완전 복흥</strong></div>
    </div>
    <div class="highlight-bar">
      <div class="highlight-icon">⛳</div>
      <div class="highlight-text">명물 홀: 「마노세」(OUT 3번 PAR5) · 「203고지」 · 「독사골」 · 「휘파람새 골짜기」</div>
    </div>
  </div>
  <div class="tags">
    <span class="tag">구마모토 최고령</span>
    <span class="tag">자연 지형 코스</span>
    <span class="tag">북외륜산 전망</span>
    <span class="tag">2022년 완전 복흥</span>
    <span class="tag">골프 마니아 필수</span>
  </div>
  <div class="bottom-bar"></div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\일본 구마모토 골프여행 하기 좋은 5개의 골프클럽\images\body-6.png", full_page=True)
    browser.close()
    print("body-6.png 생성 완료")
