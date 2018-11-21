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
          <nuxt-link :to="'/blog/'+i" style="text-decoration:none;">
            <div class="bx--tile">
              <h4 style="color:#30588c">Blog {{x}}</h4>
              <p style="color:#aaa;font-weight:400">A new Paragraph</p>
            </div>
            <br>
          </nuxt-link>
        </div>
        
      </div>
      <nuxt-link class="bx--btn bx--btn--primary" :to="'/blog/create'"
          type="button">
          Share your experience
          <svg class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
            <path d="M7 7H4v2h3v3h2V9h3V7H9V4H7v3zm1 9A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" fill-rule="evenodd" />
          </svg>
        </nuxt-link>
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
