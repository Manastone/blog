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
    margin-bottom: 50px;
  }
  .header .tag {
    display: inline-block;
    background: #1565C0;
    color: white;
    font-size: 22px;
    font-weight: 700;
    padding: 8px 24px;
    border-radius: 30px;
    margin-bottom: 20px;
    letter-spacing: 1px;
  }
  .header h2 {
    font-size: 46px;
    font-weight: 900;
    color: #1a2e3a;
    line-height: 1.2;
  }
  .header h2 span {
    color: #1565C0;
  }
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 28px;
  }
  .card {
    background: white;
    border-radius: 20px;
    padding: 40px 36px;
    border: 2px solid #daeeff;
    box-shadow: 0 4px 20px rgba(21,101,192,0.07);
  }
  .card .icon {
    font-size: 48px;
    margin-bottom: 16px;
    display: block;
  }
  .card .label {
    font-size: 22px;
    font-weight: 700;
    color: #1565C0;
    margin-bottom: 12px;
    letter-spacing: 0.5px;
  }
  .card .title {
    font-size: 30px;
    font-weight: 900;
    color: #1a2e3a;
    margin-bottom: 12px;
    line-height: 1.3;
  }
  .card .desc {
    font-size: 22px;
    color: #4a6a80;
    line-height: 1.6;
  }
  .card .desc strong {
    color: #FF6B35;
    font-weight: 700;
  }
  .footer-bar {
    margin-top: 40px;
    background: linear-gradient(90deg, #1565C0, #1976D2);
    border-radius: 14px;
    padding: 22px 36px;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
  }
  .footer-bar span {
    color: white;
    font-size: 24px;
    font-weight: 700;
    letter-spacing: 0.5px;
  }
  .footer-bar .dot {
    color: rgba(255,255,255,0.5);
    font-size: 16px;
  }
</style>
</head>
<body>
  <div class="header">
    <div class="tag">카수리 서비스 소개</div>
    <h2>카수리 출장정비 <span>한눈에 보기</span></h2>
  </div>
  <div class="grid">
    <div class="card">
      <span class="icon">🔧</span>
      <div class="label">취급 항목</div>
      <div class="title">주요 소모품 교체</div>
      <div class="desc">
        엔진오일 · 배터리 · 타이어<br>에어컨 필터 등 소모품 전반
      </div>
    </div>
    <div class="card">
      <span class="icon">📍</span>
      <div class="label">방문 방식</div>
      <div class="title">고객 지정 장소 직접 방문</div>
      <div class="desc">
        집 앞, 회사 주차장, 어디든<br>고객이 있는 곳으로 찾아갑니다
      </div>
    </div>
    <div class="card">
      <span class="icon">⏱</span>
      <div class="label">작업 시간</div>
      <div class="title">평균 <strong>40분</strong> 내외 완료</div>
      <div class="desc">
        이동 없이 작업만 진행<br>바쁜 일상 속 최소 시간 소요
      </div>
    </div>
    <div class="card">
      <span class="icon">✅</span>
      <div class="label">무상 점검</div>
      <div class="title"><strong>13~14개</strong> 항목 기본 포함</div>
      <div class="desc">
        브레이크·배터리·타이어 등<br>안전점검 무상 기본 제공
      </div>
    </div>
  </div>
  <div class="footer-bar">
    <span>누적 출장정비 40만 건</span>
    <span class="dot">●</span>
    <span>고객만족도 99.5%</span>
    <span class="dot">●</span>
    <span>전국 출장 서비스</span>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 750})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\body-1.png", full_page=True)
    browser.close()
print("body-1.png 완료")
