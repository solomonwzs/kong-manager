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
        <sidebar-nav
          v-on:eventSelectSNav="selectSNav"
          v-bind:sNavActive="sNavActive"></sidebar-nav>
      </el-aside>

      <el-main>
        <services-list
          v-if="sNavActive === '1'"
          ></services-list>
      </el-main>
    </el-container>
  </el-container>
</template>

<script>
import ServicesList from '../components/ServicesList'
import SidebarNav from '../components/SidebarNav.vue'
import UserManager from '../js/UserManager'

export default {
  data () {
    return {
      'sNavActive': '1'
    }
  },

  mixins: [UserManager],

  components: {
    'services-list': ServicesList,
    'sidebar-nav': SidebarNav
  },

  methods: {
    selectSNav (index) {
      this.sNavActive = index
    }
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
