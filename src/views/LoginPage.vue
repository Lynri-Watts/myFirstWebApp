<template>
  <div class="container">
    <img alt="Vue logo" src="../assets/logo.png">
    <br>
    <div class="login-container">
      <h2>用户登录</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label>电子邮箱</label>
          <input
            type="email"
            v-model="form.email"
            placeholder="请输入邮箱"
            autofocus
          >
          <div class="error" v-if="errors.email">{{ errors.email }}</div>
        </div>

        <div class="form-group">
          <label>密码</label>
          <input
            type="password"
            v-model="form.password"
            placeholder="请输入密码"
          >
          <div class="error" v-if="errors.password">{{ errors.password }}</div>
        </div>

        <button type="submit" :disabled="isSubmitting">
          {{ isSubmitting ? '登录中...' : '立即登录' }}
        </button>

        <div class="links">
          <a href="#">忘记密码？</a>
          <span style="color: #dadce0"> | </span>
          <router-link to="/register">注册账号</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
  import { ref, reactive, computed } from 'vue';
  import { useRouter } from 'vue-router'

  const form = reactive({
    email: '',
    password: ''
  });

  const errors = reactive({
    email: '',
    password: ''
  });

  const isSubmitting = ref(false);

  const isValidEmail = computed(() => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email);
  });

  const validateForm = () => {
    let isValid = true;
    
    if (!form.email) {
      errors.email = '邮箱不能为空';
      isValid = false;
    } else if (!isValidEmail.value) {
      errors.email = '请输入有效的邮箱地址';
      isValid = false;
    } else {
      errors.email = '';
    }

    if (!form.password) {
      errors.password = '密码不能为空';
      isValid = false;
    } else {
      errors.password = '';
    }

    return isValid;
  };
  const router = useRouter()

  const handleSubmit = async () => {
    if (!validateForm()) return;

    isSubmitting.value = true;
    
    try {
      const response = await fetch('http://localhost:5000/api/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: form.email,
          password: form.password
        })
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || '登录失败');
      }

      // 存储Token到localStorage
      // localStorage.setItem('access_token', data.data.access_token);
      console.log(data)
      localStorage.setItem('username',data.data.username)
      router.push('/dashboard');
      
    } catch (error) {
      alert(error.message);
    } finally {
      isSubmitting.value = false;
    }
  };
</script>

<style scoped>
  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    min-height: 100vh;
    padding: 2rem 0;
    background-color: #f0f2f5;
  }
  .login-container {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    width: 320px;
  }

  h2 {
    text-align: center;
    color: #1a73e8;
    margin-bottom: 1.5rem;
  }

  .form-group {
    margin-bottom: 1rem;
  }

  label {
    display: block;
    margin-bottom: 0.5rem;
    color: #5f6368;
  }

  input {
    width: 100%;
    padding: 0.8rem;
    border: 1px solid #dadce0;
    border-radius: 4px;
    box-sizing: border-box;
  }

  input:focus {
    outline: none;
    border-color: #1a73e8;
    box-shadow: 0 0 0 2px #e8f0fe;
  }

  .error {
    color: #dc3545;
    font-size: 0.875rem;
    margin-top: 0.25rem;
  }

  button {
    width: 100%;
    padding: 0.8rem;
    background-color: #1a73e8;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #1557b0;
  }

  button:disabled {
    background-color: #9ac1f3;
    cursor: not-allowed;
  }

  .links {
    margin-top: 1rem;
    text-align: center;
  }

  .links a {
    color: #1a73e8;
    text-decoration: none;
    font-size: 0.875rem;
  }

  .links a:hover {
    text-decoration: underline;
  }
</style>