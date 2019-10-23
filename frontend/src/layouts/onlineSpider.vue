<template>
  <div class="onlineSpider">
    <div class="start">
        <input/><button @click="startSpider">启动爬虫</button>
    </div>
    <div class="steps">

    </div>
  </div>
</template>

<script>
export default {
  name: "onlineSpider",
  data() {
    return {
      msg: "在线爬虫"
    };
  },
  methods:{
    startSpider(){
      console.log("start spider")
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.start{
  display: flex;
  flex-direction: row;
  justify-content: center;
  flex-wrap:wrap;
  padding-top:20px;
}
input{
  width:60%;
  border: 1px solid #dcdfe6;
  border-radius:4px;
    margin-right:20px;

}
button{
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    color: #fff;
    background-color: #409eff;
    border: 1px solid #409eff;
    -webkit-appearance: none;
    text-align: center;
    box-sizing: border-box;
    outline: none;
    margin: 0;
    transition: .1s;
    font-weight: 500;
    -moz-user-select: none;
    -webkit-user-select: none;
    -ms-user-select: none;
    padding: .8em 1.5em;
    font-size: 1em;
    border-radius: 4px;
}

</style>
