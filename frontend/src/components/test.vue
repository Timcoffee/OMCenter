<template>
  <div class="charts">
    <h1>test22222</h1>
    <div id="chartObj" :style="{width:'800px',height:'600px'}"></div>
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
        title: { text: 'ECharts aaaaaa' },
        tooltip: {},
        xAxis: {
          data: ["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"]
        },
        yAxis: {},
        series: [{
          name: '销量',
          type: 'bar',
          data: [15, 240, 236, 150, 110, 240]
        }]
      });
    }

  }
</script>
<style>

</style>
