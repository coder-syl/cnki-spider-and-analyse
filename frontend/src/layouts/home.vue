<template>
  <div class="home">
    <div class="slider">
      <div class="slider-container">
        <div class="slider-left">
          <div class="slider-left-title">
            <h1>知网大数据</h1>
          </div>
          <div class="slider-left-dec">
            <p>本系统采用Django+Celery实现在线知网爬虫，并针对爬取的数据进行实时的数据分析</p>
          </div>
          <div class="slider-left-welcome">
            <button>欢迎使用</button>
          </div>
        </div>
        <div class="slider-right">
          <img class src="../assets/img/analyse.png" alt />
        </div>
      </div>
    </div>
    <div class="service">
      <div class="service-container">
        <div class="service-content">
          <div class="service-content-img"><img src="" alt=""></div>
          <div class="service-content-title"><h2>在线智能爬虫</h2></div>
          <div class="service-content-dec"><p>提供关键词，实时开启知网爬虫模块，自动化采集，摒弃人工采集.</p></div>
        </div>
        <div class="service-content">
          <div class="service-content-img"><img src="" alt=""></div>
          <div class="service-content-title"><h2>在线智能爬虫</h2></div>
          <div class="service-content-dec"><p>提供关键词，实时开启知网爬虫模块，自动化采集，摒弃人工采集.</p></div>
        </div>
        <div class="service-content">
          <div class="service-content-img"><img src="" alt=""></div>
          <div class="service-content-title"><h2>在线智能爬虫</h2></div>
          <div class="service-content-dec"><p>提供关键词，实时开启知网爬虫模块，自动化采集，摒弃人工采集.</p></div>
        </div>
      </div>

      <div></div>
      <div></div>
    </div>
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
.slider {
  background: url(../assets/img/sliderBg.png) 0 100% repeat-x;
}
.slider-container,
.service-container {
  /* background:  url("../assets/img/sliderBg.png") ; */
  width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content:center;
  margin: auto;
  /* height: 450px; */
}
.slider-left {
  width: 40%;
  display: flex;
  flex-direction: column;
  justify-content:  center;
}
.slider-left-title h1 {
  font-size: 36px;
  font-weight: 300;
}
.slider-left-dec p {
  font-size: 16px;
  font-weight: 300;
}
.slider-left-welcome button {
  padding: 12px 25px;
  font-size: 18px;
  font-weight: 300;
  border: 1px solid #0099ae;
  border-radius: 5px;
}
.slider-right {
  display: flex;
  flex-direction: column-reverse;
  /* justify-container: center; */
  width: 60%;
}
.slider-right img {
  margin: 0px;
  animation: bounceDown  ease-in-out 200ms both；
}
@keyframes bounceDown {
  0% {
    opacity: 0;
    -webkit-transform: translateY(-2000px);
    -ms-transform: translateY(-2000px);
    transform: translateY(-2000px);
  }
  60% {
    opacity: 1;
    -webkit-transform: translateY(30px);
    -ms-transform: translateY(30px);
    transform: translateY(30px);
  }
  80% {
    -webkit-transform: translateY(-10px);
    -ms-transform: translateY(-10px);
    transform: translateY(-10px);
  }
  100% {
    -webkit-transform: translateY(0);
    -ms-transform: translateY(0);
    transform: translateY(0);
  }
}
.service-content{
 /* width: 30%; */
  display: flex;
  flex-direction: column;
  justify-content:  center;
}

</style>
