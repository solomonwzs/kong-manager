import Axios from 'axios'
import Cookie from 'vue-cookie'
import Vue from 'vue'

Vue.use(Cookie)
const env = process.env

export default {
  data () {
    return {
      'inName': '',
      'inPawd': '',
      'user': null
    }
  },

  methods: {
    login () {
      var body = {
        'name': this.inName,
        'pawd': this.inPawd
      }
      Axios.post(env.API_URL + '/login', body)
        .then(respose => {
          this.$cookie.set(env.COOKIE_F, respose.data.cookie, 1)
          this.user = respose.data.user
          this.$router.push('/')
        })
        .catch(error => {
          console.log(error)
        })
    },

    getUser () {
      const cookie = this.$cookie.get(env.COOKIE_F)
      if (cookie === null) {
        this.$router.push('/login')
        return
      }

      Axios.get(env.API_URL + '/user', {
        headers: {
          'X-Kong-Api-Cookie': cookie
        }
      }).then(respose => {
        this.user = {
          name: respose.data.name
        }
      }).catch(error => {
        console.log(error)
        this.$router.push('/login')
      })
    },

    logout () {
      this.$cookie.delete(env.COOKIE_F)
      this.user = null
      this.$router.push('/login')
    }
  }
}
