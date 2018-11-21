<template>
  <div class="app-container">
    <div class="filter-container">
      <el-select clearable @change='handleFilter'  class="filter-item" style="width: 130px" v-model="listQuery.bankcard_type" :placeholder="$t('table.bankcard_type')">
        <!--versionQuery-->
        <el-option v-for="item in  bankcardTypeOptions" :key="item.key" :label="item.display_name" :value="item.key" >
        </el-option>
      </el-select>

      <el-select clearable @change='handleFilter' class="filter-item" style="width: 200px" v-model="listQuery.bank" :placeholder="$t('table.bank')">
        <el-option v-for="item in  bankOptions" :key="item.key" :label="item.display_name" :value="item.key">
        </el-option>
      </el-select>


      <el-input @keyup.enter.native="handleFilter" style="width: 200px;" class="filter-item" :placeholder="$t('table.bankcard_num')" v-model="listQuery.bankcard_num">
      </el-input>


      <el-button class="filter-item" type="primary" v-waves icon="el-icon-search" @click="handleFilter">{{$t('table.search')}}</el-button>
    </div>
    <div class="filter-container">
      <el-button :disabled="multipleSelection.length === 0" class="filter-item" type="danger" @click="handleSelectedDelete()">{{$t('table.delete_selected')}}
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" @click="handleCreate" type="primary" icon="el-icon-edit">{{$t('table.add_bankcard')}}</el-button>

   </div>



    <el-table ref="multipleTable"  :key='tableKey' :data="list" v-loading="listLoading" element-loading-text="给我一点时间" border fit highlight-current-row
      style="width: 100%" @selection-change="handleSelectionChange">

      <el-table-column type="selection" width="55">
      </el-table-column>

      <el-table-column type="expand" >
        <template slot-scope="scope">
          <el-form label-position="left" inline class="demo-table-expand">
            <el-form-item :label="$t('table.bank')">
              <span>
                <el-tag >{{scope.row.fields.bank}}</el-tag>
              </span>
            </el-form-item>
            <el-form-item :label="$t('table.bankcard_type')">
              <span>
                <el-tag v-show=" scope.row.fields.bankcard_type === '信用卡'" type="success">{{scope.row.fields.bankcard_type }}</el-tag>
                <el-tag v-show=" scope.row.fields.bankcard_type === '借记卡'" type="warning">{{scope.row.fields.bankcard_type }}</el-tag>
              </span>
            </el-form-item>
            <el-form-item :label="$t('table.bankcard_num')">
              <span>{{scope.row.fields.bankcard_num}}</span>
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


      <el-table-column min-width="80px" align="center" :label="$t('table.bankcard_type')">
        <template slot-scope="scope">
              <span>
                <el-tag v-show=" scope.row.fields.bankcard_type === '信用卡' " type="success">{{scope.row.fields.bankcard_type }}</el-tag>
                <el-tag v-show=" scope.row.fields.bankcard_type === '借记卡' " type="warning">{{scope.row.fields.bankcard_type }}</el-tag>
              </span>
        </template>
      </el-table-column>

            <el-table-column min-width="150px" align="center" :label="$t('table.bank')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.bank}}</span>
        </template>
      </el-table-column>

      <el-table-column min-width="180px" align="center" :label="$t('table.bankcard_num')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.bankcard_num}}</span>
        </template>
      </el-table-column>


      <el-table-column min-width="200px" align="center" :label="$t('table.date')">
        <template slot-scope="scope">
          <span>{{scope.row.fields.update_datetime | parseTime('{y}-{m}-{d} {h}:{i}:{s}')}}</span>
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
       <el-dialog width="30%" title="添加银行" :visible.sync="dialogBankVisible" append-to-body>
           <el-form :rules="bankrules" ref="bankdataForm" :model="bank_temp" label-position="left" label-width="70px" style='width: 300px; margin-left:30px;'>
            <el-form-item :label="$t('table.bank')" prop="bank" width="50px">
              <el-input v-model="bank_temp.bank"  placeholder="请输入银行"></el-input>
            </el-form-item>
           </el-form>
            <div slot="footer" class="dialog-footer">
              <el-button @click="dialogBankVisible = false">{{$t('table.cancel')}}</el-button>
              <el-button  type="primary" @click="createBankData">{{$t('table.confirm')}}</el-button>
            </div>
      </el-dialog>

      <el-form :rules="rules" ref="dataForm" :model="temp" label-position="left" label-width="95px" style='width: 550px; margin-left:50px;'>

      <el-row>
          <el-form-item :label="$t('table.bankcard_type')" prop="bankcard_type">
            <el-select class="filter-item" v-model="temp.bankcard_type" placeholder="请选择银行卡类型">
              <el-option v-for="item in  bankcardTypeOptions" :key="item.key" :label="item.display_name" :value="item.key">
              </el-option>
            </el-select>
          </el-form-item>
      </el-row>

        <el-row>
          <el-col :span="12">

            <el-form-item :label="$t('table.bank')" prop="bank" width="70px">
              <el-select  filterable class="filter-item" v-model="temp.bank" placeholder="请选择银行" >
                <el-option v-for="item in  bankOptions" :key="item.key" :label="item.display_name" :value="item.key">
                </el-option>
              </el-select>
            </el-form-item>

          </el-col>

          <el-col :span="12">
            <span>
              <el-button type="primary" icon="el-icon-plus" @click="handleBankCreate"></el-button>
            </span>
          </el-col>
        </el-row>

        <el-row>
          <el-form-item :label="$t('table.bankcard_num')" prop="bankcard_num" width="70px">
            <el-input v-model="temp.bankcard_num"  placeholder="请输入银行卡号"></el-input>
          </el-form-item>
        </el-row>



        <el-row>
            <el-col :span="12">

              <el-form-item :label="$t('table.bill_day')" prop="bill_day" width="70px">
                <el-input-number style="width:150px;" v-model="temp.bill_day"  :min="1" :max="31" label="请输入账单日"></el-input-number>
              </el-form-item>


            </el-col>
           <el-col :span="12">
            <el-form-item :label="$t('table.repay_day')" prop="repay_day" width="70px">
              <el-input-number style="width:150px;"  v-model="temp.repay_day"  :min="1" :max="31" label="请输入还款日"></el-input-number>
            </el-form-item>
           </el-col>
        </el-row>

        <el-row>

        </el-row>

        <el-row>
          <el-col :span="12">
            <el-form-item :label="$t('table.valid_until')" prop="valid_until" width="70px">
              <el-date-picker style="width:150px;" v-model="temp.valid_until" type="date" placeholder="请输入有效期"></el-date-picker>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item :label="$t('table.annual_fee')" prop="annual_fee" width="70px">
              <el-input-number style="width:150px;" v-model="temp.annual_fee" placeholder="请输入年费" :precision="2" :step="0.1" :max="1000"></el-input-number>
            </el-form-item>
          </el-col>
        </el-row>

        <el-row>
          <el-form-item :label="$t('table.is_free')" prop="is_free" width="70px">
            <!--<el-input v-model="temp.is_free"  placeholder="是否可免年费"></el-input>-->
            <el-switch v-model="temp.is_free" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
          </el-form-item>
        </el-row>

        <el-row>
          <el-form-item v-show="temp.free_condition" :label="$t('table.free_condition')" prop="free_condition" width="70px">
            <el-input type="textarea" :autosize="{ minRows: 2, maxRows: 4}" placeholder="免年费条件（选填）" v-model="temp.free_condition">
            </el-input>
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
import { getItem, addItem, deleteItems, editItem, getList, getBankCardType, getBankList, addBank } from '@/api/bankcard'
import waves from '@/directive/waves' // 水波纹指令
import { parseTime } from '@/utils'
import { Message } from 'element-ui'

export default {
  name: 'bankCard',
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
        bankcard_type: '',
        bank: '',
        bankcard_num: ''
      },
      bankcardTypeOptions: null,
      formSubmoduleOptions: null,
      sortOptions: [{ label: '正序', key: '+id' }, { label: '倒序', key: '-id' }],
      temp: {
        pk: '',
        bankcard_type: '',
        bank: '',
        bankcard_num: '',
        bill_day: '',
        repay_day: '',
        valid_until: '',
        annual_fee: '',
        is_free: true,
        free_condition: '',
        remark: ''
      },
      bank_temp: {
        bank: ''
      },
      dialogFormVisible: false,
      dialogBankVisible: false,
      dialogStatus: '',
      rules: {
        bankcard_type: [{ required: true, message: '请选择银行卡类型', trigger: 'change' }],
        bank: [{ required: true, message: '请选择发卡银行', trigger: 'change' }],
        bankcard_num: [{ required: true, message: '请输入银行卡号', trigger: 'blur' }],
        bill_day: [{ required: false, message: '请输入账单日', trigger: 'blur' }],
        repay_day: [{ required: false, message: '请输入还款日', trigger: 'blur' }],
        valid_until: [{ required: false, message: '请输入有效期', trigger: 'blur' }],
        annual_fee: [{ required: false, message: '请输入年费', trigger: 'blur' }],
        is_free: [{ required: false, message: '是否免费', trigger: 'blur' }],
        free_condition: [{ required: false, message: '请输入免费条件', trigger: 'blur' }],
        remark: [{ required: false, message: '请输入备注', trigger: 'blur' }]
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
    this.getBankCardTypeFunc()
    this.getBankListFunc()
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
    resetBankTemp() {
      this.bank_temp = {
        bank: ''
      }
    },
    handleBankCreate() {
      this.resetBankTemp()
      this.dialogBankVisible = true
      this.$nextTick(() => {
        this.$refs['bankdataForm'].clearValidate()
      })
    },
    createBankData() {
      this.$refs['bankdataForm'].validate((valid) => {
        if (valid) {
          addBank(this.bank_temp).then((rsp) => {
            this.getBankListFunc()
            this.dialogBankVisible = false
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
    getBankCardTypeFunc() {
      getBankCardType({}).then(response => {
        this.bankcardTypeOptions = response.data.items.map((array) => {
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
    getBankListFunc() {
      getBankList({}).then(response => {
        this.bankOptions = response.data.items.map((array) => {
          var temp = {}
          temp['key'] = array.pk
          temp['display_name'] = array.fields.name
          return temp
        }, {})
        console.log(this.bankOptions)
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
        bankcard_type: '',
        bank: '',
        bankcard_num: '',
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
