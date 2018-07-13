<template>
  <el-container>
    <el-header>
      <div v-if="user" class="top-user-panel">
        <span>hi, {{ user.name }} </span>
        <el-button v-on:click="logout">logout</el-button>
      </div>
    </el-header>

    <el-container>
      <el-aside width="20%">
      </el-aside>

      <el-main>
        <services-list></services-list>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import UserManager from '../js/UserManager'
import ServicesList from '../components/ServicesList'

export default {
  data () {
    return {
      'x': 2,
      'posts': {
        'key': 'hello',
        'value': 'world'
      }
    }
  },

  mixins: [UserManager],

  components: {
    'services-list': ServicesList
  },

  beforeMount () {
    this.getUser()
  }
}
</script>

<style>
.el-row {
  margin-bottom: 8px;
  &:last-child {
    margin-bottom: 0;
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-light {
  background: #e5e9f2;
}

.grid-content {
  border-radius: 6px;
  min-height: 32px;
}

.top-user-panel {
  float: right;
}
</style>
