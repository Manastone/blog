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

  .quote-box {
    background: #e8f4fd;
    border-left: 8px solid #1565C0;
    border-radius: 0 20px 20px 0;
    padding: 44px 50px;
    margin-bottom: 32px;
    position: relative;
  }
  .quote-mark {
    font-size: 100px;
    color: #1565C0;
    opacity: 0.18;
    position: absolute;
    top: 10px;
    left: 20px;
    line-height: 1;
    font-family: Georgia, serif;
  }
  .quote-text {
    font-size: 38px;
    font-weight: 900;
    color: #1a2e3a;
    line-height: 1.5;
    position: relative;
    z-index: 1;
    padding-left: 20px;
  }
  .quote-sub {
    margin-top: 20px;
    font-size: 23px;
    color: #3a5a70;
    font-weight: 500;
    padding-left: 20px;
    line-height: 1.7;
    position: relative;
    z-index: 1;
  }
  .tags-row {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 32px;
  }
  .tag-item {
    display: flex;
    align-items: center;
    gap: 8px;
    background: white;
    border: 2px solid #b3d9f5;
    border-radius: 50px;
    padding: 14px 26px;
    font-size: 22px;
    font-weight: 700;
    color: #1a2e3a;
    box-shadow: 0 2px 10px rgba(21,101,192,0.07);
    flex: 1;
    justify-content: center;
  }
  .tag-item .check {
    color: #1565C0;
    font-size: 22px;
  }
  .info-box {
    background: white;
    border-radius: 16px;
    padding: 30px 36px;
    border: 2px solid #e0ecf8;
    display: flex;
    align-items: flex-start;
    gap: 18px;
  }
  .info-icon { font-size: 36px; flex-shrink: 0; margin-top: 2px; }
  .info-content {}
  .info-title {
    font-size: 22px;
    font-weight: 800;
    color: #1565C0;
    margin-bottom: 8px;
  }
  .info-desc {
    font-size: 21px;
    color: #4a6a80;
    line-height: 1.7;
  }
</style>
</head>
<body>
  <div class="header">
    <div class="tag">👁 장점 3 — 작업 투명성</div>
    <h2>정비 과정을 <span>눈으로 직접</span> 확인</h2>
  </div>

  <div class="quote-box">
    <div class="quote-mark">"</div>
    <div class="quote-text">"내 차에 뭘 넣는지,<br>눈으로 직접 봤습니다"</div>
    <div class="quote-sub">
      정비사가 고객 바로 앞에서 작업 · 오일 종류·필터 상태·배터리 수치 현장 설명
    </div>
  </div>

  <div class="tags-row">
    <div class="tag-item"><span class="check">✅</span> 작업 현장 공개</div>
    <div class="tag-item"><span class="check">✅</span> 부품 정보 투명 공개</div>
    <div class="tag-item"><span class="check">✅</span> 전후 상태 설명</div>
  </div>

  <div class="info-box">
    <span class="info-icon">💡</span>
    <div class="info-content">
      <div class="info-title">정보 비대칭이 사라집니다</div>
      <div class="info-desc">
        카센터에서 전문 용어로 설명을 들어도 정확히 이해가 안 되던 경험, 카수리는 다릅니다.<br>
        작업 전후 차량 상태를 이해하기 쉽게 설명해줬다는 이용 후기가 많은 이유입니다.
      </div>
    </div>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\body-4.png", full_page=True)
    browser.close()
print("body-4.png 완료")
