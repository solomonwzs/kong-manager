<template>
  <div>
    <el-row>
      <div class="button-panel-right">
        <el-button @click="openEditDialog('add')">add</el-button>
      </div>
    </el-row>

    <el-row>
      <el-table
        v-loading="ksSerListLoading"
        class="ks-ser-list"
        border
        :data="ksSerList">
        <el-table-column label="id">
          <template slot-scope="scope">
            <el-popover trigger="hover" placement="top">
              <p>created at: {{ scope.row.created_at }}</p>
              <p>updated at: {{ scope.row.updated_at }}</p>
              <p>retries: {{ scope.row.retries }}</p>
              <p>connect timeout: {{ scope.row.connect_timeout }}</p>
              <p>write timeout: {{ scope.row.write_timeout }}</p>
              <p>read timeout: {{ scope.row.read_timeout }}</p>
              <div slot="reference" class="name-wrapper">
                <i class="el-icon-info"></i>
                <span>{{ scope.row.id }}</span>
              </div>
            </el-popover>
          </template>
        </el-table-column>
        <el-table-column prop="name" label="name"></el-table-column>
        <el-table-column prop="protocol" label="protocol"></el-table-column>
        <el-table-column prop="host" label="host"></el-table-column>
        <el-table-column prop="path" label="path"></el-table-column>
        <el-table-column prop="port" label="port"></el-table-column>

        <el-table-column label="opt">
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="primary"
              @click="openEditDialog('edit',scope.row)">
              edit
            </el-button>
            <el-button
              size="mini"
              type="danger"
              @click="openDeleteDialog(scope.row.id)">
              delete
            </el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-dialog
        v-bind:title="editDialogTitle"
        width="60%"
        :visible.sync="showEditDialog" center>
        <service-edit
          v-on:eventCloseEditDialog="closeEditDialog"
          v-bind:serviceData="edService"
          v-bind:oriServiceData="oriService"
          v-bind:editOpt="edServiceOpt">
        </service-edit>
      </el-dialog>

      <el-dialog
        title="delete"
        :visible.sync="showDelDialog" center>
        <p>delete service [{{ delServiceId }}]?</p>
        <el-button
          type="danger"
          v-on:click="ksDeleteService(delServiceId,delOK,delFail)"
          >enter</el-button>
      </el-dialog>
    </el-row>

    <el-row>
      <el-button v-if='hasPrev' v-on:click="getPrevPage">prev</el-button>
      <el-button disabled v-else>prev</el-button>

      <el-button v-if='hasNext' v-on:click="getNextPage">next</el-button>
      <el-button disabled v-else>next</el-button>
    </el-row>
  </div>
</template>

<script>
import KongServices from '../js/KongServices'
import ServiceEdit from './ServiceEdit'
import Vue from 'vue'

export default {
  data () {
    return {
      'showEditDialog': false,
      'showDelDialog': false,

      'delServiceId': null,

      'edService': {},
      'oriService': null,
      'edServiceOpt': ''
    }
  },

  mixins: [KongServices],

  components: {
    'service-edit': ServiceEdit
  },

  computed: {
    hasPrev: function () {
      return !this.ksSerListLoading && this.ksReqPage !== 0
    },

    hasNext: function () {
      var offset = this.ksReqOffset[this.ksReqPage + 1]
      return !this.ksSerListLoading && offset !== undefined
    },

    editDialogTitle: function () {
      return this.edServiceOpt + ' service'
    }
  },

  methods: {
    getPrevPage () {
      this.ksReqPage -= 1
      this.ksListServices()
    },

    getNextPage () {
      this.ksReqPage += 1
      this.ksListServices()
    },

    openEditDialog (opt, row) {
      if (row !== undefined) {
        for (var k in row) {
          Vue.set(this.edService, k, row[k])
        }
        this.oriService = row
      } else {
        this.edService = {}
      }
      this.edServiceOpt = opt
      this.showEditDialog = true
    },

    openDeleteDialog (sid) {
      console.log(sid)
      this.delServiceId = sid
      this.showDelDialog = true
    },

    delOK (resp) {
      this.showDelDialog = false
      this.refreshList()

      this.$message({
        message: 'delete service [' + this.delServiceId + '] ok',
        type: 'success'
      })
    },

    delFail (e) {
      this.showDelDialog = false
      this.$message({
        message: 'error: ' + e.response.data.message,
        type: 'error'
      })
    },

    closeEditDialog (msg, refresh) {
      this.showEditDialog = false
      this.$message(msg)

      if (refresh === true) {
        this.refreshList()
      }
    },

    refreshList () {
      this.ksReqPage = 0
      this.ksListServices()
    }
  },

  beforeMount () {
    this.ksReqSize = 5
    this.ksListServices()
  }
}
</script>

<style>
.ks-ser-list {
  width: 100%;
}

.button-panel-right {
  float: right;
}
</style>
