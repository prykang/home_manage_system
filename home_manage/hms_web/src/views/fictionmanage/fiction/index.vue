<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select clearable @change='handleFilter'  class="filter-item" style="width: 130px" v-model="listQuery.fiction_type" :placeholder="$t('table.fiction_type')">
        <!--versionQuery-->
        <el-option v-for="item in  fictionTypeOptions" :key="item.key" :label="item.display_name" :value="item.key" >
        </el-option>
      </el-select>
      <el-select clearable @change='handleFilter'  class="filter-item" style="width: 130px" v-model="listQuery.status" :placeholder="$t('table.status')">
        <!--versionQuery-->
        <el-option v-for="item in  statusOptions" :key="item.key" :label="item.display_name" :value="item.key" >
        </el-option>
      </el-select>

      <el-select clearable @change='handleFilter' class="filter-item" style="width: 200px" v-model="listQuery.author" :placeholder="$t('table.author')">
        <el-option v-for="item in  authorOptions" :key="item.key" :label="item.display_name" :value="item.key">
        </el-option>
      </el-select>


      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" class="filter-item" :placeholder="$t('table.fiction_name')" v-model="listQuery.name">
      </el-input>


      <el-button class="filter-item" type="primary" v-waves icon="el-icon-search" @click="handleFilter">{{$t('table.search')}}</el-button>
    </div>
    <div class="filter-container">
      <el-button :disabled="multipleSelection.length === 0" class="filter-item" type="danger" @click="handleSelectedDelete()">{{$t('table.delete_selected')}}
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-edit">{{$t('table.add_fiction')}}</el-button>

   </div>



    <el-table ref="multipleTable"  :key='tableKey' :data="list" v-loading="listLoading" element-loading-text="给我一点时间" border fit highlight-current-row
      style="width: 100%" @selection-change="handleSelectionChange">

      <el-table-column type="selection" width="55">
      </el-table-column>

      <el-table-column type="expand" >
        <template slot-scope="scope">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item :label="$t('table.fiction_name')">
              <span>
                {{scope.row.fields.name}}
              </span>
            </el-form-item>
            <el-form-item :label="$t('table.fiction_type')">
              <span>
                <el-tag type="success">{{scope.row.fields.fiction_type }}</el-tag>
              </span>
            </el-form-item>
            <el-form-item :label="$t('table.author')">
              <span>{{scope.row.fields.author}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.status')">
              <span>
                <el-tag type="warning">{{scope.row.fields.status}}</el-tag>
              </span>
            </el-form-item>

            <el-form-item :label="$t('table.source')">
              <span>{{scope.row.fields.source}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.file_path')">
              <span>{{scope.row.fields.file_path}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.dialysis_pic')">
              <span>{{scope.row.fields.dialysis_pic}}</span>
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


      <el-table-column min-width="80px" align="center" :label="$t('table.fiction_type')">
        <template slot-scope="scope">
          <el-tag  type="success">{{scope.row.fields.fiction_type }}</el-tag>
        </template>
      </el-table-column>

            <el-table-column min-width="150px" align="center" :label="$t('table.author')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.author}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="180px" align="center" :label="$t('table.fiction_name')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.name}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="180px" align="center" :label="$t('table.status')">
        <template slot-scope="scope">

          <span>
            <el-tag type="warning">{{scope.row.fields.status}}</el-tag>
          </span>
        </template>
      </el-table-column>


      <el-table-column min-width="200px" align="center" :label="$t('table.date')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.update_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}')}}</span>
        </template>
      </el-table-column>



      <el-table-column align="center" :label="$t('table.actions')" min-width="250px" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button :disabled="scope.row.fields.status === '下载中'" type="success" size="mini" @click="handleStatusChange(scope.row.pk)">{{$t('table.start')}}</el-button>-
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
       <el-dialog width="30%" title="添加作者" :visible.sync="dialogAuthorVisible" append-to-body>
           <el-form :rules="authorrules" ref="authordataForm" :model="author_temp" label-position="left" label-width="70px" style='width: 300px; margin-left:30px;'>
            <el-form-item :label="$t('table.author')" prop="author" width="50px">
              <el-input v-model="author_temp.name"  placeholder="请输入作者"></el-input>
            </el-form-item>
           </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogAuthorVisible = false">{{$t('table.cancel')}}</el-button>
              <el-button  type="primary" @click="createAuthorData">{{$t('table.confirm')}}</el-button>
            </div>
      </el-dialog>

      <el-dialog width="40%" title="添加小说类型" :visible.sync="dialogFictionTypeVisible" append-to-body>
        <el-form :rules="fiction_type_rules" ref="fiction_type_dataForm" :model="fiction_type_temp" label-position="left" label-width="70px" style='width: 300px; margin-left:30px;'>
          <el-form-item :label="$t('table.fiction_type')" prop="country" width="50px">
            <el-input v-model="fiction_type_temp.name"  placeholder="请输入小说类型"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="dialogFictionTypeVisible = false">{{$t('table.cancel')}}</el-button>
          <el-button  type="primary" @click="createFictionTypeData">{{$t('table.confirm')}}</el-button>
        </div>
      </el-dialog>

      <el-form :rules="rules" ref="dataForm" :model="temp" label-position="left" label-width="95px" style='width: 550px; margin-left:50px;'>

      <el-row>
        <el-col :span="12">
          <el-form-item :label="$t('table.fiction_type')" prop="fiction_type">
            <el-select class="filter-item" v-model="temp.fiction_type" placeholder="请选择小说类型">
              <el-option v-for="item in  fictionTypeOptions" :key="item.key" :label="item.display_name" :value="item.key">
              </el-option>
            </el-select>
          </el-form-item>
        </el-col>

          <el-col :span="12">
            <span>
              <el-button type="primary" icon="el-icon-plus" @click="handleFictionTypeCreate"></el-button>
            </span>
          </el-col>
      </el-row>

        <el-row>
          <el-col :span="12">

            <el-form-item :label="$t('table.author')" prop="author" width="70px">
              <el-select  filterable class="filter-item" v-model="temp.author" placeholder="请选择作者" >
                <el-option v-for="item in  authorOptions" :key="item.key" :label="item.display_name" :value="item.key">
                </el-option>
              </el-select>
            </el-form-item>

          </el-col>

          <el-col :span="12">
            <span>
              <el-button type="primary" icon="el-icon-plus" @click="handleAuthorCreate"></el-button>
            </span>
          </el-col>
        </el-row>

        <el-row>
          <el-form-item :label="$t('table.fiction_name')" prop="name" width="70px">
            <el-input v-model="temp.name"  placeholder="请输入小说名称"></el-input>
          </el-form-item>
        </el-row>

        <el-form-item :label="$t('table.remark')"  prop="remark">
          <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="请输入备注（选填）" v-model="temp.remark">
          </el-input>
        </el-form-item>



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
import { getItem, addItem, deleteItems, editItem, getList, getAuthorList, addAuthor, getFictionType, addFictionType, startSearchDownload } from '@/api/fiction'
import waves from '@/directive/waves' // 水波纹指令
import { parseTime } from '@/utils'
import { Message } from 'element-ui'

export default {
  name: 'Fiction',
  directives: {
    waves
  },
  data() {
    return {
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
        status: '',
        fiction_type: '',
        author: ''
      },
      fictionTypeOptions: null,
      authorOptions: null,
      sortOptions: [{ label: '正序', key: '+id' }, { label: '倒序', key: '-id' }],
      temp: {
        pk: '',
        name: '',
        author: '',
        status: 0,
        tags: [],
        remark: ''
      },
      author_temp: {
        name: ''
      },
      fiction_type_temp: {
        name: ''
      },
      dialogFormVisible: false,
      dialogAuthorVisible: false,
      dialogFictionTypeVisible: false,
      dialogStatus: '',
      rules: {
        fiction_type: [{ required: true, message: '请选择小说类型', trigger: 'change' }],
        author: [{ required: true, message: '请选择作者', trigger: 'change' }],
        name: [{ required: true, message: '请输入小说名称', trigger: 'blur' }]
      },
      authorrules: {
        name: [{ required: true, message: '请输入作者名', trigger: 'blur' }]
      },
      fiction_type_rules: {
        name: [{ required: true, message: '请输入小说分类', trigger: 'blur' }]
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
    this.getFictionTypeFunc()
    this.getAuthorListFunc()
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
    // on_or_off(status) {
    //   console.log('status', status)
    //   if (status === '未开始') {
    //     return true
    //   } else {
    //     return false
    //   }
    // },
    resetAuthorTemp() {
      this.author_temp = {
        name: ''
      }
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
    createFictionTypeData() {
      this.$refs['fiction_type_dataForm'].validate((valid) => {
        if (valid) {
          addFictionType(this.fiction_type_temp).then((rsp) => {
            this.getFictionTypeFunc()
            this.dialogFictionTypeVisible = false
            this.$message({
              message: rsp.msg,
              type: 'success'
            })
          })
        }
      })
    },
    createAuthorData() {
      this.$refs['authordataForm'].validate((valid) => {
        if (valid) {
          addAuthor(this.author_temp).then((rsp) => {
            this.getAuthorListFunc()
            this.dialogAuthorVisible = false
            this.$message({
              message: rsp.msg,
              type: 'success'
            })
          })
        }
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
    getFictionTypeFunc() {
      getFictionType({}).then(response => {
        this.fictionTypeOptions = response.data.items.map((array) => {
          var temp = {}
          temp['key'] = array.pk
          temp['display_name'] = array.fields.name
          return temp
        }, {})
        console.log(this.bankcardTypeOptions)
      }).catch((err) => {
        Message.error(err.msg)
      })
    },
    getAuthorListFunc() {
      getAuthorList({}).then(response => {
        this.authorOptions = response.data.items.map((array) => {
          var temp = {}
          temp['key'] = array.pk
          temp['display_name'] = array.fields.name
          return temp
        }, {})
        console.log(this.authorOptions)
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
        author: ''
      }
    },
    resetFictionTypeTemp() {
      this.fiction_type_temp = {
        name: ''
      }
    },
    handleCreate() {
      this.resetTemp()
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
        // this.formVersionQuery.client_type = response.data.client_type
      })
    },
    handleStatusChange(pk) {
      console.log('status change!')
      startSearchDownload({ pk: pk }).then(response => {
        this.getListFunc()
        this.$message({
          type: 'success',
          message: response['msg']
        })
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
          const tempData = Object.assign({}, this.temp)
          editItem(tempData).then(() => {
            this.getList()
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
