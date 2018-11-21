<template>
  <div :class="className" :id="id" :style="{height:height,width:width}"></div>
</template>

<script>
import echarts from 'echarts'
import resize from './mixins/resize'
require('echarts/theme/macarons')

export default {
  mixins: [resize],
  props: {
    className: {
      type: String,
      default: 'chart'
    },
    id: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '500px'
    },
    chartData: {
      type: Object
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.initChart()
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  watch: {
    chartData: {
      deep: true,
      handler(val) {
        this.setOptions(val)
      }
    }
  },
  methods: {
    setOptions(
      {
        unexecutedData,
        passedData,
        failedData,
        blockData,
        NAData,
        timeData,
        executedData,
        show_type
      } = {}) {
      this.chart.setOption({
        backgroundColor: '#344b58',
        title: {
          text: '用例执行记录',
          x: '20',
          top: '20',
          textStyle: {
            color: '#fff',
            fontSize: '22'
          },
          subtextStyle: {
            color: '#90979c',
            fontSize: '16'
          }
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            textStyle: {
              color: '#fff'
            }
          }
        },
        grid: {
          borderWidth: 0,
          top: 110,
          bottom: 95,
          textStyle: {
            color: '#fff'
          }
        },
        legend: {
          x: '5%',
          top: '10%',
          textStyle: {
            color: '#90979c'
          },
          // data: ['通过', '阻塞', '失败', '未执行', '不适用', '执行数量']
          data: ['通过', '阻塞', '失败', '未执行', '不适用']
        },
        calculable: true,
        xAxis: [{
          type: 'category',
          axisLine: {
            lineStyle: {
              color: '#90979c'
            }
          },
          splitLine: {
            show: false
          },
          axisTick: {
            show: false
          },
          splitArea: {
            show: false
          },
          axisLabel: {
            interval: 0

          },
          data: timeData
        }],
        yAxis: [{
          type: 'value',
          splitLine: {
            show: false
          },
          axisLine: {
            lineStyle: {
              color: '#90979c'
            }
          },
          axisTick: {
            show: false
          },
          axisLabel: {
            interval: 0
          },
          splitArea: {
            show: false
          }
        }],
        dataZoom: [{
          show: true,
          height: 30,
          xAxisIndex: [
            0
          ],
          bottom: 30,
          start: 0,
          end: 100,
          handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
          handleSize: '110%',
          handleStyle: {
            color: '#d3dee5'

          },
          textStyle: {
            color: '#fff' },
          borderColor: '#90979c'

        }, {
          type: 'inside',
          show: true,
          height: 15,
          start: 1,
          end: 35
        }],
        series: [{
          name: '通过',
          type: show_type,
          stack: show_type === 'bar' ? 'total' : '',
          symbolSize: 10,
          symbol: 'circle',
          itemStyle: {
            normal: {
              color: 'rgba(34,139,34,1)', // 34 139 34
              barBorderRadius: 0,
              label: {
                show: true,
                position: 'top',
                formatter(p) {
                  return p.value > 0 ? p.value : ''
                }
              }
            }
          },
          data: passedData,
          smooth: true,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        }, {
          name: '阻塞',
          type: show_type,
          stack: show_type === 'bar' ? 'total' : '',
          symbolSize: 10,
          symbol: 'circle',
          itemStyle: {
            normal: {
              color: 'rgba(205,149,12,1)', //	205 149 12
              barBorderRadius: 0,
              label: {
                show: show_type === 'bar',
                position: 'top',
                formatter(p) {
                  return p.value > 0 ? p.value : ''
                }
              }
            }
          },
          data: blockData,
          smooth: true,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        }, {
          name: '失败',
          type: show_type,
          stack: show_type === 'bar' ? 'total' : '',
          symbolSize: 10,
          symbol: 'circle',
          itemStyle: {
            normal: {
              color: 'rgba(178,34,34,1)', // 178 34 34
              barBorderRadius: 0,
              label: {
                show: show_type === 'bar',
                position: 'top',
                formatter(p) {
                  return p.value > 0 ? p.value : ''
                }
              }
            }
          },
          data: failedData,
          smooth: true,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        }, {
          name: '未执行',
          type: show_type,
          stack: show_type === 'bar' ? 'total' : '',
          // barMaxWidth: 35,
          // barGap: '10%',
          symbolSize: 10,
          symbol: 'circle',
          itemStyle: {
            normal: {
              color: 'rgba(190,190,190,1)', //			248 248 255
              label: {
                show: show_type === 'bar',
                textStyle: {
                  color: '#fff'
                },
                position: 'insideTop',
                formatter(p) {
                  return p.value > 0 ? p.value : ''
                }
              }
            }
          },
          data: unexecutedData
        }, {
          name: '不适用',
          type: show_type,
          stack: show_type === 'bar' ? 'total' : '',
          symbolSize: 10,
          symbol: 'circle',
          itemStyle: {
            normal: {
              color: 'rgba(105,105,105,1)', //		105 105 105
              barBorderRadius: 0,
              label: {
                show: true,
                position: 'top',
                formatter(p) {
                  return p.value > 0 ? p.value : ''
                }
              }
            }
          },
          data: NAData,
          smooth: true,
          animationDuration: 2800,
          animationEasing: 'cubicInOut'
        }
        // }, {
        //   name: '执行数量',
        //   type: 'line',
        //   stack: 'total',
        //   symbolSize: 10,
        //   symbol: 'circle',
        //   itemStyle: {
        //     normal: {
        //       color: 'rgba(252,230,48,1)',
        //       barBorderRadius: 0,
        //       label: {
        //         show: true,
        //         position: 'top',
        //         formatter(p) {
        //           return p.value > 0 ? p.value : ''
        //         }
        //       }
        //     }
        //   },
        //   data: executedData,
        //   smooth: true,
        //   animationDuration: 2800,
        //   animationEasing: 'cubicInOut'
        // }
        ]
      })
    },
    initChart() {
      // this.chart = echarts.init(document.getElementById(this.id))
      this.chart = echarts.init(document.getElementById(this.id), 'macarons')
      this.setOptions(this.chartData)
    }
  }
}
</script>
