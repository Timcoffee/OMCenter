<template>
  <div class="charts">
    <h1>test</h1>
    <div id="chartObj" :style="{width:'600px',height:'400px'}"></div>
  </div>
</template>
<script>
  import echarts from 'echarts'
  export default{
    data (){
      return {
        msg:"123"
      }
    },
    mounted (){
      var myChart = echarts.init(document.getElementById('chartObj'));
      myChart.setOption({
        title: { text: 'ECharts 入门示例' },
        tooltip: {},
        xAxis: {
          data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }]
      });
    }

  }
</script>
<style>

</style>
