# Codex Task: Improve Listening Slide

## Goal

Update the **Listening** slide in `index.html`.

We want:

1. A clearer, classroom-friendly transcript.
2. No confusing term **"sloth moth"**.
3. No **"female sloth moth"**.
4. Use **"moth"** only.
5. Use **"dung"** only. Do not use **"poop"**.
6. Add four listening speed buttons:
   - 🐌 0.6x
   - 🐢 0.8x
   - 🎧 1.0x Normal
   - ⚡ 1.2x
7. The selected speed should be used when the browser reads the transcript aloud.
8. If speech is already playing and a new speed is selected, restart the listening with the new speed.

---

## 1. Replace the listening transcript

Find this element:

```html
<p id="listeningText">...</p>
```

Replace the full content with this:

```html
<p id="listeningText">A moth lives in the fur of a sloth. About once a week, the sloth climbs down from the trees to leave dung on the ground. This is dangerous, because other animals may attack the sloth. When the sloth is on the ground, some moths leave the fur. They lay eggs in the fresh dung. The eggs hatch into larvae. Larvae are young moths. They feed and grow in the dung. Later, the larvae become adult moths. The adult moths fly back into the trees and find a sloth. In the fur, the moths may help algae grow. Algae can make the sloth’s fur look green. This green colour may help the sloth hide in the rainforest.</p>
```

### Important transcript rules

Do **not** use:

- `female sloth moth`
- `sloth moth`
- `poop`
- `canopy`
- `predators`

Use:

- `moth`
- `dung`
- `trees`
- `other animals may attack`

---

## 2. Replace the listening controls

Find the current listening controls near the transcript.

Replace this area:

```html
<div class="pillbox listening-controls">
  <button onclick="playListening()" type="button">▶️ Play listening</button>
  <button class="secondary" onclick="stopListening()" type="button">⏹ Stop</button>
</div>
```

with this:

```html
<div class="pillbox listening-controls">
  <button class="plain speed-btn" onclick="setListenRate(0.6, this)" type="button">🐌 0.6x</button>
  <button class="plain speed-btn" onclick="setListenRate(0.8, this)" type="button">🐢 0.8x</button>
  <button class="plain speed-btn active" onclick="setListenRate(1.0, this)" type="button">🎧 1.0x Normal</button>
  <button class="plain speed-btn" onclick="setListenRate(1.2, this)" type="button">⚡ 1.2x</button>
  <button onclick="playListening()" type="button">▶️ Play listening</button>
  <button class="secondary" onclick="stopListening()" type="button">⏹ Stop</button>
</div>
<p class="micro-help" id="listenRateLabel">Speed: 🎧 1.0x Normal</p>
```

---

## 3. Update missing-word question 2

The current version still uses `poop`.

Find this block:

```html
<div class="question gap-question" data-answer="poop" data-gap="poop">
  <strong>2) About once a week, the sloth climbs down to <span class="blank">???</span> at the base of a tree.</strong>
  <div class="choice-grid compact gap-options">
    <button class="choice-btn gap-option" data-value="swim" type="button">Swim</button>
    <button class="choice-btn gap-option" data-value="poop" type="button">Poop</button>
    <button class="choice-btn gap-option" data-value="sing" type="button">Sing</button>
    <button class="choice-btn gap-option" data-value="sleep" type="button">Sleep</button>
  </div><div class="feedback"></div>
</div>
```

Replace with:

```html
<div class="question gap-question" data-answer="dung" data-gap="dung">
  <strong>2) About once a week, the sloth climbs down to leave <span class="blank">???</span> on the ground.</strong>
  <div class="choice-grid compact gap-options">
    <button class="choice-btn gap-option" data-value="eggs" type="button">Eggs</button>
    <button class="choice-btn gap-option" data-value="dung" type="button">Dung</button>
    <button class="choice-btn gap-option" data-value="fur" type="button">Fur</button>
    <button class="choice-btn gap-option" data-value="algae" type="button">Algae</button>
  </div><div class="feedback"></div>
</div>
```

---

## 4. Replace the current speech synthesis JS

Find the current code that looks like this:

```js
let utterance;
function playListening(){
  if(!('speechSynthesis' in window)){
    alert('Speech is not supported in this browser. Please read the transcript aloud.');
    return;
  }
  stopListening();
  utterance = new SpeechSynthesisUtterance($('#listeningText').textContent);
  utterance.lang = 'en-GB';
  utterance.rate = 0.88;
  speechSynthesis.speak(utterance);
}
function stopListening(){
  if('speechSynthesis' in window) speechSynthesis.cancel();
}
```

Replace with:

```js
let utterance;
let listenRate = 1.0;

function setListenRate(rate, btn){
  listenRate = rate;

  const label = $('#listenRateLabel');
  if(label){
    const labelText =
      rate === 0.6 ? 'Speed: 🐌 0.6x' :
      rate === 0.8 ? 'Speed: 🐢 0.8x' :
      rate === 1.2 ? 'Speed: ⚡ 1.2x' :
      'Speed: 🎧 1.0x Normal';

    label.textContent = labelText;
  }

  $$('.speed-btn').forEach(button => button.classList.remove('active'));
  if(btn) btn.classList.add('active');

  if('speechSynthesis' in window && speechSynthesis.speaking){
    playListening();
  }
}

function playListening(){
  if(!('speechSynthesis' in window)){
    alert('Speech is not supported in this browser. Please read the transcript aloud.');
    return;
  }

  stopListening();

  const text = $('#listeningText')?.textContent?.trim();
  if(!text) return;

  utterance = new SpeechSynthesisUtterance(text);
  utterance.lang = 'en-GB';
  utterance.rate = listenRate;
  utterance.pitch = 1;
  utterance.volume = 1;

  speechSynthesis.speak(utterance);
}

function stopListening(){
  if('speechSynthesis' in window) speechSynthesis.cancel();
}
```

---

## 5. Add optional CSS for active speed button

Add this to the CSS if no active state exists yet:

```css
.speed-btn.active{
  background:linear-gradient(135deg,#ffefc8,#fff7e8);
  border-color:#ffcc66;
  box-shadow:0 0 0 4px rgba(255,204,102,.18),0 10px 22px rgba(122,72,21,.12);
  color:#6b4210;
}
```

---

## 6. Final checks

After the changes, verify:

- The transcript says **moth**, not **sloth moth**.
- The transcript says **dung**, not **poop**.
- Question 2 uses **dung** as answer.
- The four speed buttons appear:
  - 🐌 0.6x
  - 🐢 0.8x
  - 🎧 1.0x Normal
  - ⚡ 1.2x
- The default speed is **1.0x Normal**.
- Clicking a speed button updates the label.
- Clicking a speed button while audio is playing restarts the audio with the new speed.
- Play and Stop still work.
