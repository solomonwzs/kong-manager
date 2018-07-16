import Axios from 'axios'
import Cookie from 'vue-cookie'
import Vue from 'vue'
import Utils from './Utils'

Vue.use(Cookie)
const env = process.env
const apiUrl = env.API_URL + '/kong'

export default {
  data () {
    return {
      'krReqPage': 0,
      'krReqOffset': {
        0: ''
      },
      'krReqSize': '',
      'krRoutesList': null,
      'krRoutesListLoading': true
    }
  },

  mixins: [Utils],

  methods: {
    krListRoutes () {
      const cookie = this.$cookie.get(env.COOKIE_F)
      if (cookie === null) {
        return
      }

      var ep
      if (this.serviceId !== null) {
        ep = '/services/' + this.serviceId + '/routes'
      } else {
        var query = this.uGenUrlQuery({
          'size': this.krReqSize,
          'offset': this.krReqOffset[this.krReqPage]
        })
        ep = '/routes?' + query
      }

      this.krRoutesListLoading = true
      Axios.get(apiUrl, {
        headers: {
          'X-Kong-Api-Cookie': cookie,
          'X-Kong-Endpoint': ep
        }
      }).then(response => {
        var data = response.data
        Vue.set(this.krReqOffset, this.krReqPage + 1, data.offset)
        this.krRoutesList = data.data
        this.krRoutesListLoading = false
      }).catch(error => {
        console.log(error)
      })
    }
  }
}
