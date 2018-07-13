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
      'ksReqPage': 0,
      'ksReqOffset': {
        0: ''
      },
      'ksReqSize': '',
      'ksSerList': null,
      'ksSerListLoading': true
    }
  },

  mixins: [Utils],

  methods: {
    ksListServices () {
      const cookie = this.$cookie.get(env.COOKIE_F)
      if (cookie === null) {
        return
      }

      var query = this.uGenUrlQuery({
        'size': this.ksReqSize,
        'offset': this.ksReqOffset[this.ksReqPage]
      })

      this.ksSerListLoading = true
      Axios.get(apiUrl, {
        headers: {
          'X-Rf-Api-Cookie': cookie,
          'X-Rf-Kong-Ep': '/services?' + query
        }
      }).then(response => {
        var data = response.data
        Vue.set(this.ksReqOffset, this.ksReqPage + 1, data.offset)
        this.ksSerList = data.data
        this.ksSerListLoading = false
      }).catch(error => {
        console.log(error)
      })
    },

    ksUpdateService (data, onCb, errCb) {
      const cookie = this.$cookie.get(env.COOKIE_F)
      if (cookie === null) {
        return
      }

      var id = data.id
      var body = {}
      for (var k in data) {
        if (k !== 'id') {
          body[k] = data[k]
        }
      }

      Axios.patch(apiUrl, body, {
        headers: {
          'X-Rf-Api-Cookie': cookie,
          'X-Rf-Kong-Ep': '/services/' + id
        }
      }).then(response => {
        if (onCb !== undefined) {
          onCb(response)
        }
      }).catch(error => {
        if (errCb !== undefined) {
          errCb(error)
        }
      })
    },

    ksAddService (data, onCb, errCb) {
      const cookie = this.$cookie.get(env.COOKIE_F)
      if (cookie === null) {
        return
      }

      Axios.post(apiUrl, data, {
        headers: {
          'X-Rf-Api-Cookie': cookie,
          'X-Rf-Kong-Ep': '/services/'
        }
      }).then(response => {
        if (onCb !== undefined) {
          onCb(response)
        }
      }).catch(error => {
        if (errCb !== undefined) {
          errCb(error)
        }
      })
    }
  }
}
