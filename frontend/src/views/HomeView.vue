<script setup>
import { ref, onMounted, computed } from 'vue'
import { api } from '@/api'

const events = ref([])
const loading = ref(false)

const mainEvent = computed(() => events.value[0] || null)
const otherEvents = computed(() => events.value.slice(1, 4))

onMounted(() => {
  loadEvents()
})

async function loadEvents() {
  try {
    loading.value = true

    const response = await api.get('/api/events/')

    events.value = response.data
  } catch (error) {
    console.error('Ошибка загрузки мероприятий:', error)
    alert('Ошибка загрузки мероприятий')
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="page">
    <header class="header">
      <div class="header-inner">
        <router-link to="/home" class="logo">
          <img class="logo-img" src="@/assets/logo.png" alt="ИВЕНТУС" />
          <span>ИВЕНТУС</span>
        </router-link>

        <div class="header-actions">
          <img
            class="user-icon-img"
            src="@/assets/user.png"
            alt="user"
            @click="$router.push('/profile')"
          />

          <button class="login-btn" @click="$router.push('/')">Войти / Регистрация</button>
        </div>
      </div>
    </header>

    <main class="main">
      <h1>Ближайшие мероприятия</h1>

      <p v-if="loading" class="empty-text">Загрузка мероприятий...</p>

      <p v-else-if="events.length === 0" class="empty-text">Пока нет доступных мероприятий</p>

      <template v-else>
        <section v-if="mainEvent" class="main-event">
          <div class="image-placeholder large">Изображение мероприятия</div>

          <div class="event-info">
            <h2>{{ mainEvent.title || mainEvent.name }}</h2>

            <p>
              {{ mainEvent.description || 'Здесь находится информация о мероприятии.' }}
            </p>

            <p v-if="mainEvent.location" class="event-extra">Место: {{ mainEvent.location }}</p>

            <p v-if="mainEvent.event_date || mainEvent.date" class="event-extra">
              Дата: {{ mainEvent.event_date || mainEvent.date }}
            </p>

            <button class="more-btn">Развернуть</button>

            <button class="primary-btn">Перейти</button>
          </div>
        </section>

        <section class="cards">
          <article v-for="event in otherEvents" :key="event.id" class="event-card">
            <div class="image-placeholder small">Изображение</div>

            <h3>{{ event.title || event.name }}</h3>

            <p>
              {{ event.description || 'Краткое описание мероприятия' }}
            </p>
          </article>
        </section>
      </template>
    </main>

    <footer class="footer">
      <div class="footer-inner">
        <div class="footer-logo">
          <img class="logo-img" src="@/assets/logo.png" alt="ИВЕНТУС" />
          <span>ИВЕНТУС</span>
        </div>

        <p>Авторы</p>
        <p>...</p>
        <p>...</p>
        <p>...</p>
        <p>Github</p>
      </div>
    </footer>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&display=swap');

.page {
  min-height: 100vh;
  font-family: 'Playfair Display', serif;
  background: #fff;
  color: #000;
}

.header {
  width: 100%;
  border-bottom: 2px solid #b5b5b5;
}

.header-inner {
  max-width: 1120px;
  height: 90px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: inherit;
  cursor: pointer;
}

.logo-img {
  height: 50px;
  width: auto;
  object-fit: contain;
}

.logo span {
  font-size: 28px;
  font-weight: 700;
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

.user-icon-img {
  width: 32px;
  height: 32px;
  cursor: pointer;
}

.login-btn {
  background: #000;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 18px;
  font-size: 12px;
  cursor: pointer;
}

.main {
  max-width: 1120px;
  margin: 0 auto;
  padding: 55px 0 120px;
}

h1 {
  font-size: 44px;
  margin-bottom: 70px;
}

.empty-text {
  font-size: 22px;
  color: #777;
  text-align: center;
}

.main-event {
  border: 3px solid #aaa;
  border-radius: 32px;
  padding: 42px;
  display: grid;
  grid-template-columns: 1.35fr 1fr;
  gap: 34px;
  margin-bottom: 80px;
}

.image-placeholder {
  border: 3px dashed #aaa;
  background: #f4f4f4;
  color: #999;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-size: 18px;
  box-sizing: border-box;
}

.image-placeholder.large {
  height: 430px;
}

.event-info h2 {
  font-size: 36px;
  line-height: 1.15;
  margin: 0 0 24px;
}

.event-info p {
  font-size: 18px;
  line-height: 1.35;
  color: #777;
  margin-bottom: 18px;
}

.event-extra {
  font-size: 16px;
  color: #555;
}

.more-btn {
  display: block;
  border: none;
  background: none;
  font-family: 'Playfair Display', serif;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  margin-bottom: 30px;
  padding: 0;
}

.primary-btn {
  width: 190px;
  height: 58px;
  background: #08a8e8;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 20px;
  font-family: 'Playfair Display', serif;
  cursor: pointer;
}

.cards {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
}

.image-placeholder.small {
  height: 210px;
  margin-bottom: 18px;
}

.event-card h3 {
  font-size: 18px;
  margin: 0 0 8px;
}

.event-card p {
  font-size: 16px;
  margin: 0;
}

.footer {
  width: 100%;
  border-top: 1px solid #ddd;
}

.footer-inner {
  max-width: 1120px;
  margin: 0 auto;
  padding: 18px 0 40px;
  font-size: 12px;
  color: #777;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 10px;
}

.footer-logo span {
  font-size: 18px;
  font-weight: 700;
  color: #000;
}

.footer-logo .logo-img {
  height: 24px;
}

@media (max-width: 900px) {
  .main-event {
    grid-template-columns: 1fr;
  }

  .cards {
    grid-template-columns: 1fr;
  }

  .main,
  .header-inner,
  .footer-inner {
    padding-left: 20px;
    padding-right: 20px;
  }
}
</style>
