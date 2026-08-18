import { createRouter, createWebHistory } from "vue-router";
import Qixi from "../views/Qixi.vue";

const routes = [
  { path: "/", name: "Qixi", component: Qixi },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
