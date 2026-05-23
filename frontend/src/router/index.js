import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/HomeView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import SurveyView from '../views/SurveyView.vue'
import ProfileView from '../views/ProfileView.vue'
import SettingsView from '../views/SettingsView.vue'
import InterestsView from '../views/InterestsView.vue'

const router = createRouter({
  history: createWebHistory(),

  routes: [
    {
      path: '/',
      component: LoginView, // страница входа (главная при запуске)
    },
    {
      path: '/home',
      component: HomeView, // главный экран с мероприятиями
    },
    {
      path: '/register',
      component: RegisterView, // регистрация
    },
    {
      path: '/survey',
      component: SurveyView, // анкета
    },
    {
      path: '/profile',
      component: ProfileView, // личный кабинет
    },
    {
      path: '/settings',
      component: SettingsView,
    },
    {
      path: '/interests',
      component: InterestsView,
    },
  ],
})

export default router
