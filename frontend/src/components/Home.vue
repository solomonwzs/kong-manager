<template>
  <div>
    <p>Home page</p>
    <p>{{ bar }}</p>
    <p>{{ endpoint }}</p>
  </div>
</template>

<script>
const env = process.env

export default {
  name: 'Home',
  data () {
    return {
      n: 0,
      foo: 'hello',
      endpoint: env.API_URL
    }
  },
  created: function () {
    console.log('hello world')
  },
  computed: {
    bar: function () {
      return this.foo + ' xx'
    }
  }
}
</script>
