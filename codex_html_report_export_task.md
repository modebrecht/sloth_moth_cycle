# Codex Task: Rename PDF Export to HTML Report and Export All Student Work

## Goal

The current export is technically **not a PDF**.

The current code creates an HTML file and downloads it as:

```js
sloth-moth-final-${Date.now()}.html
```

So the UI should no longer say **PDF**.

Rename the feature everywhere to:

```txt
Download HTML Report
```

The exported file should be a clean, teacher-readable HTML report containing all student work from the activity.

---

## 1. Rename all user-facing PDF labels

Find all buttons, labels, helper text, toast messages, comments, and UI text that say:

```txt
PDF
PDF herunterladen
PDF downloaded
PDF generation failed
PDF unlock requirements
```

Replace them with HTML Report wording.

Use these exact user-facing labels:

```txt
Download HTML Report
HTML Report downloaded ✅
HTML Report export failed ❌
HTML Report unlock requirements not met ❌
```

Examples:

### Header button

Change:

```html
<button class="ghost export-locked" data-final-export id="headerPdfBtn" onclick="requestPDF()" disabled>🔒 PDF · 100 XP</button>
```

to:

```html
<button class="ghost export-locked" data-final-export id="headerReportBtn" onclick="downloadHTMLReport()" disabled>🔒 HTML Report · 100 XP</button>
```

### Final slide button

Change:

```html
<button class="secondary" id="finalPdfBtn2" onclick="requestPDF()">PDF herunterladen</button>
```

to:

```html
<button class="secondary" id="finalHtmlReportBtn" onclick="downloadHTMLReport()">Download HTML Report</button>
```

### Helper text

Change:

```html
Download your worksheet (PDF or JSON) for this activity.
```

to:

```html
Download your worksheet as an HTML Report or JSON for this activity.
```

Keep the JSON button.

---

## 2. Rename the JavaScript function

Rename:

```js
function requestPDF()
```

to:

```js
function downloadHTMLReport()
```

Update every caller:

```js
onclick="requestPDF()"
```

to:

```js
onclick="downloadHTMLReport()"
```

Important:

Do not leave duplicate functions.  
There should be only one export function for the HTML report.

Optional compatibility wrapper:

If needed, this is acceptable temporarily:

```js
function requestPDF(){
  downloadHTMLReport();
}
```

But preferred final result is: no old `requestPDF()` calls remain in the HTML.

---

## 3. Keep the exported file as HTML

The export should still create an HTML file.

Keep this file extension:

```txt
.html
```

Use a better filename:

```js
a.download = `sloth-moth-html-report-${Date.now()}.html`;
```

Do **not** try to generate a real PDF in this task.

Reason:

- HTML export is more reliable for this interactive worksheet.
- Textarea contents will not be cut off.
- The teacher can open the report in any browser.
- If needed, the teacher or student can print the HTML report to PDF from the browser.

---

## 4. Export all student-filled content

The HTML Report must include all relevant student work, not only the final writing task.

Include at least:

### Text areas

- `#predictionBox`
- `#surpriseBox`
- `#evidenceBox`
- `#finalText`

### Research fields

- `#fact1`
- `#source1`
- `#fact2`
- `#source2`

### Self-checks

All `.selfcheck` checkbox states.

### XP and timestamp

- current XP
- generated timestamp
- final word count

### Quiz / activity state

Also include the student's selected answers where available:

- selected Missing Words answers
- Order Quiz dropdown choices
- Symbiosis / Who benefits dropdown choices
- Reading check selected answers if they exist as radio/checkbox inputs
- any other checked radio/checkbox input in the activity

---

## 5. Add a generic form-state collector

Add a helper function that safely collects all filled form elements.

Use this approach:

```js
function collectAllFormState(){
  const fields = [];

  document.querySelectorAll('textarea, input, select').forEach((el) => {
    if(!el.id && !el.name && !el.className) return;

    const label =
      el.closest('.question')?.querySelector('strong')?.textContent?.trim()
      || el.closest('section')?.querySelector('h2')?.textContent?.trim()
      || el.id
      || el.name
      || el.className
      || el.tagName;

    let value = '';

    if(el.type === 'checkbox'){
      value = el.checked ? 'checked' : 'not checked';
    }else if(el.type === 'radio'){
      if(!el.checked) return;
      value = el.value || 'selected';
    }else{
      value = el.value || '';
    }

    fields.push({
      label,
      id: el.id || '',
      name: el.name || '',
      type: el.type || el.tagName.toLowerCase(),
      value
    });
  });

  return fields;
}
```

This function does not need to replace the existing structured export.  
It should supplement it, so the report captures everything even if new fields are added later.

---

## 6. Escape HTML before inserting student content

Do not insert raw student text into the exported HTML.

Add this helper:

```js
function escapeHTML(value){
  return String(value ?? '')
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#039;');
}
```

Use `escapeHTML(...)` for every student-generated value.

Important:

Student writing may contain `<`, `>`, quotes, or copied text.  
The HTML Report must not break.

---

## 7. Build a cleaner HTML Report

The exported HTML Report should be a standalone readable page.

It should include:

- title
- timestamp
- XP
- word count
- Prediction
- Three surprising things
- Evidence reflection
- Research findings
- Final explanation
- Self-check results
- Activity answers / form state
- Print button at the top

The report does not need to include all slides or all decorative images.

Use a clean report layout.

Suggested structure:

```html
<h1>Sloth, Moth & Algae – HTML Report</h1>
<p class="timestamp">Generated: ...</p>
<p class="meta">XP earned: ... · Final word count: ...</p>

<section>
  <h2>Prediction</h2>
  <p>...</p>
</section>

<section>
  <h2>Three Surprising Things</h2>
  <p>...</p>
</section>

<section>
  <h2>Evidence Reflection</h2>
  <p>...</p>
</section>

<section>
  <h2>Research Findings</h2>
  ...
</section>

<section>
  <h2>Final Explanation</h2>
  ...
</section>

<section>
  <h2>Self-Check Results</h2>
  ...
</section>

<section>
  <h2>All Activity Answers</h2>
  ...
</section>
```

---

## 8. Suggested `downloadHTMLReport()` structure

Replace the old `requestPDF()` function with a function like this:

```js
function downloadHTMLReport(){
  try{
    const finalText = $('#finalText');
    const wordCountFinal = wordCount(finalText.value);
    const allChecks = $$('.selfcheck').every(c => c.checked);
    const hasMinWords = wordCountFinal >= 120;

    if(xp < 100 || !hasMinWords || !allChecks){
      showToast('HTML Report unlock requirements not met ❌');
      return;
    }

    const checks = $$('.selfcheck').map((c,i) => {
      const labels = [
        'Used 5+ vocab words',
        'Explained 2+ benefits',
        'Used careful language',
        'Wrote 2+ research facts'
      ];
      return `${c.checked ? '✅' : '⬜'} ${labels[i] || `Self-check ${i+1}`}`;
    });

    const allFields = collectAllFormState();

    const allFieldsHTML = allFields.map(field => `
      <tr>
        <th>${escapeHTML(field.label)}</th>
        <td>${escapeHTML(field.value || '(empty)')}</td>
      </tr>
    `).join('');

    const htmlContent = `
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sloth, Moth & Algae – HTML Report</title>
  <style>
    body{
      font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
      margin:0;
      padding:40px;
      line-height:1.6;
      color:#17352a;
      background:#f6fff5;
    }
    main{
      max-width:900px;
      margin:0 auto;
      background:white;
      border:1px solid #d8e9dd;
      border-radius:24px;
      padding:34px;
      box-shadow:0 18px 42px rgba(16,41,31,.10);
    }
    h1{
      margin:0 0 8px;
      color:#10291f;
      line-height:1.1;
    }
    h2{
      margin-top:28px;
      color:#1e6046;
      border-bottom:2px solid #d8e9dd;
      padding-bottom:6px;
    }
    .timestamp,.meta{
      color:#5f766d;
      font-weight:650;
    }
    .section{
      margin:18px 0;
      padding:16px;
      border-left:5px solid #6fcf7d;
      background:#f6fff5;
      border-radius:14px;
    }
    .answer{
      white-space:pre-wrap;
    }
    table{
      width:100%;
      border-collapse:collapse;
      margin-top:14px;
    }
    th,td{
      text-align:left;
      vertical-align:top;
      border-bottom:1px solid #d8e9dd;
      padding:10px;
    }
    th{
      width:34%;
      color:#315548;
      background:#f8fff8;
    }
    .print-btn{
      margin:18px 0 26px;
      padding:10px 16px;
      border-radius:999px;
      border:1px solid #cfe5d2;
      background:#eff9f0;
      color:#245a3e;
      font-weight:800;
      cursor:pointer;
    }
    @media print{
      body{background:white;padding:0;}
      main{box-shadow:none;border:none;border-radius:0;}
      .print-btn{display:none;}
    }
  </style>
</head>
<body>
<main>
  <h1>🦥 Sloth, Moth & Algae – HTML Report</h1>
  <p class="timestamp">Generated: ${escapeHTML(new Date().toLocaleString())}</p>
  <p class="meta">XP earned: ${escapeHTML(xp)} · Final word count: ${escapeHTML(wordCountFinal)}</p>

  <button class="print-btn" onclick="window.print()">Print / Save as PDF</button>

  <section class="section">
    <h2>Prediction</h2>
    <p class="answer">${escapeHTML($('#predictionBox').value.trim() || '(not filled)')}</p>
  </section>

  <section class="section">
    <h2>Three Surprising Things</h2>
    <p class="answer">${escapeHTML($('#surpriseBox').value.trim() || '(not filled)')}</p>
  </section>

  <section class="section">
    <h2>Evidence Reflection</h2>
    <p class="answer">${escapeHTML($('#evidenceBox').value.trim() || '(not filled)')}</p>
  </section>

  <section class="section">
    <h2>Research Findings</h2>
    <p><strong>Fact 1:</strong> ${escapeHTML($('#fact1').value.trim() || '(not filled)')}</p>
    <p><strong>Source 1:</strong> ${escapeHTML($('#source1').value.trim() || '(not filled)')}</p>
    <p><strong>Fact 2:</strong> ${escapeHTML($('#fact2').value.trim() || '(not filled)')}</p>
    <p><strong>Source 2:</strong> ${escapeHTML($('#source2').value.trim() || '(not filled)')}</p>
  </section>

  <section class="section">
    <h2>Final Explanation</h2>
    <p class="answer">${escapeHTML($('#finalText').value.trim() || '(not filled)')}</p>
  </section>

  <section class="section">
    <h2>Self-Check Results</h2>
    <p class="answer">${escapeHTML(checks.join('\n'))}</p>
  </section>

  <section class="section">
    <h2>All Activity Answers</h2>
    <table>
      <tbody>
        ${allFieldsHTML}
      </tbody>
    </table>
  </section>
</main>
</body>
</html>
    `;

    const blob = new Blob([htmlContent], {type: 'text/html'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `sloth-moth-html-report-${Date.now()}.html`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);

    playSoftTone('success');
    showToast('HTML Report downloaded ✅');
    burstConfetti(window.innerWidth/2, window.innerHeight/2, 50);
    showReaction('HTML Report ready! 🏆', window.innerWidth/2, window.innerHeight/2);
  }catch(e){
    console.error('HTML Report export failed:', e);
    showToast('HTML Report export failed ❌');
  }
}
```

---

## 9. Update unlock button logic

If the code updates export button labels dynamically, update those labels too.

Look for code that sets:

```js
PDF
```

or:

```js
PDF · 100 XP
```

or references button IDs like:

```js
headerPdfBtn
finalPdfBtn2
```

Rename them consistently:

```js
headerReportBtn
finalHtmlReportBtn
```

The locked state should say:

```txt
🔒 HTML Report · 100 XP
```

The unlocked state should say:

```txt
Download HTML Report
```

---

## 10. JSON export stays unchanged

Keep the JSON download feature.

Do not remove:

```js
downloadWorksheetJSON()
```

But it is okay to improve the JSON later using the same `collectAllFormState()` helper.

For this task, the priority is the HTML Report.

---

## 11. Final validation checklist

After editing, verify:

### UI wording

There is no visible button or toast saying:

```txt
PDF
```

except inside the optional print button text:

```txt
Print / Save as PDF
```

Allowed:

```txt
Print / Save as PDF
```

Not allowed:

```txt
PDF herunterladen
PDF downloaded
PDF generation failed
```

### Functionality

Clicking **Download HTML Report** downloads an `.html` file.

The file name starts with:

```txt
sloth-moth-html-report-
```

### Report content

The downloaded HTML Report includes:

- Prediction
- Three surprising things
- Evidence reflection
- Research findings
- Final explanation
- Self-checks
- XP
- timestamp
- final word count
- all form/select/radio/checkbox states

### Safety

Student text is escaped with `escapeHTML()`.

### Existing activity

Still working:

- slide navigation
- XP
- final unlock logic
- JSON download
- listening controls
- quizzes
- final task
