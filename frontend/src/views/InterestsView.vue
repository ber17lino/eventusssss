<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { api } from '@/api'

const router = useRouter()

const interests = ref([
  { name: 'Рисование', category_id: 7 },
  { name: 'Лепка', category_id: 7 },
  { name: 'Музыка', category_id: 6 },
  { name: 'Фотография', category_id: 7 },
  { name: 'Танцы', category_id: 7 },
  { name: 'Программирование', category_id: 1 },
  { name: 'Дизайн', category_id: 7 },
  { name: 'Кино', category_id: 7 },
  { name: 'Театр', category_id: 7 },
  { name: 'Литература', category_id: 7 },
  { name: 'Спорт', category_id: 2 },
  { name: 'Путешествия', category_id: 7 },
  { name: 'Иностранные языки', category_id: 7 },
  { name: 'История', category_id: 3 },
  { name: 'Философия', category_id: 3 },
  { name: 'Психология', category_id: 3 },
  { name: 'Гастрономия', category_id: 7 },
  { name: 'Настольные игры', category_id: 4 },
  { name: 'Видеоигры', category_id: 4 },
  { name: 'Наука', category_id: 3 },
])

const selected = ref([])

function toggleInterest(item) {
  const exists = selected.value.find((interest) => interest.name === item.name)

  if (exists) {
    selected.value = selected.value.filter((interest) => interest.name !== item.name)
  } else {
    selected.value.push(item)
  }
}

function isSelected(item) {
  return selected.value.some((interest) => interest.name === item.name)
}

async function saveInterests() {
  if (selected.value.length === 0) {
    alert('Выберите хотя бы один интерес')
    return
  }

  try {
    const userId = localStorage.getItem('userId')

    if (!userId) {
      alert('Не найден id пользователя. Войдите заново.')
      router.push('/')
      return
    }

    const uniqueCategoryIds = [...new Set(selected.value.map((interest) => interest.category_id))]

    const payload = uniqueCategoryIds.map((categoryId) => ({
      category_id: categoryId,
      weight: 5,
    }))

    await api.post(`/api/users/${userId}/interests`, payload)

    localStorage.setItem(
      'userInterests',
      JSON.stringify(selected.value.map((interest) => interest.name)),
    )

    router.push('/profile')
  } catch (error) {
    console.error('Ошибка интересов:', error)
    console.error('Ответ backend:', error.response?.data)

    alert('Ошибка сохранения интересов: ' + JSON.stringify(error.response?.data))
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
      <h1>Анкета</h1>

      <p class="subtitle">Выберите ваши интересы</p>

      <div class="interests-grid">
        <button
          v-for="item in interests"
          :key="item.name"
          class="interest-card"
          :class="{ active: isSelected(item) }"
          @click="toggleInterest(item)"
        >
          {{ item.name }}
        </button>
      </div>

      <button class="continue-btn" @click="saveInterests">Продолжить</button>
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
  width: 100%;
  min-height: 100vh;
  background: #fff;
  font-family: 'Playfair Display', serif;
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

.logo,
.footer-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: inherit;
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
  object-fit: contain;
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
  max-width: 1180px;
  margin: 0 auto;
  padding: 40px 0 80px;
}

h1 {
  text-align: center;
  font-size: 34px;
  margin-bottom: 50px;
}

.subtitle {
  font-size: 22px;
  margin-bottom: 40px;
  margin-left: 40px;
}

.interests-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 34px;
  justify-items: center;
}

.interest-card {
  width: 210px;
  min-height: 90px;
  padding: 12px;
  border: 3px solid #b0b0b0;
  border-radius: 10px;
  background: white;
  font-size: 18px;
  font-family: 'Playfair Display', serif;
  cursor: pointer;
  transition: 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  word-break: break-word;
}

.interest-card:hover {
  transform: scale(1.03);
}

.interest-card.active {
  background: #08a8e8;
  color: white;
  border-color: #08a8e8;
}

.continue-btn {
  display: block;
  width: 320px;
  height: 58px;
  margin: 90px auto 0;
  background: #08a8e8;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 18px;
  cursor: pointer;
}

.footer {
  width: 100%;
  border-top: 1px solid #ddd;
  margin-top: 100px;
}

.footer-inner {
  max-width: 1120px;
  margin: 0 auto;
  padding: 18px 0 40px;
  font-size: 12px;
  color: #777;
}

.footer-logo span {
  font-size: 18px;
  font-weight: 700;
  color: #000;
}

.footer-logo .logo-img {
  height: 24px;
}

@media (max-width: 1100px) {
  .interests-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

@media (max-width: 760px) {
  .interests-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .interest-card {
    width: 170px;
    min-height: 80px;
    font-size: 16px;
  }
}
</style>
