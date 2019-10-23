<template>
  <div class="home">
   <div class="slider">
     <div class="slider-left">
       <div>知网大数据</div>
       <div>本系统采用Django+Celery实现在线知网爬虫，并针对爬取的数据进行实时的数据分析</div>
       <div><button>欢迎使用</button></div>
     </div>
     <div class="slider-gight"></div>
   </div>
   <div class="service"></div>
   <div class="data"></div>
   <div class="feature"></div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: "这是首页"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.slider{
  /* background:  url("../assets/img/sliderBg.png") ; */
  background: url(../assets/img/sliderBg.png) 0 100% repeat-x ;
}
</style>
