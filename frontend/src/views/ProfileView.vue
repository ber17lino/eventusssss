<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { api } from '@/api'

const router = useRouter()

const user = ref({
  name: 'Пользователь',
  birthDate: 'Дата рождения не указана',
  email: '',
  course: '',
  faculty: '',
})

const skills = ref([])
const interests = ref([])

onMounted(() => {
  loadProfile()
})

async function loadProfile() {
  try {
    const userId = localStorage.getItem('userId')

    if (!userId) {
      alert('Не найден пользователь. Войдите заново.')
      router.push('/')
      return
    }

    const response = await api.get(`/api/users/${userId}/full-profile`)
    const data = response.data

    console.log('Профиль с backend:', data)

    user.value.name = data.full_name || 'Пользователь'
    user.value.email = data.email || ''
    user.value.course = data.course || ''
    user.value.faculty = data.faculty || ''

    const savedBirthDate = localStorage.getItem('profileBirthDate')
    if (savedBirthDate) {
      user.value.birthDate = formatDate(savedBirthDate)
    }

    skills.value = normalizeSkills(data)
    interests.value = normalizeInterests(data)
  } catch (error) {
    console.error('Ошибка загрузки профиля:', error)
    console.error('Ответ backend:', error.response?.data)

    alert('Ошибка загрузки профиля')
  }
}

function normalizeSkills(data) {
  const backendSkills =
    data.test_results || data.competencies || data.competences || data.skills || []

  return backendSkills.map((item) => ({
    id: item.competence_id || item.competency_id || item.id,
    name: item.competence_name || item.competency_name || item.name || item.title || 'Компетенция',
    value: item.score || item.value || 0,
  }))
}

function normalizeInterests(data) {
  const backendInterests = data.interests || data.categories || data.user_interests || []

  return backendInterests.map((item) => ({
    id: item.category_id || item.id,
    name: item.category_name || item.name || item.title || 'Интерес',
  }))
}

function formatDate(dateString) {
  const date = new Date(dateString)

  return date.toLocaleDateString('ru-RU', {
    day: 'numeric',
    month: 'long',
    year: 'numeric',
  })
}

function getPointsWord(value) {
  const numberValue = Number(value)

  if (numberValue === 1) return 'балл'
  if (numberValue >= 2 && numberValue <= 4) return 'балла'

  return 'баллов'
}

function logout() {
  localStorage.removeItem('token')
  localStorage.removeItem('userId')
  localStorage.removeItem('userData')

  router.push('/')
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

    <main class="profile">
      <aside class="sidebar">
        <div class="avatar-card">
          <div class="avatar-head"></div>
          <div class="avatar-body"></div>
        </div>

        <button class="side-btn" @click="$router.push('/settings')">Настройки</button>

        <button class="side-btn" @click="logout">Выход</button>
      </aside>

      <section class="content">
        <h1>{{ user.name }}</h1>
        <p class="birth">{{ user.birthDate }}</p>

        <p class="user-info">Email: {{ user.email }}</p>
        <p class="user-info">Курс: {{ user.course }}</p>
        <p class="user-info">Факультет: {{ user.faculty }}</p>

        <h2>Компетенции</h2>

        <div v-if="skills.length > 0" class="skills">
          <div v-for="skill in skills" :key="skill.id" class="skill-row">
            <span>{{ skill.name }}</span>
            <span>{{ skill.value }} {{ getPointsWord(skill.value) }}</span>
          </div>
        </div>

        <p v-else class="empty-text">Компетенции пока не заполнены</p>

        <h2>Интересы</h2>

        <div v-if="interests.length > 0" class="interests">
          <span
            v-for="interest in interests"
            :key="interest.id || interest.name"
            class="interest-tag"
          >
            {{ interest.name }}
          </span>
        </div>

        <p v-else class="empty-text">Интересы пока не выбраны</p>
      </section>
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
  transition: 0.2s;
}

.user-icon-img:hover {
  transform: scale(1.08);
}

.login-btn {
  background: #000;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 10px 18px;
  font-size: 12px;
  cursor: pointer;
}

.profile {
  max-width: 1120px;
  margin: 0 auto;
  padding: 28px 0 360px;
  display: flex;
  gap: 24px;
}

.sidebar {
  width: 260px;
}

.avatar-card {
  height: 300px;
  border: 3px solid #aaa;
  border-radius: 26px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.avatar-head {
  width: 110px;
  height: 110px;
  border: 5px solid #ff4b12;
  border-radius: 50%;
  margin-bottom: 20px;
}

.avatar-body {
  width: 170px;
  height: 115px;
  border: 5px solid #ff4b12;
  border-top-left-radius: 90px;
  border-top-right-radius: 90px;
  border-bottom-left-radius: 45px;
  border-bottom-right-radius: 45px;
}

.side-btn {
  width: 100%;
  height: 44px;
  margin-top: 18px;
  border: 3px solid #aaa;
  border-radius: 12px;
  background: white;
  font-size: 20px;
  font-weight: 700;
  font-family: 'Playfair Display', serif;
  cursor: pointer;
}

.content {
  flex: 1;
}

h1 {
  font-size: 44px;
  margin: 10px 0 8px;
}

.birth {
  font-size: 24px;
  color: #777;
  margin: 0 0 18px;
}

.user-info {
  font-size: 18px;
  color: #777;
  margin: 4px 0;
}

h2 {
  font-size: 26px;
  margin: 26px 0 16px;
}

.skills {
  width: 100%;
}

.skill-row {
  min-height: 44px;
  border: 3px solid #aaa;
  border-radius: 12px;
  margin-bottom: 8px;
  padding: 8px 22px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  color: #777;
  font-size: 24px;
  font-weight: 700;
  box-sizing: border-box;
}

.interests {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-bottom: 24px;
}

.interest-tag {
  border: 3px solid #aaa;
  border-radius: 12px;
  padding: 8px 16px;
  color: #777;
  font-size: 20px;
  font-weight: 700;
}

.empty-text {
  color: #999;
  font-size: 18px;
  margin-bottom: 20px;
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
</style>
