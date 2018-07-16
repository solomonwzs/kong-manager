<template>
  <el-form ref="serviceData" :model="serviceData" label-width="20%">
    <el-form-item label="name">
      <el-input v-model="serviceData.name"></el-input>
    </el-form-item>
    <el-form-item label="retries">
      <el-input v-model="serviceData.retries"></el-input>
    </el-form-item>
    <el-form-item label="protocol">
      <el-input v-model="serviceData.protocol"></el-input>
    </el-form-item>
    <el-form-item label="host">
      <el-input v-model="serviceData.host"></el-input>
    </el-form-item>
    <el-form-item label="port">
      <el-input v-model="serviceData.port"></el-input>
    </el-form-item>
    <el-form-item label="path">
      <el-input v-model="serviceData.path"></el-input>
    </el-form-item>
    <el-form-item label="connect timeout">
      <el-input v-model="serviceData.connect_timeout"></el-input>
    </el-form-item>
    <el-form-item label="write timeout">
      <el-input v-model="serviceData.write_timeout"></el-input>
    </el-form-item>
    <el-form-item label="read timeout">
      <el-input v-model="serviceData.read_timeout"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button
        type="primary"
        v-if="editOpt==='edit'"
        v-on:click="ksUpdateService(serviceData,updateOK,saveFail)">
        save</el-button>
      <el-button
        type="primary"
        v-else
        v-on:click="ksAddService(serviceData,createOK,saveFail)">
        add</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import KongServices from '../js/KongServices'
import Vue from 'vue'

export default {
  props: ['serviceData', 'editOpt', 'oriServiceData'],

  mixins: [KongServices],

  methods: {
    updateOK (resp) {
      for (var k in resp.data) {
        Vue.set(this.oriServiceData, k, resp.data[k])
      }

      var msg = {
        message: 'update service [' + this.serviceData.id + '] ok',
        type: 'success'
      }
      this.$emit('eventCloseEditDialog', msg)
    },

    createOK (resp) {
      var msg = {
        message: 'add service [' + resp.data.id + '] ok',
        type: 'success'
      }
      this.$emit('eventCloseEditDialog', msg, true)
    },

    saveFail (e) {
      var msg = {
        message: 'error: ' + e.response.data.message,
        type: 'error'
      }
      this.$message(msg)
    }
  }
}
</script>
