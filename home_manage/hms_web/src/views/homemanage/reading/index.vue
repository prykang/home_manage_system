<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select clearable @change='handleFilter'  class="filter-item" style="width: 130px" v-model="listQuery.name" :placeholder="$t('table.reading_plan_name')">
        <!--versionQuery-->
        <el-option v-for="item in  readingPlanTypeOptions" :key="item.key" :label="item.display_name" :value="item.key" >
        </el-option>
      </el-select>



      <el-button class="filter-item" type="primary" v-waves icon="el-icon-search" @click="handleFilter">{{$t('table.search')}}</el-button>
    </div>
    <div class="filter-container">
      <el-button :disabled="multipleSelection.length === 0" class="filter-item" type="danger" @click="handleSelectedDelete()">{{$t('table.delete_selected')}}
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-edit">{{$t('table.add_reading_plan')}}</el-button>

   </div>



    <el-table ref="multipleTable"  :key='tableKey' :data="list" v-loading="listLoading" element-loading-text="给我一点时间" border fit highlight-current-row
      style="width: 100%" @selection-change="handleSelectionChange">

      <el-table-column type="selection" width="55">
      </el-table-column>

      <el-table-column type="expand" >
        <template slot-scope="scope">
          <el-form label-position="left" inline class="demo-table-expand">
            <!--<el-form-item :label="$t('table.book_type')">-->
                <!--<el-tag  type="success">{{scope.row.fields.book }}</el-tag>-->
            <!--</el-form-item>-->
            <el-form-item :label="$t('table.book')">
              <span>{{scope.row.fields.book}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.overdue_day')">
              <span>{{scope.row.fields.overdue_day}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.status')">
              <span>{{scope.row.fields.status}}</span>
            </el-form-item>

            <el-form-item :label="$t('table.start_datetime')">
              <span>{{scope.row.fields.start_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}')  }}</span>
            </el-form-item>

            <el-form-item :label="$t('table.end_datetime')">
              <span>{{scope.row.fields.end_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}') }}</span>
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



      <el-table-column min-width="150px" align="center" :label="$t('table.reading_plan_name')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.name}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="180px" align="center" :label="$t('table.book')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.book}}</span>
        </template>
      </el-table-column>



      <el-table-column min-width="80px" align="center" :label="$t('table.status')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.status}}</span>
        </template>
      </el-table-column>


      <el-table-column min-width="200px" align="center" :label="$t('table.start_datetime')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.start_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}')}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="200px" align="center" :label="$t('table.end_datetime')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.end_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}')}}</span>
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
       <el-dialog width="40%" title="添加图书" :visible.sync="dialogBookVisible" append-to-body>
          <el-dialog width="40%" title="添加作者" :visible.sync="dialogAuthorVisible" append-to-body>
            <el-dialog width="40%" title="添加国家" :visible.sync="dialogCountryVisible" append-to-body>
              <el-form :rules="countryrules" ref="countrydataForm" :model="country_temp" label-position="left" label-width="70px" style='width: 300px; margin-left:30px;'>
                <el-form-item :label="$t('table.country')" prop="country" width="50px">
                  <el-input v-model="country_temp.name"  placeholder="请输入国家"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button @click="dialogCountryVisible = false">{{$t('table.cancel')}}</el-button>
                <el-button  type="primary" @click="createCountryData">{{$t('table.confirm')}}</el-button>
              </div>
            </el-dialog>

            <el-form :rules="authorrules" ref="authordataForm" :model="author_temp" label-position="left" label-width="70px" style='width: 300px; margin-left:30px;'>
              <el-form-item :label="$t('table.author')" prop="author" width="50px">
                <el-input v-model="author_temp.name"  placeholder="请输入作者"></el-input>
              </el-form-item>
              <el-row>
                <el-col :span="19">
                  <el-form-item :label="$t('table.country')" prop="country" >
                    <el-select  filterable class="filter-item" v-model="author_temp.country" placeholder="请选择国家或地区" >
                      <el-option v-for="item in  countryOptions" :key="item.key" :label="item.display_name" :value="item.key">
                      </el-option>
                    </el-select>
                  </el-form-item>
                </el-col>

                <el-col :span="5">
                  <span>
                    <el-button type="primary" icon="el-icon-plus" @click="handleCountryCreate"></el-button>
                  </span>
                </el-col>
              </el-row>

            </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogAuthorVisible = false">{{$t('table.cancel')}}</el-button>
              <el-button  type="primary" @click="createAuthorData">{{$t('table.confirm')}}</el-button>
            </div>
          </el-dialog>
           <el-form :rules="bookrules" ref="bookdataForm" :model="book_temp" label-position="left" label-width="70px" style='width: 300px; margin-left:30px;'>
              <el-form-item :label="$t('table.book')" prop="book" width="50px">
                <el-input v-model="book_temp.name"  placeholder="请输入图书"></el-input>
              </el-form-item>
            <el-row>

              <el-col :span="18">
                <el-form-item :label="$t('table.author')" prop="author" >
                  <el-select  filterable class="filter-item" v-model="book_temp.author" placeholder="请选择作者" >
                    <el-option v-for="item in  authorOptions" :key="item.key" :label="item.display_name" :value="item.key">
                    </el-option>
                  </el-select>
                </el-form-item>
              </el-col>

              <el-col :span="6">
                <span>
                  <el-button type="primary" icon="el-icon-plus" @click="handleAuthorCreate"></el-button>
                </span>
              </el-col>
            </el-row>

           </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogBookVisible = false">{{$t('table.cancel')}}</el-button>
              <el-button  type="primary" @click="createBookData">{{$t('table.confirm')}}</el-button>
            </div>
      </el-dialog>

      <el-form :rules="rules" ref="dataForm" :model="temp" label-position="left" label-width="95px" style='width: 550px; margin-left:50px;'>


        <el-row>
          <el-form-item :label="$t('table.reading_plan_name')" prop="name" width="70px">
            <el-input v-model="temp.name"  placeholder="请输入阅读计划名称"></el-input>
          </el-form-item>
        </el-row>

        <el-row>
          <el-col :span="12">

            <el-form-item :label="$t('table.book')" prop="book" width="70px">
              <el-select  filterable class="filter-item" v-model="temp.book" placeholder="请选择图书" >
                <el-option v-for="item in  bookOptions" :key="item.key" :label="item.display_name" :value="item.key">
                </el-option>
              </el-select>
            </el-form-item>

          </el-col>

          <el-col :span="12">
            <span>
              <el-button type="primary" icon="el-icon-plus" @click="handleBookCreate"></el-button>
            </span>
          </el-col>
        </el-row>


        <el-row>
          <el-form-item :label="$t('table.start_end_time')" prop="book" width="70px">
            <el-date-picker
              v-model="temp.start_end_time"
              type="daterange"
              align="right"
              unlink-panels
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
              :picker-options="pickerOptions2">
            </el-date-picker>
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
import { getItem, addItem, deleteItems, editItem, getList, addBook, getBookList, addAuthor, getAuthorList, addCountry, getCountryList } from '@/api/reading'
import waves from '@/directive/waves' // 水波纹指令
import { parseTime } from '@/utils'
import { Message } from 'element-ui'

export default {
  name: 'Reading',
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
      formVersionQuery: {
        client_type: ''
      },
      formSubModuleQuery: {
        module: ''
      },
      submoduleQuery: {
        module: ''
      },
      listQuery: {
        page: 1,
        limit: 20,
        bookcard_type: '',
        book: '',
        bookcard_num: ''
      },
      bookOptions: null,
      countryOptions: null,
      authorOptions: null,
      sortOptions: [{ label: '正序', key: '+id' }, { label: '倒序', key: '-id' }],
      temp: {
        pk: '',
        name: '',
        start_end: '',
        book: '',
        start_datetime: '',
        end_datetime: '',
        remark: ''
      },
      book_temp: {
        name: '',
        author: ''
      },
      author_temp: {
        name: '',
        country: ''
      },
      country_temp: {
        name: ''
      },
      dialogFormVisible: false,
      dialogBookVisible: false,
      dialogAuthorVisible: false,
      dialogCountryVisible: false,
      dialogStatus: '',
      rules: {
        name: [{ required: false, message: '请输入阅读计划名称', trigger: 'blur' }],
        book: [{ required: true, message: '请选择发卡银行', trigger: 'change' }],
        start_end_time: [{ required: false, message: '请输入起止日期', trigger: 'blur' }],
        remark: [{ required: false, message: '请输入备注', trigger: 'blur' }]
      },
      downloadLoading: false,
      multipleSelection: [],
      pickerOptions2: {
        shortcuts: [{
          text: '最近一周',
          onClick(picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '最近一个月',
          onClick(picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30)
            picker.$emit('pick', [start, end])
          }
        }, {
          text: '最近三个月',
          onClick(picker) {
            const end = new Date()
            const start = new Date()
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90)
            picker.$emit('pick', [start, end])
          }
        }]
      }
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
    this.getBookListFunc()
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
    resetBookTemp() {
      this.book_temp = {
        name: ''
      }
    },
    resetAuthorTemp() {
      this.author_temp = {
        name: ''
      }
    },
    resetCountryTemp() {
      this.country_temp = {
        name: ''
      }
    },
    handleBookCreate() {
      this.resetBookTemp()
      this.getAuthorListFunc()
      this.dialogBookVisible = true
      this.$nextTick(() => {
        this.$refs['bookdataForm'].clearValidate()
      })
    },
    handleAuthorCreate() {
      this.resetAuthorTemp()
      this.getCountryListFunc()
      this.dialogAuthorVisible = true
      this.$nextTick(() => {
        this.$refs['authordataForm'].clearValidate()
      })
    },
    handleCountryCreate() {
      this.resetCountryTemp()
      this.dialogCountryVisible = true
      this.$nextTick(() => {
        this.$refs['countrydataForm'].clearValidate()
      })
    },
    createBookData() {
      this.$refs['bookdataForm'].validate((valid) => {
        if (valid) {
          addBook(this.book_temp).then((rsp) => {
            this.getBookListFunc()
            this.dialogBookVisible = false
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
    createCountryData() {
      this.$refs['countrydataForm'].validate((valid) => {
        if (valid) {
          addCountry(this.country_temp).then((rsp) => {
            this.getCountryListFunc()
            this.dialogCountryVisible = false
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
    getBookListFunc() {
      getBookList({}).then(response => {
        this.bookOptions = response.data.items.map((array) => {
          var temp = {}
          temp['key'] = array.pk
          temp['display_name'] = array.fields.name
          return temp
        }, {})
        console.log(this.bookOptions)
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
    getCountryListFunc() {
      getCountryList({}).then(response => {
        this.countryOptions = response.data.items.map((array) => {
          var temp = {}
          temp['key'] = array.pk
          temp['display_name'] = array.fields.name
          return temp
        }, {})
        console.log(this.countryOptions)
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
        bookcard_type: '',
        book: '',
        bookcard_num: '',
        bill_day: '',
        repay_day: '',
        valid_until: '',
        annual_fee: '',
        is_free: true,
        free_condition: '',
        remark: ''
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
          this.temp.start_datetime = this.temp.start_end_time[0]
          this.temp.end_datetime = this.temp.start_end_time[1]
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
