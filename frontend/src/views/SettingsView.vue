<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const fullName = ref('Иванов Иван Иванович')
const birthDate = ref('2006-03-18')

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

function saveSettings() {
  localStorage.setItem('profileName', fullName.value)
  localStorage.setItem('profileBirthDate', birthDate.value)
  localStorage.setItem('surveySkills', JSON.stringify(skills.value))

  alert('Настройки сохранены')
  router.push('/profile')
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

    <main class="settings">
      <h1>Настройки</h1>

      <section class="settings-card">
        <label>
          Изменить ФИО
          <input v-model="fullName" type="text" />
        </label>

        <label>
          Изменить дату рождения
          <input v-model="birthDate" type="date" />
        </label>

        <h2>Изменить компетенции</h2>

        <div class="skills">
          <div v-for="skill in skills" :key="skill.name" class="skill-row">
            <span>{{ skill.name }}</span>

            <input v-model="skill.value" type="number" min="1" max="5" />

            <span>баллов</span>
          </div>
        </div>

        <div class="buttons">
          <button class="save-btn" @click="saveSettings">Сохранить</button>

          <button class="interests-btn" type="button" @click="$router.push('/interests')">
            Выбрать интересы заново
          </button>

          <button class="back-btn" @click="$router.push('/profile')">Назад</button>
        </div>
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

.settings {
  max-width: 760px;
  margin: 0 auto;
  padding: 48px 0 120px;
}

h1 {
  text-align: center;
  font-size: 38px;
  margin-bottom: 42px;
}

.settings-card {
  border: 3px solid #aaa;
  border-radius: 26px;
  padding: 42px;
}

label {
  display: flex;
  flex-direction: column;
  gap: 10px;
  font-size: 18px;
  margin-bottom: 28px;
}

input {
  height: 38px;
  border: 2px solid #aaa;
  border-radius: 6px;
  background: #eee;
  font-size: 18px;
  padding: 0 12px;
  font-family: 'Playfair Display', serif;
}

h2 {
  font-size: 26px;
  margin: 36px 0 24px;
}

.skills {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.skill-row {
  height: 46px;
  border: 2px solid #aaa;
  border-radius: 10px;
  padding: 0 16px;
  display: grid;
  grid-template-columns: 1fr 80px 70px;
  align-items: center;
  gap: 12px;
  font-size: 18px;
}

.skill-row input {
  height: 30px;
  text-align: center;
}

.buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  margin-top: 40px;
}

.save-btn,
.interests-btn,
.back-btn {
  width: 280px;
  height: 54px;
  border: none;
  border-radius: 6px;
  font-size: 18px;
  cursor: pointer;
  font-family: 'Playfair Display', serif;
  color: white;
}

.save-btn {
  background: #08a8e8;
}

.interests-btn {
  background: #08a8e8;
}

.back-btn {
  background: #ff4b12;
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
</style>
