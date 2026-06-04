from playwright.sync_api import sync_playwright

html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    width: 1080px;
    background: #f8f9fa;
    font-family: 'Malgun Gothic', 'Apple SD Gothic Neo', sans-serif;
    padding: 60px;
  }
  .header {
    text-align: center;
    margin-bottom: 48px;
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
    font-size: 50px;
    font-weight: 900;
    color: #1a2e3a;
  }
  .header h2 span { color: #1565C0; }
  .columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }
  .col {
    border-radius: 20px;
    padding: 36px 30px;
  }
  .col.left {
    background: white;
    border: 2px solid #e0e0e0;
  }
  .col.right {
    background: linear-gradient(160deg, #e8f4fd, #daeeff);
    border: 2px solid #b3d9f5;
  }
  .col-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 30px;
    padding-bottom: 20px;
    border-bottom: 2px solid;
  }
  .col.left .col-header { border-color: #e0e0e0; }
  .col.right .col-header { border-color: #b3d9f5; }
  .col-header .col-icon { font-size: 32px; }
  .col-header .col-title {
    font-size: 24px;
    font-weight: 800;
  }
  .col.left .col-header .col-title { color: #666; }
  .col.right .col-header .col-title { color: #1565C0; }
  .steps { display: flex; flex-direction: column; gap: 0; }
  .step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    position: relative;
    padding-bottom: 20px;
  }
  .step:last-child { padding-bottom: 0; }
  .step-left {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-width: 36px;
  }
  .step-num {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    font-weight: 800;
    flex-shrink: 0;
  }
  .col.left .step-num { background: #f0f0f0; color: #999; }
  .col.right .step-num { background: #1565C0; color: white; }
  .step-line {
    width: 2px;
    flex: 1;
    margin-top: 4px;
    min-height: 20px;
  }
  .col.left .step-line { background: #e0e0e0; }
  .col.right .step-line { background: #b3d9f5; }
  .step:last-child .step-line { display: none; }
  .step-content {
    padding-top: 4px;
    flex: 1;
  }
  .step-content .step-title {
    font-size: 22px;
    font-weight: 700;
    line-height: 1.3;
    margin-bottom: 4px;
  }
  .col.left .step-title { color: #888; }
  .col.right .step-title { color: #1a2e3a; }
  .step-content .step-time {
    font-size: 19px;
    font-weight: 600;
  }
  .col.left .step-time { color: #aaa; }
  .col.right .step-time { color: #1565C0; }
  .total-box {
    margin-top: 28px;
    padding: 18px 20px;
    border-radius: 12px;
    text-align: center;
  }
  .col.left .total-box {
    background: #f5f5f5;
    border: 1.5px solid #ddd;
  }
  .col.right .total-box {
    background: #1565C0;
  }
  .total-label {
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 6px;
  }
  .col.left .total-label { color: #999; }
  .col.right .total-label { color: rgba(255,255,255,0.85); }
  .total-time {
    font-size: 36px;
    font-weight: 900;
  }
  .col.left .total-time { color: #888; }
  .col.right .total-time { color: white; }
  .col.right .total-time span { font-size: 22px; font-weight: 600; opacity: 0.85; }
  .arrow-badge {
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    top: 50%;
    background: #FF6B35;
    color: white;
    font-size: 28px;
    font-weight: 900;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10;
    box-shadow: 0 4px 12px rgba(255,107,53,0.4);
  }
  .columns-wrapper { position: relative; }
  .bottom-bar {
    margin-top: 32px;
    background: white;
    border-radius: 14px;
    padding: 20px 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    border: 2px solid #e8f4fd;
    box-shadow: 0 2px 12px rgba(21,101,192,0.06);
  }
  .bottom-bar .icon { font-size: 28px; }
  .bottom-bar .text {
    font-size: 24px;
    color: #1a2e3a;
    font-weight: 700;
  }
  .bottom-bar .text span { color: #1565C0; }
</style>
</head>
<body>
  <div class="header">
    <div class="tag">⏱ 장점 2 — 시간 절약</div>
    <h2>같은 정비, <span>다른 시간</span></h2>
  </div>

  <div class="columns-wrapper">
    <div class="columns">
      <div class="col left">
        <div class="col-header">
          <span class="col-icon">🏪</span>
          <span class="col-title">정비소 방문</span>
        </div>
        <div class="steps">
          <div class="step">
            <div class="step-left">
              <div class="step-num">1</div>
              <div class="step-line" style="height:36px"></div>
            </div>
            <div class="step-content">
              <div class="step-title">정비소까지 이동</div>
              <div class="step-time">약 30분</div>
            </div>
          </div>
          <div class="step">
            <div class="step-left">
              <div class="step-num">2</div>
              <div class="step-line" style="height:36px"></div>
            </div>
            <div class="step-content">
              <div class="step-title">정비소 대기</div>
              <div class="step-time">약 1시간</div>
            </div>
          </div>
          <div class="step">
            <div class="step-left">
              <div class="step-num">3</div>
              <div class="step-line" style="height:36px"></div>
            </div>
            <div class="step-content">
              <div class="step-title">실제 작업</div>
              <div class="step-time">약 40분</div>
            </div>
          </div>
          <div class="step">
            <div class="step-left">
              <div class="step-num">4</div>
            </div>
            <div class="step-content">
              <div class="step-title">집으로 복귀</div>
              <div class="step-time">약 30분</div>
            </div>
          </div>
        </div>
        <div class="total-box">
          <div class="total-label">총 소요 시간</div>
          <div class="total-time">2시간 40분+</div>
        </div>
      </div>

      <div class="col right">
        <div class="col-header">
          <span class="col-icon">✅</span>
          <span class="col-title">카수리 출장정비</span>
        </div>
        <div class="steps">
          <div class="step">
            <div class="step-left">
              <div class="step-num">1</div>
              <div class="step-line" style="height:36px"></div>
            </div>
            <div class="step-content">
              <div class="step-title">앱으로 예약</div>
              <div class="step-time">3분</div>
            </div>
          </div>
          <div class="step">
            <div class="step-left">
              <div class="step-num">2</div>
              <div class="step-line" style="height:36px"></div>
            </div>
            <div class="step-content">
              <div class="step-title">정비사 방문 (내가 이동 없음)</div>
              <div class="step-time">—</div>
            </div>
          </div>
          <div class="step">
            <div class="step-left">
              <div class="step-num">3</div>
            </div>
            <div class="step-content">
              <div class="step-title">작업 완료</div>
              <div class="step-time">약 40분</div>
            </div>
          </div>
        </div>
        <div class="total-box">
          <div class="total-label">총 소요 시간</div>
          <div class="total-time">40분 <span>끝</span></div>
        </div>
      </div>
    </div>
  </div>

  <div class="bottom-bar">
    <span class="icon">🎯</span>
    <div class="text">이동 없이 <span>작업 시간 40분만</span> — 바쁜 직장인에게 진짜 시간 절약</div>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 750})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\body-3.png", full_page=True)
    browser.close()
print("body-3.png 완료")
