<template>
  <div>
    <div class="header">
      <div class="bx--grid">
        <div class="bx--row">
          <div class="bx--col-xs-12 " style="padding:2rem 0">
            <h5 style="color:#5a6872;font-weight:400;margin:0">Welcome</h5>
            <h1 class="page-title" style="margin:0">Blog</h1>
          </div>
        </div>
      </div>
      
    </div>
    <br>
    <div class="bx--grid">
      <div class="bx--row">
        <div class="bx--col-xs-3" v-for="(x,i) in a" :key="i">
          <nuxt-link :to="''">
            <div class="bx--tile">
              <h4 style="text-decoration:none;color:black">Blog {{x}}</h4>
              <p style="color:#aaa;font-weight:400">A new Paragraph</p>
            </div>
            <br>
          </nuxt-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Logo from '~/components/Logo.vue'

export default {
  components: {
    Logo
  },
  data(){
    return {
      a:[1,2,3,4,5,6,7,8,9,10]
    }
  }
}
</script>

<style>
body{
  background-color: #fff
}
.header{
  background-color: #f4f7fb;
  border-bottom: 1px solid #3057d5;
}
.page-title{
  font-size: 3.375rem
}
</style>
