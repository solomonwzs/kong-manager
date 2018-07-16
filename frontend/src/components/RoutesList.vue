<template>
  <div>
    <el-row>
      <el-table
        v-loading="krRoutesListLoading"
        border
        :data="krRoutesList">
        <el-table-column prop="id" label="id"></el-table-column>
        <el-table-column prop="protocols" label="protocols">
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
import KongRoutes from '../js/KongRoutes'

export default {
  data () {
    return {}
  },

  props: ['serviceId'],

  mixins: [KongRoutes],

  beforeMount () {
    this.krListRoutes()
  }
}
</script>
