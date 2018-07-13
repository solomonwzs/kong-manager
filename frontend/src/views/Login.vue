<template>
  <el-main>
    <div v-if="user">
      <p>hello, {{ user.name }}</p>
      <p>
        <el-button v-on:click="getUser">user</el-button>
        <el-button v-on:click="logout">logout</el-button>
      </p>
    </div>

    <el-form v-else label-width="20%" class="login-panel">
      <el-form-item label="username">
        <el-input v-model="inName"></el-input>
      </el-form-item>
      <el-form-item label="password">
        <el-input v-model="inPawd" type="password"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button v-on:click="login">login</el-button>
      </el-form-item>
    </el-form>
  </el-main>
</template>

<script>
import UserManager from '../js/UserManager'

export default {
  mixins: [UserManager],

  beforeMount () {
    this.getUser()
  }
}
</script>

<style>
.login-panel {
  width: 50%;
}
</style>
