<template>

</template>

<script>
import PanelGroup from './components/PanelGroup'
import waves from '@/directive/waves' // 水波纹指令

// import LineChart from './components/LineChart'
// import RaddarChart from './components/RaddarChart'
// import PieChart from './components/PieChart'
// import BarChart from './components/BarChart'
// import TransactionTable from './components/TransactionTable'
// import TodoList from './components/TodoList'
// import BoxCard from './components/BoxCard'

import MixChart from '@/components/Charts/MixChart'

export default {
  name: 'dashboard-admin',
  directives: {
    waves
  },
  components: {
    // GithubCorner,
    // PanelGroup,
    // RaddarChart,
    // PieChart,
    // BarChart,
    // TransactionTable,
    // TodoList,
    // BoxCard,
    //
    // LineChart,
    PanelGroup,
    MixChart
  },
  created() {
  },
  data() {
    return {
      temp: ''
    }
  },
  methods: {}
}
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
.dashboard-editor-container {
  padding: 32px;
  background-color: rgb(240, 242, 245);
  .chart-wrapper {
    background: #fff;
    padding: 16px 16px 0;
    margin-bottom: 32px;
  }
}
</style>
