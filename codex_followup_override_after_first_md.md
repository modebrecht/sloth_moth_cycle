# Codex Follow-up Patch: Override Previous Listening Instructions

## Important

I already gave you an earlier Markdown instruction for the Listening slide.

This document **overrides the earlier instruction** where it differs.

Keep the useful parts from the first instruction:

- 4 speed buttons:
  - 🐌 0.6x
  - 🐢 0.8x
  - 🎧 1.0x Normal
  - ⚡ 1.2x
- `setListenRate(...)`
- active speed button styling
- no duplicate `playListening()` / `stopListening()` / `let utterance`
- transcript should use `moth`, not `sloth moth`
- transcript should use `dung`, not `poop`

But update the task structure as follows.

---

## Final Listening Slide Structure

Use:

- **5 Missing Word questions**
- **6 Order Quiz steps**

Do **not** use:

- 5 Missing Words + 8 Order Steps
- 6 Missing Words + 6 Order Steps
- any `poop`
- any `sloth moth`
- any `female sloth moth`

---

## Final Transcript

Replace the listening transcript with:

```html
<p id="listeningText">A moth lives in the fur of a sloth. About once a week, the sloth climbs down from the trees to leave dung on the ground. This is dangerous, because other animals may attack the sloth. When the sloth is on the ground, some moths leave the fur. They lay eggs in the fresh dung. The eggs hatch into larvae. Larvae are young moths. They feed and grow in the dung. Later, the larvae become adult moths. The adult moths fly back into the trees and find a sloth. In the fur, the moths may help algae grow. Algae can make the sloth’s fur look green. This green colour may help the sloth hide in the rainforest.</p>
```

---

## Final Missing Word Questions

Replace the whole `gapQuiz` block with exactly 5 questions.

Correct answers:

1. `fur`
2. `dung`
3. `larvae`
4. `algae`
5. `green`

Use this HTML:

```html
<div class="gap-quiz" id="gapQuiz">

  <div class="question gap-question" data-answer="fur" data-gap="fur">
    <strong>1) The moth lives in the sloth’s <span class="blank">???</span>.</strong>
    <div class="choice-grid compact gap-options">
      <button class="choice-btn gap-option" data-value="fur" type="button">Fur</button>
      <button class="choice-btn gap-option" data-value="trees" type="button">Trees</button>
      <button class="choice-btn gap-option" data-value="dung" type="button">Dung</button>
      <button class="choice-btn gap-option" data-value="ground" type="button">Ground</button>
    </div>
    <div class="feedback"></div>
  </div>

  <div class="question gap-question" data-answer="dung" data-gap="dung">
    <strong>2) The moths lay eggs in fresh <span class="blank">???</span>.</strong>
    <div class="choice-grid compact gap-options">
      <button class="choice-btn gap-option" data-value="eggs" type="button">Eggs</button>
      <button class="choice-btn gap-option" data-value="dung" type="button">Dung</button>
      <button class="choice-btn gap-option" data-value="fur" type="button">Fur</button>
      <button class="choice-btn gap-option" data-value="algae" type="button">Algae</button>
    </div>
    <div class="feedback"></div>
  </div>

  <div class="question gap-question" data-answer="larvae" data-gap="larvae">
    <strong>3) The eggs hatch into <span class="blank">???</span>.</strong>
    <div class="choice-grid compact gap-options">
      <button class="choice-btn gap-option" data-value="moths" type="button">Moths</button>
      <button class="choice-btn gap-option" data-value="larvae" type="button">Larvae</button>
      <button class="choice-btn gap-option" data-value="sloths" type="button">Sloths</button>
      <button class="choice-btn gap-option" data-value="algae" type="button">Algae</button>
    </div>
    <div class="feedback"></div>
  </div>

  <div class="question gap-question" data-answer="algae" data-gap="algae">
    <strong>4) The moths may help <span class="blank">???</span> grow.</strong>
    <div class="choice-grid compact gap-options">
      <button class="choice-btn gap-option" data-value="trees" type="button">Trees</button>
      <button class="choice-btn gap-option" data-value="eggs" type="button">Eggs</button>
      <button class="choice-btn gap-option" data-value="algae" type="button">Algae</button>
      <button class="choice-btn gap-option" data-value="fur" type="button">Fur</button>
    </div>
    <div class="feedback"></div>
  </div>

  <div class="question gap-question" data-answer="green" data-gap="green">
    <strong>5) Algae can make the sloth’s fur look <span class="blank">???</span>.</strong>
    <div class="choice-grid compact gap-options">
      <button class="choice-btn gap-option" data-value="green" type="button">Green</button>
      <button class="choice-btn gap-option" data-value="red" type="button">Red</button>
      <button class="choice-btn gap-option" data-value="dry" type="button">Dry</button>
      <button class="choice-btn gap-option" data-value="loud" type="button">Loud</button>
    </div>
    <div class="feedback"></div>
  </div>

</div>
```

---

## Final Order Quiz

Replace the whole `orderQuiz` block with exactly 6 steps.

Correct order:

1. A moth lives in the fur of a sloth.
2. The sloth climbs down from the trees to the ground.
3. Some moths leave the sloth’s fur.
4. The moths lay eggs in fresh dung.
5. The eggs hatch into larvae.
6. The larvae become adult moths and fly back to the trees.

Use this HTML:

```html
<div class="timeline order-quiz" id="orderQuiz">

  <div class="timeline-item order-item">
    <select class="order-live" data-answer="4" data-step="4">
      <option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option>
    </select>
    <div>The moths lay eggs in fresh dung.</div>
    <div class="feedback"></div>
  </div>

  <div class="timeline-item order-item">
    <select class="order-live" data-answer="1" data-step="1">
      <option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option>
    </select>
    <div>A moth lives in the fur of a sloth.</div>
    <div class="feedback"></div>
  </div>

  <div class="timeline-item order-item">
    <select class="order-live" data-answer="2" data-step="2">
      <option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option>
    </select>
    <div>The sloth climbs down from the trees to the ground.</div>
    <div class="feedback"></div>
  </div>

  <div class="timeline-item order-item">
    <select class="order-live" data-answer="6" data-step="6">
      <option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option>
    </select>
    <div>The larvae become adult moths and fly back to the trees.</div>
    <div class="feedback"></div>
  </div>

  <div class="timeline-item order-item">
    <select class="order-live" data-answer="3" data-step="3">
      <option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option>
    </select>
    <div>Some moths leave the sloth’s fur.</div>
    <div class="feedback"></div>
  </div>

  <div class="timeline-item order-item">
    <select class="order-live" data-answer="5" data-step="5">
      <option></option><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option>
    </select>
    <div>The eggs hatch into larvae.</div>
    <div class="feedback"></div>
  </div>

</div>
```

---

## Text updates

Change the title to:

```html
<h2>Listen &amp; order: the moth life cycle</h2>
```

Change the lead to:

```html
<p class="lead">Listen to the short text. Then complete five missing words and put the moth life cycle in order.</p>
```

Change the order quiz help text to:

```html
<h3>Order quiz: put the moth life cycle in the correct order</h3>
<p class="micro-help">Choose a number from 1 to 6. Immediate feedback. Every correct step gives <strong>+2 XP</strong>.</p>
```

---

## Final validation

Check that the final HTML has:

- exactly 5 `.gap-question` elements inside `#gapQuiz`
- exactly 6 `.order-item` elements inside `#orderQuiz`
- no `poop`
- no `sloth moth`
- no `female sloth moth`
- dropdown options only from 1 to 6
- four speed buttons still present
- no duplicate JS functions
