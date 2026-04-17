# Marly Rubin

![Marly Rubin](images/me.jpeg)

## About Me

I am a postbac researcher at the NIH in the NIMH/Section on Functional Imaging Methods.
My work involves neuroimaging analysis and developing software for real-time fMRI processing. 
I'm interested in building tools to support scientific research.

In my free time, I enjoy figure skating, playing guitar, and coding.

## Skills

- Python (NumPy, pandas, scikit-learn, nibabel, Nilearn, etc.)
- Bash, Linux, HPC
- Currently learning: React, TypeScript, FastAPI

<a href="https://github.com/marlyr">
  <i class="fab fa-github"></i> GitHub
</a> |
<a href="https://www.linkedin.com/in/marly-rubin-85043022b">
  <i class="fab fa-linkedin"></i> LinkedIn
</a>

<div class="art-section">
  <button class="art-toggle-btn" onclick="toggleArt()">
    <img src="/images/art/art.png" alt="my art">
    <span>my art</span>
  </button>
  <div class="art-grid" id="art-grid">
    <div class="art-thumb" onclick="openLightbox('/images/art/beckett.webp')">
      <img src="/images/art/beckett.webp" alt="samuel beckett">
      <span class="art-caption">samuel beckett</span>
    </div>
    <div class="art-thumb" onclick="openLightbox('/images/art/soldier.webp')">
      <img src="/images/art/soldier.webp" alt="soldier + dog in gas masks">
      <span class="art-caption">soldier + dog in gas masks</span>
    </div>
    <div class="art-thumb" onclick="openLightbox('/images/art/diogenes.webp')">
      <img src="/images/art/diogenes.webp" alt="diogenes">
      <span class="art-caption">diogenes</span>
    </div>
  </div>
  <div class="lightbox" id="lightbox" onclick="closeLightbox()">
    <img id="lightbox-img" src="" alt="art">
  </div>
</div>

<script>
function toggleArt() {
  const grid = document.getElementById('art-grid');
  const btn = document.querySelector('.art-toggle-btn');
  const isActive = grid.classList.contains('active');
  grid.classList.toggle('active', !isActive);
  btn.classList.toggle('active', !isActive);
}
function openLightbox(src) {
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox').classList.add('active');
}
function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
}
</script>
