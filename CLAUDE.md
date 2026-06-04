# 블로그 글 작성 자동화 시스템

주제를 받으면 서브 에이전트들을 순서대로 호출해 리서치→글쓰기→이미지→통합까지 자동으로 처리한다.

---

## 폴더 구조

```
agents/       각 서브 에이전트 정의 (researcher, writer, image-maker, assembler)
guides/       에이전트가 따르는 규칙 파일 (style-guide, seo-guide, image-guide)
output/[주제]/  주제별 산출물 (research.md, draft.md, images/, final.md, final.html)
```

---

## 작업 흐름 (주제가 주어지면 이 순서대로)

**Step 1 — 리서치** (`agents/researcher.md` 위임)
→ `output/[주제]/research.md` 생성
→ 완료 후 사용자에게 소스 수, 주요 발견 보고

**Step 2 — 글쓰기** (`agents/writer.md` 위임)
→ `guides/style-guide.md` + `guides/seo-guide.md` + `research.md` 기반으로 초고 작성
→ `output/[주제]/draft.md` 생성
→ 완료 후 제목, 글자 수 보고

**Step 3 — 이미지 제작** (`agents/image-maker.md` 위임)
→ `guides/image-guide.md` 기반, draft.md의 `[IMAGE: ...]` 마커마다 PNG 생성
→ `output/[주제]/images/` 저장 + draft.md 마커 치환
→ 완료 후 생성 이미지 수, 검수 결과 보고

**Step 4 — 통합** (`agents/assembler.md` 위임)
→ `output/[주제]/final.md` + `output/[주제]/final.html` 생성
→ 완료 후 사용자에게 final.html을 브라우저로 열어보도록 안내

---

## 규칙

- 메인(오케스트레이터)은 **직접 글을 쓰거나 리서치하지 않는다.** 모든 실작업은 서브 에이전트에게 위임한다.
- 각 Step 완료마다 사용자에게 한 줄 진행 상황을 알린다.
- 서브 에이전트 호출 전에 해당 `agents/*.md` 파일을 읽고 지시를 따른다.
