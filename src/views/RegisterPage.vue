<template>
  
  <div class="container">
    <img alt="Vue logo" src="../assets/logo.png">
    <br>
    <div class="register-container">
      
      <h2>用户注册</h2>
      <form @submit.prevent="handleSubmit">
        <div class="form-group">
          <label>用户名</label>
          <input
            type="text"
            v-model="form.username"
            placeholder="请输入用户名"
            autofocus
          >
        </div>

        <div class="form-group">
          <label>电子邮箱</label>
          <input
            type="email"
            v-model="form.email"
            placeholder="请输入邮箱"
          >
        </div>

        <div class="form-group">
          <label>密码</label>
          <input
            type="password"
            v-model="form.password"
            placeholder="请输入密码"
          >
        </div>

        <button type="submit">立即注册</button>

        <div class="links">
          <router-link to="/login">已有账号？立即登录</router-link>
        </div>
      </form>
    </div>
  </div>
</template>
  
<script setup>
  import { reactive } from 'vue'
  import { useRouter } from 'vue-router'
  import { ref, computed } from 'vue';

  
  const router = useRouter()
  
  const form = reactive({
    username: '',
    email: '',
    password: ''
  })

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

    if (!form.username) {
      errors.username = '用户名不能为空';
      isValid = false;
    } else {
      errors.username = '';
    }

    return isValid;
  };
  
  const handleSubmit = async () => {
    if (!validateForm()) return;

    isSubmitting.value = true;
    
    try {
      const response = await fetch('http://localhost:5000/api/register', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          email: form.email,
          password: form.password,
          username: form.username
        }),
        credentials: 'include' // 关键配置
      });

      const data = await response.json();
      
      if (!response.ok) {
        throw new Error(data.message || '注册失败');
      }

      // 存储Token到localStorage
      // localStorage.setItem('access_token', data.data.access_token);
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
  /* 复用登录页的样式 */
  .register-container {
    background: white;
    padding: 2rem;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    width: 320px;
  }

  h2 {
    text-align: center;
    color: #0ecd70;
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
    background-color: #08924d;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.2s;
  }

  button:hover {
    background-color: #15b039;
  }

  button:disabled {
    background-color: #9ac1f3;
    cursor: not-allowed;
  }
  
  .links {
    margin-top: 1rem;
    text-align: center;
  }
  
  a {
    color: #1ae851;
    text-decoration: none;
    font-size: 0.875rem;
  }
  
  a:hover {
    text-decoration: underline;
  }
</style>