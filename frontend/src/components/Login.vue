<template>
  <div v-if="user">
    <p>hello, {{ user.name }}</p>
    <p>
      <button v-on:click="get_user">user</button>
      <button v-on:click="logout">logout</button>
    </p>
  </div>
  <div v-else>
    <p>
      <span>username</span>
      <input v-model="in_name">
    </p>
    <p>
      <span>passowrd</span>
      <input v-model="in_pawd">
    </p>
    <p>
      <button v-on:click="login">login</button>
    </p>
  </div>
</template>

<script>
import axios from 'axios'
import vue from 'vue'
import cookie from 'vue-cookie'

vue.use(cookie)
const env = process.env

export default {
  data () {
    return {
      'in_name': 'xx',
      'in_pawd': 'yy',
      'user': null
    }
  },

  methods: {
    login () {
      var body = {
        'name': this.in_name,
        'pawd': this.in_pawd
      }
      axios.post(env.API_URL + '/login', body)
        .then(respose => {
          console.log(respose.data.cookie)
          this.$cookie.set(env.COOKIE_F, respose.data.cookie, 1)
          this.user = respose.data.user
        })
        .catch(error => {
          console.log(error)
        })
    },

    logout () {
      this.$cookie.delete(env.COOKIE_F)
      this.user = null
    },

    get_user () {
      const cookie = this.$cookie.get(env.COOKIE_F)
      axios.get(env.API_URL + '/user', {
        headers: {
          'X-Rf-Api-Cookie': cookie
        }
      })
        .then(respose => {
          console.log(respose)
          this.user = {
            name: respose.data.name
          }
        })
        .catch(error => {
          console.log(error)
        })
    }
  },

  beforeMount () {
    this.get_user()
  }
}
</script>
