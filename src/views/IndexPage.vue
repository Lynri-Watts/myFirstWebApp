<!-- <script setup>
import { ref } from 'vue'

// 必须使用ref声明响应式变量
const username = ref(localStorage.getItem("username"))
</script>

<template>
     <div class="container">
         <img alt="Vue logo" src="../assets/logo.png">
         <br>
         <div class="login-container">
             <h2>用户登录</h2>
             <div class="text">
                 你好！{{ username }}
             </div>
             <form @submit.prevent="handleSubmit">
                 <button type="submit" :disabled="isSubmitting">
                     {{ isSubmitting ? '退出中...' : '退出登录' }}
                 </button>
             </form>
         </div>
     </div>
 </template>

<script>
// eslint-disable-next-line
import { reactive, computed } from 'vue';
import { useRouter } from 'vue-router'
const router = useRouter()
console.log(router)
const isSubmitting = ref(false);
const handleSubmit = async () => {
    isSubmitting.value = true;
    try {
        const response = await fetch('http://localhost:5000/api/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '退出失败');
        }
        // 存储Token到localStorage
        // localStorage.setItem('access_token', data.data.access_token);
        console.log(data)
        localStorage.setItem('username', "")
        console.log(router)
        router.push('/login'); //TODO

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
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    width: 320px;
}

h2 {
    text-align: center;
    color: #1a73e8;
    margin-bottom: 1.5rem;
}

.text {
    font-size: 1em;
    color: black
}
</style> -->


<template>
    <div class="container">
        <img alt="Vue logo" src="../assets/logo.png">
        <br>
        <div class="login-container">
            <h2>登陆成功！</h2>
            <form @submit.prevent="handleSubmit">
                <div class="text">
                    你好！{{ username }}
                </div>
                <button type="submit" :disabled="isSubmitting">
                    {{ isSubmitting ? '退出中...' : '退出登录' }}
                </button>

            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router'

const isSubmitting = ref(false);
const username = ref(localStorage.getItem("username"))

const router = useRouter()

const handleSubmit = async () => {
    isSubmitting.value = true;

    try {
        const response = await fetch('http://localhost:5000/api/logout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.message || '退出失败');
        }

        // 存储Token到localStorage
        // localStorage.setItem('access_token', data.data.access_token);
        console.log(data)
        localStorage.setItem('username', "")
        console.log(router)
        router.push('/login'); //TODO

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
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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