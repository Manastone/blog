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
    font-size: 44px;
    font-weight: 900;
    color: #1a2e3a;
    line-height: 1.3;
  }
  .header h2 span { color: #1565C0; }
  .cards-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 24px;
    margin-bottom: 32px;
  }
  .card {
    background: #f8f9fa;
    border-radius: 20px;
    padding: 36px 28px;
    border: 2px solid #e8f0fe;
    text-align: center;
    box-shadow: 0 3px 16px rgba(21,101,192,0.06);
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 14px;
  }
  .card .icon {
    font-size: 52px;
  }
  .card .label {
    font-size: 19px;
    font-weight: 700;
    color: #1565C0;
    background: #e8f4fd;
    padding: 5px 16px;
    border-radius: 20px;
    border: 1.5px solid #b3d9f5;
  }
  .card .title {
    font-size: 24px;
    font-weight: 900;
    color: #1a2e3a;
    line-height: 1.4;
  }
  .card .desc {
    font-size: 19px;
    color: #5a7a90;
    line-height: 1.6;
  }
  .card.highlight {
    background: linear-gradient(160deg, #e8f4fd, #daeeff);
    border-color: #1565C0;
  }
  .card.highlight .title { color: #1565C0; }
  .price-banner {
    background: linear-gradient(90deg, #1565C0, #1976D2);
    border-radius: 16px;
    padding: 28px 40px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
  }
  .price-banner .left {
    display: flex;
    align-items: center;
    gap: 16px;
  }
  .price-banner .icon { font-size: 40px; }
  .price-banner .text {
    color: white;
  }
  .price-banner .text .main {
    font-size: 26px;
    font-weight: 900;
    margin-bottom: 4px;
  }
  .price-banner .text .sub {
    font-size: 20px;
    color: rgba(255,255,255,0.8);
  }
  .price-banner .badge {
    background: #FF6B35;
    color: white;
    font-size: 22px;
    font-weight: 900;
    padding: 12px 28px;
    border-radius: 50px;
    white-space: nowrap;
    box-shadow: 0 4px 12px rgba(255,107,53,0.4);
  }
</style>
</head>
<body>
  <div class="header">
    <div class="tag">💰 장점 4 — 가격 투명성</div>
    <h2>예약할 때 본 금액이<br><span>그대로 청구됩니다</span></h2>
  </div>

  <div class="cards-row">
    <div class="card">
      <span class="icon">💰</span>
      <span class="label">예약 전 확인</span>
      <div class="title">올인원 가격<br>사전 공개</div>
      <div class="desc">오일 + 필터 + 공임 + 출장비<br>모두 포함된 최종 가격을<br>예약 전에 확인 가능</div>
    </div>
    <div class="card highlight">
      <span class="icon">🚫</span>
      <span class="label">추가 청구 없음</span>
      <div class="title">예약 금액 =<br>최종 청구 금액</div>
      <div class="desc">작업 후 추가 공임 없음<br>고지 금액 그대로<br>청구됩니다</div>
    </div>
    <div class="card">
      <span class="icon">📊</span>
      <span class="label">가격 절감</span>
      <div class="title">카센터 대비<br>최대 20% 절약</div>
      <div class="desc">동일 오일 기준<br>약 30% 절감 사례<br>이용자 직접 확인</div>
    </div>
  </div>

  <div class="price-banner">
    <div class="left">
      <span class="icon">✅</span>
      <div class="text">
        <div class="main">숨겨진 비용, 나중에 추가되는 공임 — 없습니다</div>
        <div class="sub">가격이 투명하면 신뢰가 생깁니다. 그것이 이미 상당한 장점입니다.</div>
      </div>
    </div>
    <div class="badge">최대 20% 절약</div>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\body-5.png", full_page=True)
    browser.close()
print("body-5.png 완료")
