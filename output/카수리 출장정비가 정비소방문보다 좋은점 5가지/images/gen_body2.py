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
    margin-bottom: 50px;
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
  .header h2 span {
    color: #1565C0;
  }
  .compare-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 24px rgba(21,101,192,0.1);
  }
  .compare-table thead tr {
    background: #1565C0;
  }
  .compare-table thead th {
    padding: 26px 20px;
    font-size: 26px;
    font-weight: 800;
    color: white;
    text-align: center;
    letter-spacing: 0.5px;
  }
  .compare-table thead th:first-child {
    background: #0d47a1;
    color: rgba(255,255,255,0.9);
  }
  .compare-table thead th.highlight {
    background: #FF6B35;
  }
  .compare-table tbody tr {
    background: white;
  }
  .compare-table tbody tr:nth-child(even) {
    background: #f5f9ff;
  }
  .compare-table tbody tr:hover {
    background: #eef5ff;
  }
  .compare-table tbody td {
    padding: 28px 24px;
    font-size: 24px;
    color: #333;
    text-align: center;
    border-bottom: 1px solid #e0ecf8;
    line-height: 1.5;
  }
  .compare-table tbody td:first-child {
    font-weight: 800;
    color: #1a2e3a;
    background: #f0f7ff;
    border-right: 2px solid #b3d9f5;
  }
  .compare-table tbody td.bad {
    color: #888;
  }
  .compare-table tbody td.good {
    color: #1565C0;
    font-weight: 700;
  }
  .compare-table tbody td .good-tag {
    display: inline-block;
    background: #e8f4fd;
    color: #1565C0;
    font-size: 20px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 20px;
    border: 1.5px solid #b3d9f5;
  }
  .compare-table tbody td .bad-tag {
    display: inline-block;
    background: #f5f5f5;
    color: #999;
    font-size: 20px;
    font-weight: 500;
    padding: 4px 14px;
    border-radius: 20px;
    border: 1.5px solid #ddd;
  }
  .compare-table tbody tr:last-child td {
    border-bottom: none;
  }
  .summary {
    margin-top: 36px;
    background: linear-gradient(90deg, #e8f4fd, #daeeff);
    border-radius: 14px;
    padding: 24px 36px;
    display: flex;
    align-items: center;
    gap: 16px;
    border-left: 6px solid #1565C0;
  }
  .summary .icon { font-size: 32px; }
  .summary .text {
    font-size: 24px;
    color: #1a2e3a;
    font-weight: 700;
    line-height: 1.5;
  }
  .summary .text span { color: #1565C0; }
</style>
</head>
<body>
  <div class="header">
    <div class="tag">🚗 장점 1 — 이동 편의성</div>
    <h2>이동이 <span>사라지는</span> 경험</h2>
  </div>

  <table class="compare-table">
    <thead>
      <tr>
        <th style="width:22%">구분</th>
        <th style="width:39%">정비소 방문</th>
        <th class="highlight" style="width:39%">✅ 카수리 출장정비</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>이동</td>
        <td class="bad"><span class="bad-tag">❌ 직접 운전해서 이동</span></td>
        <td class="good"><span class="good-tag">✅ 이동 없음</span></td>
      </tr>
      <tr>
        <td>장소</td>
        <td class="bad"><span class="bad-tag">정비소 지정 위치</span></td>
        <td class="good"><span class="good-tag">집 · 회사 주차장</span></td>
      </tr>
      <tr>
        <td>작업 중</td>
        <td class="bad"><span class="bad-tag">정비소에서 대기</span></td>
        <td class="good"><span class="good-tag">업무 · 일상 계속</span></td>
      </tr>
      <tr>
        <td>복귀</td>
        <td class="bad"><span class="bad-tag">❌ 다시 이동 필요</span></td>
        <td class="good"><span class="good-tag">✅ 불필요</span></td>
      </tr>
    </tbody>
  </table>

  <div class="summary">
    <span class="icon">💡</span>
    <div class="text">
      정비사가 <span>고객 쪽으로 이동</span>하는 방식 — 이동 시간 제로, 기다림 제로
    </div>
  </div>
</body>
</html>"""

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1080, "height": 700})
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path=r"d:\Dropbox\Ai study\2606_데키랩_블로그글쓰기에이전트\blog\output\카수리 출장정비가 정비소방문보다 좋은점 5가지\images\body-2.png", full_page=True)
    browser.close()
print("body-2.png 완료")
