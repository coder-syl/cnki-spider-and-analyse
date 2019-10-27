<template>
  <div class="footer">
    <div class="footer-container">
      <!-- <div class="footer-content">
        <img src="../assets/img/under.png" alt />
      </div>-->
      <!-- < class="footer-content"> -->
          <div class="footer-content-phone">
            <h2>联系方式</h2>
            <p>
              Email
              <a href="mailto:someone@example.com">2522011411@qq.com</a>
            </p>
            <p>Phone: 18796323596</p>
            <p>QQ: 2522011411</p>
            <h2 class="address">地址</h2>
            <p>江苏省徐州市泉山区江苏师范大学</p>
          </div>
          <div class="footer-content-online">
            <h2>在线联系</h2>
            <form id="main-contact-form" name="contact-form" method="get">
              <div class="form-group">
                <input
                  type="text"
                  name="name"
                  class="form-control"
                  required="required"
                  placeholder="您的姓名"
                />
              </div>
              <div class="form-group">
                <input
                  type="email"
                  name="email"
                  class="form-control"
                  required="required"
                  placeholder="您的邮箱"
                />
              </div>
              <div class="form-group">
                <textarea
                  name="message"
                  id="message"
                  required
                  class="form-control"
                  rows="8"
                  placeholder="您的建议或者疑惑"
                ></textarea>
              </div>
              <div class="form-group">
                <input
                  type="submit"
                  name="submit"
                  class="btn btn-submit"
                  value="Submit"
                  id="submit"
                />
              </div>
            </form>
          </div>

      <!-- </div> -->

    </div>
  </div>
   <!-- <div class="footer-content">
        <div class="footer-content-copyright">
          <p>&copy; 知网大数据 2019. All Rights Reserved.</p>
          <p>
            Designed by
            <a target="_blank" href="http://sylblog.xin">尚衍亮</a>
          </p>
        </div>
      </div> -->
</template>

<script>
export default {
  name: "cnki-footer",
  data() {
    return {
      msg: "Welcome to Your Vue.js App"
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.footer {
  /* background: url(../assets/img/footer.png) 0 100% repeat-x; */
}
.footer-container {
 width: 80%;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
  margin: auto;
  /* height: 690px; */
}
.footer-content-phone{
 flex: 1;
  /* display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center; */

}
.footer-content-online{
   flex: 1;
  /* display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center; */
}
/* .footer-content {
   flex: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: center;
    margin: auto;

} */
/* .footer-content img { */
  /* display: block; */
  /* width: 100%; */
  /* height: auto; */
/* } */
/* .footer-content-contact { */
  /* display: flex;
  flex: auto;
  flex-direction: row;
  justify-content: center; */
  /* align-items: center; */
/* }
.footer-content-phone {
  flex: 1;
}
.footer-content-online {
  flex: 1;
}
.footer-content-phone h2 {
  margin-top: 0;
  margin-bottom: 20px;
  font-size: 24px;
  color: #686868;
  font-weight: 300;
} */
/* .footer-content-phone p {
  font-weight: 300;
  font-size: 18px;
  line-height: 22px;
  color: rgb(43, 43, 43);
}
.footer-content-phone p a {
  text-decoration: none;
  color: #c03035;
  font-style: normal;
}
.footer-content-phone .address {
  padding-top: 20px;
}
.footer-content-copyright {
  text-align: center;
  margin-top: 70px;
  color: #fff;
  font-size: 16px;
  padding-bottom: 15px;
}
.footer-content-copyright a {
  color: #3e848a;
} */
</style>
