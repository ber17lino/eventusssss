<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { api } from '@/api'

const router = useRouter()

const showPassword = ref(false)

const email = ref('')
const password = ref('')

async function loginUser() {
  try {
    const formData = new URLSearchParams()

    formData.append('username', email.value)
    formData.append('password', password.value)

    const response = await api.post('/api/auth/login', formData, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    })

    const token = response.data.access_token

    localStorage.setItem('token', token)

    api.defaults.headers.common['Authorization'] = `Bearer ${token}`

    const meResponse = await api.get('/api/auth/me')

    localStorage.setItem('userId', meResponse.data.id)
    localStorage.setItem('userData', JSON.stringify(meResponse.data))

    router.push('/survey')
  } catch (error) {
    console.error(error)
    alert('Ошибка входа')
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
          <img class="user-icon-img" src="@/assets/user.png" alt="user" />

          <button class="login-btn" @click="$router.push('/')">Войти / Регистрация</button>
        </div>
      </div>
    </header>

    <main class="main">
      <section class="login-card">
        <div class="decor decor-big"></div>
        <div class="decor decor-mid"></div>
        <div class="decor decor-small"></div>

        <h1>Вход</h1>

        <form class="form" @submit.prevent="loginUser">
          <label>
            Введите e-mail

            <input v-model="email" type="email" />
          </label>

          <label>
            Введите пароль

            <div class="password-field">
              <input v-model="password" :type="showPassword ? 'text' : 'password'" />

              <button type="button" @click="showPassword = !showPassword">
                {{ showPassword ? 'Скрыть' : 'Показать' }}
              </button>
            </div>
          </label>

          <button class="secondary-btn" type="submit">Войти</button>

          <p class="small-text">У меня нет аккаунта</p>

          <button class="primary-btn" type="button" @click="$router.push('/register')">
            Зарегистрироваться
          </button>
        </form>
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
  width: 100%;
  min-height: 100vh;
  background: #ffffff;
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

.footer-logo span {
  font-size: 18px;
  font-weight: 700;
}

.footer-logo .logo-img {
  height: 24px;
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
  display: flex;
  justify-content: center;
  padding: 70px 0 140px;
}

.login-card {
  width: 620px;
  min-height: 640px;
  border: 3px solid #aaa;
  border-radius: 26px;
  position: relative;
  padding: 38px 44px;
  overflow: hidden;
  box-sizing: border-box;
}

h1 {
  text-align: center;
  font-size: 34px;
  margin: 0 0 80px;
}

.form {
  display: flex;
  flex-direction: column;
}

label {
  font-size: 16px;
  margin-bottom: 48px;
}

input {
  width: 100%;
  height: 34px;
  margin-top: 10px;
  border: 2px solid #aaa;
  border-radius: 4px;
  background: #eee;
  font-size: 16px;
  padding: 0 10px;
  box-sizing: border-box;
}

.password-field {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.password-field input {
  margin-top: 0;
  flex: 1;
}

.password-field button {
  height: 34px;
  padding: 0 10px;
  border: 2px solid #aaa;
  border-left: none;
  background: #fff;
  cursor: pointer;
  font-family: 'Playfair Display', serif;
}

.secondary-btn {
  width: 150px;
  height: 54px;
  margin: 0 auto 90px;
  background: #ff4b12;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  cursor: pointer;
}

.small-text {
  text-align: center;
  color: #aaa;
  font-size: 11px;
  margin: 0 0 8px;
}

.primary-btn {
  width: 280px;
  height: 54px;
  margin: 0 auto;
  background: #08a8e8;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 15px;
  cursor: pointer;
}

.decor {
  position: absolute;
  background: #08a8e8;
}

.decor-big {
  width: 132px;
  height: 110px;
  right: 10px;
  top: 10px;
  border-radius: 0 24px 0 90px;
}

.decor-mid {
  width: 110px;
  height: 70px;
  right: 70px;
  top: 10px;
  border-radius: 0 0 80px 80px;
}

.decor-small {
  width: 32px;
  height: 32px;
  right: 70px;
  top: 120px;
  border-radius: 50%;
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
</style>
