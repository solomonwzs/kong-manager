export default {
  methods: {
    uGenUrlQuery (data) {
      var arr = []
      for (var k in data) {
        var v = data[k]
        if (v !== '' && v !== undefined) {
          arr.push(k + '=' + v)
        }
      }
      return arr.join('&')
    }
  }
}
