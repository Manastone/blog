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
  .course-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 24px;
  }
  .course-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(201,168,76,0.15);
    border-radius: 10px;
    padding: 22px 24px;
  }
  .course-label {
    color: #c9a84c;
    font-size: 12px;
    letter-spacing: 2px;
    margin-bottom: 8px;
  }
  .course-name {
    color: #ffffff;
    font-size: 20px;
    font-weight: 700;
    margin-bottom: 8px;
  }
  .course-desc {
    color: rgba(245,240,224,0.6);
    font-size: 14px;
    line-height: 1.5;
  }
  .warning-bar {
    background: rgba(255,160,50,0.08);
    border-left: 4px solid #f0a030;
    border-radius: 0 8px 8px 0;
    padding: 16px 24px;
    display: flex;
    align-items: center;
    gap: 16px;
    margin-bottom: 20px;
  }
  .warning-icon { font-size: 22px; }
  .warning-text {
    color: rgba(245,240,224,0.8);
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
    <div class="badge">JGTO 개최 코스</div>
    <div class="club-number">02</div>
  </div>
  <div class="title-section">
    <div class="club-name-en">AKAMIZU GOLF RESORT</div>
    <div class="club-name">아카미즈 골프 리조트</div>
    <div class="club-tagline">규슈 명문 · 넓은 페어웨이 · 호쾌한 드라이버샷</div>
  </div>
  <div class="divider"></div>
  <div class="info-grid">
    <div class="info-item">
      <div class="info-label">개장 / 설계</div>
      <div class="info-value">1966년</div>
      <div class="info-sub">설계: 아카호시 시로</div>
    </div>
    <div class="info-item">
      <div class="info-label">규모</div>
      <div class="info-value">18홀</div>
      <div class="info-sub">27홀 확장 리뉴얼 중 (2025~)</div>
    </div>
    <div class="info-item">
      <div class="info-label">특징</div>
      <div class="info-value">JGTO 공식</div>
      <div class="info-sub">전 일본 남자프로투어 개최</div>
    </div>
  </div>
  <div class="course-grid">
    <div class="course-card">
      <div class="course-label">코스 A</div>
      <div class="course-name">키지마 코스 (杵島)</div>
      <div class="course-desc">수령 50년+ 삼나무·편백나무<br>둘러싸인 임간(林間) 코스</div>
    </div>
    <div class="course-card">
      <div class="course-label">코스 B</div>
      <div class="course-name">나카다케 코스 (中岳)</div>
      <div class="course-desc">화산암 점재 고원 코스<br>아소 칼데라 지형 활용</div>
    </div>
  </div>
  <div class="warning-bar">
    <div class="warning-icon">⚠️</div>
    <div class="warning-text"><strong style="color:#f0d98a;">주의사항</strong> — 스태프가 일본어로만 소통 가능합니다. 동행 중 일본어 가능자 1명 이상 필수 권장</div>
  </div>
  <div class="tags">
    <span class="tag">JGTO 대회 개최</span>
    <span class="tag">규슈 명문 코스</span>
    <span class="tag">넓은 페어웨이</span>
    <span class="tag">아카호시 시로 설계</span>
    <span class="tag">27홀 확장 예정</span>
  </div>
  <div class="bottom-bar"></div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\일본 구마모토 골프여행 하기 좋은 5개의 골프클럽\images\body-3.png", full_page=True)
    browser.close()
    print("body-3.png 생성 완료")
