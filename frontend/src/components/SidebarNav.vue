<template>
  <el-menu
    @select="sNavSelect"
    v-bind:default-active="sNavActive"
    class="el-menu-vertical-demo">
    <el-menu-item index="1">
      <span slot="title">Services</span>
    </el-menu-item>
    <el-menu-item index="2">
      <span slot="title">Routes</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  data () {
    return {
    }
  },

  props: ['sNavActive'],

  methods: {
    sNavSelect (index, indexPath) {
      this.$emit('eventSelectSNav', index)
    }
  }
}
</script>
