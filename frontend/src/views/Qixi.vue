<template>
  <div class="qixi-page" @click.self="spawnHearts">
    <!-- 背景渐变 -->
    <div class="bg-gradient"></div>

    <!-- 爱心飘落层 -->
    <div class="floating-hearts" id="floatingHearts"></div>

    <!-- BGM 按钮 -->
    <button class="bgm-btn" @click="toggleBgm" :title="bgmPlaying ? '暂停音乐' : '播放音乐'">
      <span v-if="bgmPlaying">🔊</span>
      <span v-else>🔇</span>
    </button>
    <audio ref="bgmAudio" loop preload="auto" style="display:none">
      <source src="/music/shanghaistoneman-qixi-festival-rain-chinese-style-283032.mp3" type="audio/mpeg" />
    </audio>

    <!-- 主内容 -->
    <div class="content">
      <!-- 标题区 -->
      <header class="header">
        <div class="brand-wrap">
          <img src="/logo.svg" alt="yhy & ysy logo" class="brand-logo" />
        </div>
        <h1 class="title">🌙 七夕致我的女孩 🌙</h1>
        <p class="subtitle">
          星河璀璨，鹊桥相连。在这个浪漫的七夕，<br />
          想对你说——你是我写过最美丽的情诗。
        </p>
        <div class="divider">
          <span>❤</span><span>❤</span><span>❤</span>
        </div>
      </header>

      <!-- 图片轮播 -->
      <section class="carousel-section">
        <h2 class="section-title">📸 美好的回忆</h2>
        <div class="carousel">
          <button class="carousel-btn prev" @click="prevImage">‹</button>
          <div class="carousel-viewport">
            <div
              class="carousel-track"
              :style="{ transform: `translateX(-${currentIndex * 100}%)` }"
            >
              <div
                v-for="(img, idx) in imageList"
                :key="idx"
                class="carousel-slide"
              >
                <div class="image-wrapper">
                  <img :src="img" :alt="`回忆 ${idx + 1}`" @load="onImgLoad" />
                </div>
              </div>
            </div>
          </div>
          <button class="carousel-btn next" @click="nextImage">›</button>
        </div>
        <!-- 指示器 -->
        <div class="indicators">
          <span
            v-for="(_, idx) in imageList"
            :key="idx"
            class="dot"
            :class="{ active: idx === currentIndex }"
            @click="currentIndex = idx"
          ></span>
        </div>
      </section>

      <!-- 文字卡片轮播 -->
      <section class="text-section">
        <h2 class="section-title">💌 想对你说的话</h2>
        <div class="text-card" :key="textIndex">
          <transition name="fade" mode="out-in">
            <p class="card-text">{{ currentText }}</p>
          </transition>
        </div>
        <div class="indicators">
          <span
            v-for="(_, idx) in loveTexts"
            :key="idx"
            class="dot text-dot"
            :class="{ active: idx === textIndex }"
            @click="textIndex = idx"
          ></span>
        </div>
      </section>
    </div>

    <!-- 底部 -->
    <footer class="footer">
      <div class="footer-hearts">💕 💕 💕</div>
      <p class="footer-text">— 致 余苏雨 —</p>
      <p class="footer-name">ysy520</p>
      <p class="footer-date">乙巳年七月初七 · 七夕</p>
    </footer>

    <!-- 10秒弹窗 -->
    <transition name="popup">
      <div v-if="showPopup" class="popup-overlay" @click="showPopup = false">
        <div class="popup-card" @click.stop>
          <div class="popup-icon">🥰</div>
          <h3>嗨，你知道吗？</h3>
          <p>
            从遇见你的那一刻起，<br />
            我的世界就不再是黑白。<br /><br />
            你是我每天醒来的理由，<br />
            也是我睡前最后的惦记。<br /><br />
            <strong>七夕快乐，我的女孩 ❤</strong>
          </p>
          <button class="popup-btn" @click="showPopup = false">我知道了 💕</button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue";

// ========== 图片列表 ==========
const images = [
  "mmexport1787045302796.jpg",
  "mmexport1787045334259.jpg",
  "mmexport1787045339303.jpg",
  "mmexport1787045357024.jpg",
  "mmexport1787045376818.jpg",
  "mmexport1787045386868.jpg",
  "mmexport1787045392400.jpg",
  "mmexport1787045394451.jpg",
  "mmexport1787045602082.jpg",
  "mmexport1787045630555.jpg",
  "mmexport1787045673484.jpg",
  "mmexport1787045684072.jpg",
  "mmexport1787045703724.jpg",
  "mmexport1787045714129.jpg",
  "mmexport1787045762817.jpg",
  "mmexport1787045767553.jpg",
  "mmexport1787045770883.jpg",
  "mmexport1787045949092.jpg",
  "mmexport1787045970034.jpg",
  "mmexport1787045983571.jpg",
  "mmexport1787046093830.jpg",
  "mmexport1787046168457.jpg",
  "mmexport1787046172117.jpg",
  "mmexport1787046182735.jpg",
  "mmexport1787046184476.jpg",
];

const imageList = images.map((name) => `/pictures/${name}`);

// ========== 轮播 ==========
const currentIndex = ref(0);
let autoTimer = null;

function nextImage() {
  currentIndex.value = (currentIndex.value + 1) % imageList.length;
}
function prevImage() {
  currentIndex.value =
    (currentIndex.value - 1 + imageList.length) % imageList.length;
}
function startAutoPlay() {
  autoTimer = setInterval(nextImage, 4000);
}
function stopAutoPlay() {
  clearInterval(autoTimer);
}

function onImgLoad() {
  // 图片加载完成后的回调（可留空或用于额外逻辑）
}

// ========== 文字轮播 ==========
const textIndex = ref(0);
let textTimer = null;

const loveTexts = [
  "你是我在茫茫人海中，一眼就认定的人。",
  "想和你一起看遍星河灿烂，走遍山川四季。",
  "你一笑，整个世界的花都开了。",
  "世间万物论沧桑，唯独你是我心尖上的光。",
  "你是我平凡日子里，最惊艳的意外。",
  "想把世界上所有的温柔都攒下来，全部给你。",
  "和你在一起的每一天，都是情人节。",
  "愿有岁月可回首，且以深情共白头。",
];

const currentText = ref(loveTexts[0]);

function nextText() {
  textIndex.value = (textIndex.value + 1) % loveTexts.length;
  currentText.value = loveTexts[textIndex.value];
}
function startTextAutoPlay() {
  textTimer = setInterval(nextText, 5000);
}
function stopTextAutoPlay() {
  clearInterval(textTimer);
}

// ========== BGM 控制 ==========
const bgmPlaying = ref(false);
const bgmAudio = ref(null);

function toggleBgm() {
  if (!bgmAudio.value) return;
  if (bgmPlaying.value) {
    bgmAudio.value.pause();
    bgmPlaying.value = false;
  } else {
    bgmAudio.value.play().catch(() => {
      // 自动播放被浏览器阻止，忽略
    });
    bgmPlaying.value = true;
  }
}

// ========== 10秒弹窗 ==========
const showPopup = ref(false);
let popupTimer = null;

// ========== 爱心特效 ==========
function createHeart(x, y) {
  const heart = document.createElement("div");
  heart.className = "heart-burst";
  heart.innerHTML = ["❤", "💕", "💖", "💗", "💝"][Math.floor(Math.random() * 5)];
  heart.style.left = x + "px";
  heart.style.top = y + "px";
  heart.style.fontSize = Math.random() * 20 + 18 + "px";
  document.getElementById("floatingHearts").appendChild(heart);
  setTimeout(() => heart.remove(), 1500);
}

function spawnHearts(e) {
  for (let i = 0; i < 6; i++) {
    setTimeout(() => {
      createHeart(
        e.clientX + (Math.random() - 0.5) * 80,
        e.clientY + (Math.random() - 0.5) * 80
      );
    }, i * 80);
  }
}

let mouseTimer = null;
function onMouseMove(e) {
  clearTimeout(mouseTimer);
  mouseTimer = setTimeout(() => {
    if (Math.random() > 0.6) {
      createHeart(e.clientX + (Math.random() - 0.5) * 30, e.clientY);
    }
  }, 100);
}

// ========== 生命周期 ==========
onMounted(() => {
  startAutoPlay();
  startTextAutoPlay();

  popupTimer = setTimeout(() => {
    showPopup.value = true;
  }, 10000);

  document.addEventListener("mousemove", onMouseMove);
});

onUnmounted(() => {
  stopAutoPlay();
  stopTextAutoPlay();
  clearTimeout(popupTimer);
  document.removeEventListener("mousemove", onMouseMove);
});
</script>

<style>
/* ===== 全局 & 背景 ===== */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.qixi-page {
  position: relative;
  min-height: 100vh;
  overflow-x: hidden;
  font-family: "Microsoft YaHei", "PingFang SC", "Noto Sans SC", sans-serif;
  color: #4a2c4a;
}

.bg-gradient {
  position: fixed;
  inset: 0;
  z-index: -1;
  background: linear-gradient(135deg, #fce4ec, #f3e5f5, #e8eaf6, #fce4ec);
  background-size: 400% 400%;
  animation: gradientShift 12s ease infinite;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  25% { background-position: 100% 0%; }
  50% { background-position: 100% 100%; }
  75% { background-position: 0% 100%; }
  100% { background-position: 0% 50%; }
}

/* ===== 浮动爱心层 ===== */
.floating-hearts {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 1;
}

.heart-burst {
  position: absolute;
  animation: heartFloat 1.5s ease-out forwards;
  pointer-events: none;
}

@keyframes heartFloat {
  0% {
    opacity: 1;
    transform: translateY(0) scale(0.5) rotate(0deg);
  }
  50% {
    opacity: 0.8;
    transform: translateY(-60px) scale(1.2) rotate(20deg);
  }
  100% {
    opacity: 0;
    transform: translateY(-120px) scale(0.8) rotate(-10deg);
  }
}

/* ===== BGM 按钮 ===== */
.bgm-btn {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 50;
  width: 48px;
  height: 48px;
  border-radius: 50%;
  border: 2px solid rgba(156, 39, 176, 0.3);
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(6px);
  font-size: 1.3rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s;
  box-shadow: 0 2px 12px rgba(156, 39, 176, 0.15);
}

.bgm-btn:hover {
  transform: scale(1.1);
  border-color: rgba(156, 39, 176, 0.6);
  box-shadow: 0 4px 20px rgba(156, 39, 176, 0.25);
}

/* ===== 内容区 ===== */
.content {
  position: relative;
  z-index: 2;
  max-width: 900px;
  margin: 0 auto;
  padding: 40px 20px;
}

/* ===== 标题 ===== */
.header {
  text-align: center;
  padding: 60px 0 40px;
}

.brand-wrap {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}

.brand-logo {
  width: min(260px, 52vw);
  height: auto;
  display: block;
  border-radius: 18px;
  filter: drop-shadow(0 10px 28px rgba(156, 39, 176, 0.18));
  background: rgba(17, 14, 20, 0.22);
  padding: 8px;
  border: 1px solid rgba(255, 255, 255, 0.18);
}

.title {
  font-size: 2.8rem;
  background: linear-gradient(135deg, #e91e63, #9c27b0);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 20px;
  letter-spacing: 4px;
  text-shadow: none;
}

.subtitle {
  font-size: 1.15rem;
  line-height: 1.8;
  color: #7b587b;
  margin-bottom: 20px;
}

.divider {
  display: flex;
  justify-content: center;
  gap: 12px;
  font-size: 1.4rem;
  animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.1); }
}

/* ===== 区块标题 ===== */
.section-title {
  text-align: center;
  font-size: 1.5rem;
  color: #6a3e6a;
  margin-bottom: 24px;
}

/* ===== 图片轮播 ===== */
.carousel-section {
  margin: 40px 0;
}

.carousel {
  display: flex;
  align-items: center;
  gap: 8px;
}

.carousel-viewport {
  flex: 1;
  overflow: hidden;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(156, 39, 176, 0.15);
  background: rgba(255, 255, 255, 0.3);
}

.carousel-track {
  display: flex;
  transition: transform 0.6s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.carousel-slide {
  min-width: 100%;
}

.image-wrapper {
  width: 100%;
  height: 500px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.4);
  overflow: hidden;
}

.image-wrapper img {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
  object-fit: contain;
  display: block;
  border-radius: 4px;
}

.carousel-btn {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  border: none;
  background: rgba(156, 39, 176, 0.7);
  color: #fff;
  font-size: 1.5rem;
  cursor: pointer;
  transition: all 0.3s;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.carousel-btn:hover {
  background: rgba(156, 39, 176, 0.95);
  transform: scale(1.1);
}

.indicators {
  display: flex;
  justify-content: center;
  gap: 8px;
  margin-top: 16px;
  flex-wrap: wrap;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #d1b3d1;
  cursor: pointer;
  transition: all 0.3s;
}

.dot.active {
  background: #9c27b0;
  width: 28px;
  border-radius: 5px;
}

.dot:hover {
  background: #ce93d8;
}

/* ===== 文字卡片 ===== */
.text-section {
  margin: 40px 0 60px;
}

.text-card {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(10px);
  border-radius: 20px;
  padding: 48px 36px;
  box-shadow: 0 4px 24px rgba(233, 30, 99, 0.1);
  border: 1px solid rgba(233, 30, 99, 0.15);
  min-height: 180px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-text {
  font-size: 1.3rem;
  line-height: 1.9;
  text-align: center;
  color: #5a2d5a;
  font-weight: 500;
}

.text-dot {
  background: #e8b4d8;
}

.text-dot.active {
  background: #e91e63;
}

/* 文字过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s ease, transform 0.5s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* ===== 底部 ===== */
.footer {
  position: relative;
  z-index: 2;
  text-align: center;
  padding: 40px 20px 60px;
  border-top: 1px solid rgba(156, 39, 176, 0.15);
}

.footer-hearts {
  font-size: 1.5rem;
  margin-bottom: 12px;
  animation: pulse 2s ease-in-out infinite;
}

.footer-text {
  font-size: 1.1rem;
  color: #7b587b;
  margin-bottom: 8px;
}

.footer-name {
  font-size: 1rem;
  color: #9c27b0;
  font-weight: bold;
  margin-bottom: 6px;
}

.footer-date {
  font-size: 0.9rem;
  color: #a87ca8;
}

/* ===== 10秒弹窗 ===== */
.popup-overlay {
  position: fixed;
  inset: 0;
  z-index: 100;
  background: rgba(0, 0, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  backdrop-filter: blur(4px);
}

.popup-card {
  background: linear-gradient(135deg, #fff5f7, #f8f0ff);
  border-radius: 24px;
  padding: 40px 32px;
  max-width: 400px;
  width: 90%;
  text-align: center;
  box-shadow: 0 20px 60px rgba(156, 39, 176, 0.2);
  border: 1px solid rgba(233, 30, 99, 0.2);
}

.popup-icon {
  font-size: 3rem;
  margin-bottom: 16px;
  animation: bounce 1s ease infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.popup-card h3 {
  font-size: 1.4rem;
  color: #6a3e6a;
  margin-bottom: 16px;
}

.popup-card p {
  font-size: 1rem;
  line-height: 1.8;
  color: #5a2d5a;
  margin-bottom: 24px;
}

.popup-btn {
  background: linear-gradient(135deg, #e91e63, #9c27b0);
  color: #fff;
  border: none;
  padding: 12px 36px;
  border-radius: 50px;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  font-family: inherit;
}

.popup-btn:hover {
  transform: scale(1.05);
  box-shadow: 0 4px 20px rgba(156, 39, 176, 0.3);
}

.popup-enter-active {
  transition: opacity 0.4s ease;
}
.popup-leave-active {
  transition: opacity 0.3s ease;
}
.popup-enter-from,
.popup-leave-to {
  opacity: 0;
}
.popup-enter-active .popup-card {
  animation: popIn 0.4s ease;
}

@keyframes popIn {
  0% { transform: scale(0.7); opacity: 0; }
  100% { transform: scale(1); opacity: 1; }
}

/* ===== 响应式 ===== */
@media (max-width: 768px) {
  .brand-logo {
    width: min(200px, 58vw);
  }
  .title {
    font-size: 1.8rem;
  }
  .subtitle {
    font-size: 1rem;
  }
  .image-wrapper {
    height: 380px;
  }
  .carousel-btn {
    width: 36px;
    height: 36px;
    font-size: 1.2rem;
  }
  .text-card {
    padding: 32px 20px;
    min-height: 140px;
  }
  .card-text {
    font-size: 1.1rem;
  }
  .popup-card {
    padding: 32px 20px;
  }
  .bgm-btn {
    top: 12px;
    right: 12px;
    width: 42px;
    height: 42px;
    font-size: 1.1rem;
  }
}

@media (max-width: 480px) {
  .title {
    font-size: 1.5rem;
  }
  .header {
    padding: 40px 0 24px;
  }
  .image-wrapper {
    height: 280px;
  }
  .carousel {
    gap: 4px;
  }
  .card-text {
    font-size: 1rem;
  }
  .footer {
    padding: 30px 16px 40px;
  }
  .bgm-btn {
    top: 10px;
    right: 10px;
    width: 38px;
    height: 38px;
    font-size: 1rem;
  }
}
</style>
