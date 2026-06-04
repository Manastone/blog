from playwright.sync_api import sync_playwright

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px;
    background: #ffffff;
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    padding: 60px;
  }
  .header {
    text-align: center;
    margin-bottom: 44px;
  }
  .header .tag {
    display: inline-block;
    background: #e8f4fd;
    color: #1565C0;
    font-size: 22px;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 30px;
    margin-bottom: 18px;
    border: 2px solid #b3d9f5;
  }
  .header h2 {
    font-size: 44px;
    font-weight: 900;
    color: #1a2e3a;
    line-height: 1.3;
  }
  .header h2 span { color: #1565C0; }
  .header .subtitle {
    margin-top: 12px;
    font-size: 22px;
    color: #5a7a90;
    font-weight: 500;
  }
  .checklist-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 32px;
  }
  .check-item {
    display: flex;
    align-items: center;
    gap: 16px;
    background: #f5f9ff;
    border-radius: 14px;
    padding: 20px 24px;
    border: 1.5px solid #daeeff;
  }
  .check-icon {
    width: 34px;
    height: 34px;
    border-radius: 50%;
    background: #1565C0;
    color: white;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 900;
    flex-shrink: 0;
  }
  .check-text {
    font-size: 22px;
    font-weight: 700;
    color: #1a2e3a;
    line-height: 1.4;
  }
  .bottom-banner {
    background: linear-gradient(135deg, #1565C0 0%, #1976D2 100%);
    border-radius: 18px;
    padding: 30px 44px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 24px;
  }
  .bottom-banner .left {
    display: flex;
    align-items: center;
    gap: 18px;
  }
  .bottom-banner .icon { font-size: 44px; }
  .bottom-banner .text {}
  .bottom-banner .text .main {
    font-size: 26px;
    font-weight: 900;
    color: white;
    margin-bottom: 6px;
  }
  .bottom-banner .text .sub {
    font-size: 20px;
    color: rgba(255,255,255,0.8);
  }
  .bottom-banner .count-badge {
    background: #FF6B35;
    color: white;
    font-size: 20px;
    font-weight: 900;
    padding: 14px 28px;
    border-radius: 50px;
    white-space: nowrap;
    text-align: center;
    line-height: 1.4;
    box-shadow: 0 4px 14px rgba(255,107,53,0.5);
  }
  .count-badge .num {
    font-size: 32px;
    display: block;
  }
</style>
</head>
<body>
  <div class="header">
    <div class="tag">✅ 장점 5 — 무상 안전점검</div>
    <h2>엔진오일 교체 하나에<br><span>이게 다 무료</span>입니다</h2>
    <div class="subtitle">기본 포함 13~14개 항목 무상 점검</div>
  </div>

  <div class="checklist-grid">
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">브레이크오일 수분 체크</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">부동액 점검</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">배터리 성능 점검</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">발전기 충전전압 점검</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">외부 벨트 점검</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">브레이크 패드 점검</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">타이어 공기압 보충</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">타이어 마모도 점검</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">차량 시스템 통합진단</div>
    </div>
    <div class="check-item">
      <div class="check-icon">✓</div>
      <div class="check-text">워셔액 보충</div>
    </div>
    <div class="check-item" style="grid-column: 1 / -1; justify-content: flex-start;">
      <div class="check-icon">✓</div>
      <div class="check-text">엔진룸 청소</div>
    </div>
  </div>

  <div class="bottom-banner">
    <div class="left">
      <span class="icon">🛡</span>
      <div class="text">
        <div class="main">일반 카센터에서는 별도 요금이 붙거나 아예 없는 서비스</div>
        <div class="sub">카수리는 소모품 교체 1건에 안전점검 전체를 기본 제공합니다</div>
      </div>
    </div>
    <div class="count-badge">
      <span class="num">13~14개</span>무상 점검
    </div>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 800})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\body-6.png", full_page=True)
    browser.close()
print("body-6.png 완료")
