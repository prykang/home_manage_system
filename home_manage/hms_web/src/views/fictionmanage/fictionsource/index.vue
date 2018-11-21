<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select clearable @change='handleFilter'  class="filter-item" style="width: 130px" v-model="listQuery.name" :placeholder="$t('table.source_name')">
        <!--versionQuery-->
        <el-option v-for="item in  sourceOptions" :key="item.key" :label="item.display_name" :value="item.key" >
        </el-option>
      </el-select>


      <el-button class="filter-item" type="primary" v-waves icon="el-icon-search" @click="handleFilter">{{$t('table.search')}}</el-button>
    </div>
    <div class="filter-container">
      <el-button :disabled="multipleSelection.length === 0" class="filter-item" type="danger" @click="handleSelectedDelete()">{{$t('table.delete_selected')}}
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-edit">{{$t('table.add_source')}}</el-button>

   </div>



    <el-table ref="multipleTable"  :key='tableKey' :data="list" v-loading="listLoading" element-loading-text="给我一点时间" border fit highlight-current-row
      style="width: 100%" @selection-change="handleSelectionChange">

      <el-table-column type="selection" width="55">
      </el-table-column>

      <el-table-column type="expand" >
        <template slot-scope="scope">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item :label="$t('table.source_name')">
              <span>{{scope.row.fields.name}}</span>
            </el-form-item>
            <el-form-item :label="$t('table.status')">
              <span>
                <el-tag >{{scope.row.fields.status}}</el-tag>
              </span>
            </el-form-item>
            <el-form-item :label="$t('table.site_url')">
              <span>{{scope.row.fields.site_url}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.use_count')">
              <span>{{scope.row.fields.use_count}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.success_count')">
              <span>{{scope.row.fields.success_count}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.success_rate')">
              <span>{{scope.row.fields.success_rate}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.remark')">
              <el-input
                style="width:300px"
                readonly
                type="textarea"
                :autosize="{ minRows: 1, maxRows: 6}"
                :rows="2" v-model="scope.row.fields.remark">
              </el-input>
            </el-form-item>

            <el-form-item :label="$t('table.creator')">
              <span>{{scope.row.fields.creator[0]}}</span>
            </el-form-item>
            <el-form-item :label="$t('table.mender')">
              <span>{{scope.row.fields.mender[0]}}</span>
            </el-form-item>
            <el-form-item :label="$t('table.update_datetime')">
              <span>{{scope.row.fields.update_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}')  }}</span>
            </el-form-item>

            <el-form-item :label="$t('table.create_datetime')">
              <span>{{scope.row.fields.create_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}') }}</span>
            </el-form-item>


          </el-form>
        </template>
      </el-table-column>

      <el-table-column align="center" :label="$t('table.id')" min-width="60">
        <template slot-scope="scope">
          <span>{{scope.row.pk}}</span>
        </template>
      </el-table-column>


      <el-table-column min-width="80px" align="center" :label="$t('table.source_name')">
        <template slot-scope="scope">
          <el-tag  type="success">{{scope.row.fields.name }}</el-tag>
        </template>
      </el-table-column>

            <el-table-column min-width="180px" align="center" :label="$t('table.site_url')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.site_url}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="80px" align="center" :label="$t('table.use_count')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.use_count}}</span>
        </template>
      </el-table-column>
      <el-table-column min-width="80px" align="center" :label="$t('table.success_count')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.success_count}}</span>
        </template>
      </el-table-column>
      <el-table-column min-width="80px" align="center" :label="$t('table.success_rate')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.success_rate}}</span>
        </template>
      </el-table-column>



      <el-table-column align="center" :label="$t('table.actions')" min-width="250px" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button type="primary" size="mini" @click="handleUpdate(scope.row)">{{$t('table.edit')}}</el-button>
          <el-button  size="mini" type="danger" @click="handleDelete(scope.row)">{{$t('table.delete')}}
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <div class="pagination-container">
      <el-pagination background @size-change="handleSizeChange" @current-change="handleCurrentChange" :current-page="listQuery.page" :page-sizes="[10,20,30, 50]" :page-size="listQuery.limit" layout="total, sizes, prev, pager, next, jumper" :total="total">
      </el-pagination>
    </div>

    <el-dialog :title="$t('form.create')" :visible.sync="dialogFormVisible" >
      <el-form :rules="rules" ref="dataForm" :model="temp" label-position="left" label-width="95px" style='width: 550px; margin-left:50px;'>

        <el-row>
          <el-form-item :label="$t('table.source_name')" prop="name" width="70px">
            <el-input v-model="temp.name"  placeholder="请输入资源名称"></el-input>
          </el-form-item>
        </el-row>

        <el-row>
          <el-form-item :label="$t('table.site_url')" prop="site_url" width="70px">
            <el-input v-model="temp.site_url"  placeholder="请输入资源网址"></el-input>
          </el-form-item>
        </el-row>




        <el-row>
          <el-form-item :label="$t('table.status')" prop="status" width="70px">
            <el-select  filterable class="filter-item" v-model="temp.status" placeholder="请选择状态" >
              <el-option v-for="item in  statusOptions" :key="item.key" :label="item.display_name" :value="item.key">
              </el-option>
            </el-select>
          </el-form-item>
        </el-row>

        <el-form-item :label="$t('table.remark')"  prop="remark">
          <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入备注（选填）" v-model="temp.remark">
          </el-input>
        </el-form-item>

<el-row>
          <el-form-item :label="$t('table.search_script')" prop="search_script" width="70px">
            <el-upload
              class="upload-demo"
              accept=".py"
              name="filename"
              :headers="headers"
              :action="searchAction"
              :on-success="handleSeachScriptSuccess"
              :limit="1"
              :file-list="search_script_fileList"
              show-file-list>
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传py文件</div>
            </el-upload>
          </el-form-item>
        </el-row>

        <el-row>
          <el-form-item :label="$t('table.download_script')" prop="download_script" width="70px">
            <el-upload
              class="upload-demo"
              accept=".py"
              name="filename"
              :headers="headers"
              :action="downloadAction"
              :on-success="handleDownloadScriptSuccess"
              :on-remove="handleDownloadScriptRemove"
              :limit="1"
              :file-list="download_script_fileList"
              show-file-list>
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传py文件</div>
            </el-upload>
          </el-form-item>
        </el-row>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">{{$t('table.cancel')}}</el-button>
        <el-button v-if="dialogStatus=='create'" type="primary" @click="addItemFunc">{{$t('table.confirm')}}</el-button>
        <el-button v-else type="primary" @click="editItemFunc">{{$t('table.confirm')}}</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import { getItem, addItem, deleteItems, editItem, getList, getSourceStatusList } from '@/api/fiction_source'
import waves from '@/directive/waves' // 水波纹指令
import { parseTime } from '@/utils'
import { Message } from 'element-ui'
import { getToken } from '@/utils'

export default {
  name: 'FictionSource',
  props: {
    headers: {
      type: Object,
      default() { return { Authorization: getToken() } }
    },
    searchAction: {
      type: String,
      default: 'http://127.0.0.1:8000/filemanager/api/upload_search_script_file'
    },
    downloadAction: {
      type: String,
      default: 'http://127.0.0.1:8000/filemanager/api/upload_download_script_file'
    }
  },
  directives: {
    waves
  },
  data() {
    return {
      search_script_fileList: [],
      download_script_fileList: [],
      tableData: [],
      tableHeader: [],
      tableKey: 0,
      list: null,
      total: null,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        name: '',
        author: ''
      },
      statusOptions: null,
      sourceOptions: null,
      sortOptions: [{ label: '正序', key: '+id' }, { label: '倒序', key: '-id' }],
      temp: {
        pk: '',
        name: '',
        search_script: '',
        download_script: '',
        status: 1,
        remark: ''
      },
      dialogFormVisible: false,
      dialogStatus: '',
      rules: {
        name: [{ required: true, message: '请输入资源名称', trigger: 'blur' }],
        site_url: [{ required: true, message: '请输入资源网址', trigger: 'blur' }],
        search_script: [{ required: false, message: '缺少搜索脚本', trigger: 'blur' }],
        download_script: [{ required: false, message: '缺少下载脚本', trigger: 'blur' }],
        status: [{ required: true, message: '请选择状态', trigger: 'change' }]
      },
      downloadLoading: false,
      multipleSelection: []
    }
  },
  filters: {
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    }
  },
  created() {
    this.getSourceStatusListFunc()
    this.getListFunc()
    this.initPage()
  },
  methods: {
    initPage() {
      console.log('this.$route.params.version', this.$route.params.version)
      var reg = new RegExp('^[0-9]*$')
      if (reg.test(this.$route.params.version)) {
        console.log('error--------')
        this.listQuery.version = this.$route.params.version
      } else {
        console.log('hello--------------------')
        this.$route.params.version = 'all'
        this.listQuery.version = ''
      }
    },
    selected(data) {
      this.tableData = data.results
      this.tableHeader = data.header
    },
    resetAuthorTemp() {
      this.author_temp = {
        name: ''
      }
    },
    handleSeachScriptSuccess(res) {
      const { code, data, msg } = res
      // console.log('res', res)
      if (code === '000000') {
        const { filename } = data
        this.search_script_fileList = [{
          name: filename
        }]
        this.temp.search_script = filename
        this.$emit('transferFileList', this.search_script_fileList)
      } else {
        this.$message.error(msg || '文件上传出错，请稍后重试！')
      }
    },
    handleDownloadScriptSuccess(res) {
      const { code, data, msg } = res
      if (code === '000000') {
        const { filename } = data
        this.download_script_fileList = [{
          name: filename
        }]
        this.temp.download_script = filename
        this.$emit('transferFileList', this.download_script_fileList)
      } else {
        this.$message.error(msg || '文件上传出错，请稍后重试！')
      }
    },
    handleDownloadScriptRemove() {
      this.temp.download_script = ''
      this.download_script_fileList = []
    },
    handleFictionTypeCreate() {
      this.resetFictionTypeTemp()
      this.dialogFictionTypeVisible = true
      this.$nextTick(() => {
        this.$refs['fiction_type_dataForm'].clearValidate()
      })
    },
    handleAuthorCreate() {
      this.resetAuthorTemp()
      this.dialogAuthorVisible = true
      this.$nextTick(() => {
        this.$refs['authordataForm'].clearValidate()
      })
    },
    getListFunc() {
      this.listLoading = true
      getList(this.listQuery).then(response => {
        console.log('response', response)
        this.list = response.data.items
        this.total = response.data.total
        this.listLoading = false
      }).catch(() => {
        this.list = []
        this.listLoading = false
      })
    },
    getSourceStatusListFunc() {
      getSourceStatusList({}).then(response => {
        this.statusOptions = response.data.items.map((array) => {
          var temp = {}
          temp['key'] = array.pk
          temp['display_name'] = array.fields.name
          return temp
        }, {})
        console.log(this.statusOptions)
      }).catch((err) => {
        Message.error(err.msg)
      })
    },
    handleFilter() {
      this.listQuery.page = 1
      this.getListFunc()
    },
    handleSizeChange(val) {
      this.listQuery.limit = val
      this.getListFunc()
    },
    handleCurrentChange(val) {
      this.listQuery.page = val
      this.getListFunc()
    },
    resetTemp() {
      this.temp = {
        pk: '',
        name: '',
        search_script: '',
        download_script: '',
        status: 1,
        remark: ''
      }
    },
    resetFictionTypeTemp() {
      this.fiction_type_temp = {
        name: ''
      }
    },
    handleCreate() {
      this.resetTemp()
      this.getSourceStatusListFunc()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    addItemFunc() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          addItem(this.temp).then((rsp) => {
            this.getListFunc()
            this.dialogFormVisible = false
            this.$message({
              message: rsp.msg,
              type: 'success'
            })
          })
        }
      })
    },
    getItemFunc(pk) {
      getItem({ pk: pk }).then(response => {
        this.temp = Object.assign({}, response.data.fields)
        this.temp.pk = response.data.pk
        if (this.temp.search_script !== '') {
          this.search_script_fileList = [{
            name: this.temp.search_script
          }]
        }
        if (this.temp.download_script !== '') {
          this.download_script_fileList = [{
            name: this.temp.download_script
          }]
        }
        // this.formVersionQuery.client_type = response.data.client_type
      })
    },
    handleUpdate(row) {
      this.getItemFunc(row.pk)
      this.dialogStatus = 'update'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    editItemFunc() {
      this.$refs['dataForm'].validate((valid) => {
        if (valid) {
          editItem(this.temp).then(() => {
            this.getListFunc()
            this.dialogFormVisible = false
            this.$message({
              type: 'success',
              message: '更新成功!'
            })
          })
        }
      })
    },
    deleteItemsFunc() {
      deleteItems({ 'ids': this.multipleSelection }).then(() => {
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
        this.multipleSelection = []
        this.handleFilter()
      })
    },
    handleSelectedDelete() {
      this.$confirm('此操作将永久删除这些记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.deleteItems()
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
        this.multipleSelection = []
        this.$refs.multipleTable.clearSelection()
      })
    },
    handleDelete(row) {
      this.multipleSelection = []
      this.multipleSelection.push(row.pk)
      this.$confirm('此操作将永久删除该记录, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.deleteItemsFunc()
      }).catch(() => {
        this.multipleSelection = []
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    handleSelectionChange(val) {
      this.multipleSelection = []
      this.multipleSelection = val.map(item => item.pk)
      console.log('multipleSelection', this.multipleSelection)
    },
    formatJson(filterVal, jsonData) {
      return jsonData.map(v => filterVal.map(j => {
        if (j === 'timestamp') {
          return parseTime(v[j])
        } else {
          return v[j]
        }
      }))
    }
  }
}
</script>

<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }
  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
