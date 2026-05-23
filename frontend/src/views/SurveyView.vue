<script setup>
import { ref } from 'vue'
import { api } from '@/api'
import { useRouter } from 'vue-router'

const router = useRouter()

const skills = ref([
  {
    name: 'Анализ информации',
    value: 200,
    competence_id: 1,
  },
  {
    name: 'Планирование',
    value: 200,
    competence_id: 2,
  },
  {
    name: 'Партнерство/сотрудничество',
    value: 200,
    competence_id: 3,
  },
  {
    name: 'Коммуникативная грамотность',
    value: 200,
    competence_id: 4,
  },
  {
    name: 'Клиентоориентированность',
    value: 200,
    competence_id: 5,
  },
  {
    name: 'Стрессоустойчивость',
    value: 200,
    competence_id: 6,
  },
  {
    name: 'Эмоциональный интеллект',
    value: 200,
    competence_id: 7,
  },
])

async function saveSurvey() {
  try {
    const userId = localStorage.getItem('userId')

    if (!userId) {
      alert('Не найден пользователь. Войдите заново.')
      return
    }

    for (const skill of skills.value) {
      const payload = [
        {
          competence_id: skill.competence_id,
          score: Number(skill.value),
        },
      ]

      console.log(payload)

      await api.post(`/api/users/${userId}/test-results`, payload)
    }

    localStorage.setItem('surveySkills', JSON.stringify(skills.value))

    router.push('/interests')
  } catch (error) {
    console.error('Ошибка анкеты:', error)
    console.error('Ответ backend:', error.response?.data)

    alert('Ошибка сохранения анкеты: ' + JSON.stringify(error.response?.data))
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

      <p class="description">
        В данной анкете вам необходимо ввести свои результаты из Центра Компетенций (
        <a href="#">ссылка_на_сайт.ru</a>
        )
      </p>

      <div class="survey-list">
        <div v-for="skill in skills" :key="skill.name" class="survey-item">
          <span class="skill-name">
            {{ skill.name }}
          </span>

          <div class="score-line">
            <input v-model.number="skill.value" class="score-input" type="number" min="200" />
          </div>
        </div>
      </div>

      <button class="continue-btn" @click="saveSurvey">Продолжить</button>
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
  max-width: 820px;
  margin: 0 auto;
  padding: 34px 0 80px;
}

h1 {
  text-align: center;
  font-size: 34px;
  margin-bottom: 70px;
}

.description {
  font-size: 21px;
  line-height: 1.4;
  margin-bottom: 70px;
}

.description a {
  color: #08a8e8;
}

.survey-list {
  width: 640px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  gap: 34px;
}

.survey-item {
  height: 48px;
  border: 3px solid #aaa;
  border-radius: 14px;
  padding: 0 18px;
  display: grid;
  grid-template-columns: 1fr 220px;
  align-items: center;
  box-sizing: border-box;
}

.skill-name {
  font-size: 16px;
  font-weight: 700;
}

.score-line {
  display: flex;
  align-items: center;
  width: 220px;
}

.score-input {
  width: 100%;
  height: 30px;
  border: none;
  border-bottom: 2px solid #555;
  background: transparent;
  font-size: 18px;
  text-align: center;
  font-family: 'Playfair Display', serif;
  outline: none;
}

.continue-btn {
  display: block;
  width: 280px;
  height: 58px;
  margin: 70px auto 0;
  background: #08a8e8;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
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

.footer-logo span {
  font-size: 18px;
  font-weight: 700;
  color: #000;
}

.footer-logo .logo-img {
  height: 24px;
}

@media (max-width: 760px) {
  .survey-list {
    width: 100%;
  }

  .survey-item {
    grid-template-columns: 1fr;
    height: auto;
    padding: 12px 18px;
    gap: 8px;
  }
}
</style>
