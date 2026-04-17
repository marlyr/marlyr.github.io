# Marly Rubin

![Marly Rubin](images/me.jpeg)

## About Me

I am a postbac researcher at the NIH in the NIMH/Section on Functional Imaging Methods.
My work involves neuroimaging analysis and developing software for real-time fMRI processing. 
I'm interested in building tools to support scientific research.

In my free time, I enjoy figure skating, playing guitar, coding, and <a href="#" onclick="toggleArt(); return false;">drawing</a>.

<div class="art-grid" id="art-grid">
  <div class="art-thumb" onclick="openLightbox('/images/art/beckett.webp')">
    <img src="/images/art/beckett.webp" alt="samuel beckett">
    <span class="art-caption">samuel beckett</span>
  </div>
  <div class="art-thumb" onclick="openLightbox('/images/art/diogenes.webp')">
    <img src="/images/art/diogenes.webp" alt="diogenes">
    <span class="art-caption">diogenes</span>
  </div>
</div>
<div class="lightbox" id="lightbox" onclick="closeLightbox()">
  <img id="lightbox-img" src="" alt="art">
</div>

## Skills

- Python (NumPy, pandas, scikit-learn, nibabel, Nilearn, etc.)
- Bash, Linux, HPC
- Currently learning: React, TypeScript, FastAPI

---

<a href="https://github.com/marlyr">
  <i class="fab fa-github"></i> GitHub
</a> |
<a href="https://www.linkedin.com/in/marly-rubin-85043022b">
  <i class="fab fa-linkedin"></i> LinkedIn
</a>

<script>
function toggleArt() {
  document.getElementById('art-grid').classList.toggle('active');
}
function openLightbox(src) {
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox').classList.add('active');
}
function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
}
</script>
