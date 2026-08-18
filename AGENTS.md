# AGENTS.md

## 项目概述

本项目是一个**前后端分离**的 Web 应用：
- **后端**：Django 6.1 + Django REST Framework，提供 REST API
- **前端**：Vue 3 + Vite，单页应用（SPA）
- **后台管理**：SimpleUI 美化后台，中文界面

## 项目结构

```
E:\ysy\
├── config/                # Django 项目配置
│   ├── settings.py        # 配置文件
│   ├── urls.py            # URL 路由
│   ├── wsgi.py
│   └── asgi.py
├── core/                  # Django 主应用
│   ├── models.py
│   ├── views.py           # API 视图
│   ├── admin.py
│   ├── apps.py
│   └── migrations/
├── frontend/              # Vue 3 前端项目
│   ├── src/
│   │   ├── api/           # Axios API 服务
│   │   ├── router/        # Vue Router 路由配置
│   │   ├── views/         # 页面组件
│   │   ├── App.vue        # 根组件
│   │   └── main.js        # 入口文件
│   ├── vite.config.js     # Vite 配置（含代理）
│   ├── index.html
│   └── package.json
├── picture/               # 图片资源目录
├── manage.py              # Django 管理脚本
└── .venv/                 # Python 虚拟环境
```

## 启动项目

### 后端（Django）

```powershell
# 激活虚拟环境
E:\ysy\.venv\Scripts\Activate.ps1

# 启动 Django 开发服务器
python manage.py runserver 0.0.0.0:8000
```

### 前端（Vue 3 + Vite）

```powershell
cd E:\ysy\frontend

# Vite 开发服务器（含代理，/api 请求转发到 Django）
npx vite --host 0.0.0.0
```

前端默认运行在 `http://localhost:5173`，后端在 `http://127.0.0.1:8000`。

## 开发规范

### 后端（Django）

1. **模型**：在 `core/models.py` 中定义
2. **视图**：使用 DRF（Django REST Framework）的 APIView 或 ViewSet
3. **URL 路由**：在 `core/urls.py` 中定义，并在 `config/urls.py` 中包含
4. **序列化器**：在 `core/serializers.py` 中定义（如需要可新建）
5. **后台管理**：在 `core/admin.py` 中注册模型

### 前端（Vue 3）

1. **组件**：使用 `<script setup>` 组合式 API 风格
2. **页面**：放在 `src/views/` 目录
3. **API 请求**：通过 `src/api/index.js` 封装的 axios 实例
4. **路由**：在 `src/router/index.js` 中配置
5. **公共组件**：放在 `src/components/` 目录

### API 通信

前端通过 `/api/...` 路径访问后端 API，Vite 开发服务器会自动代理到 Django。

```javascript
// 前端调用示例
import api from "../api";

// GET 请求
const res = await api.get("/items/");

// POST 请求
const res = await api.post("/items/", { name: "test" });
```

## 后台管理

- 地址：`http://127.0.0.1:8000/admin/`
- 超级管理员账号：`ysy030907`
- 密码：`yhy201314`
- 后台使用 SimpleUI 美化框架，语言已设置为中文

## 常用命令

```powershell
# 创建新的 Django 应用
python manage.py startapp <app_name>

# 创建数据库迁移
python manage.py makemigrations

# 执行迁移
python manage.py migrate

# 创建超级管理员
python manage.py createsuperuser

# 安装前端新依赖
cd frontend
npm install <package-name>
```
