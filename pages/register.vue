<template>
    <div>
        <section class="s-content s-content--narrow" style="padding-top:0">

            <div class="row">
                <div class="col-full s-content__main">
                    <div class="row">
                        <div class="col-six tab-full">
                            <h3>Sign In</h3>

                            <form name="cForm" id="cForm" method="post" action="">
                                <fieldset>
                                    <div class="form-field">
                                        <input name="cEmail" type="text" id="cEmail" class="full-width" placeholder="Your Email" v-model="xlogin.email">
                                    </div>

                                    <div class="form-field">                                        
                                        <input name="cWebsite" type="password" id="cWebsite" class="full-width" placeholder="Enter Password" v-model="xlogin.password">
                                    </div>

                                    <button type="submit" class="submit btn btn--primary full-width" @click.prevent="signin">Sign In</button>

                                </fieldset>
                            </form> 

                        </div>

                        <div class="col-six tab-full">
                            <h3>Register</h3>

                            <form name="cForm" id="cForm" method="post" action="">
                                <fieldset>

                                    <div class="form-field">
                                        <input name="cName" type="text" id="cName" class="full-width" placeholder="Your Full Name" v-model="xregister.name">
                                    </div>
                                    <div class="form-field">
                                        <input name="cEmail" type="text" id="cEmail" class="full-width" placeholder="Your Email" v-model="xregister.email">
                                    </div>
                                    <div>
                                        <label for="sampleRecipientInput">Nationality</label>
                                        <div class="cl-custom-select">
                                            <select class="full-width" id="sampleRecipientInput" v-model="xregister.country">
                                                <option v-for="(x,i) in countries" :key="i" :value="x.alpha2Code">{{x.name}}</option>
                                            </select>
                                        </div>
                                    </div>
                                    <div class="form-field">
                                        <input name="cMobile" type="text" id="cMobile" class="full-width" placeholder="Your Mobile Number" value="" v-model="xregister.mobile">
                                    </div>
                                    <div class="form-field">
                                        <input name="cWebsite" type="password" id="cWebsite" class="full-width" placeholder="Enter Password" v-model="xregister.password">
                                    </div>
                                    <div class="form-field">
                                        <input name="cpwd" type="password" id="cpwd" class="full-width" placeholder="Repeat Password"  value="">
                                    </div>


                                    <button type="submit" class="submit btn btn--primary full-width" @click.prevent="register">Register</button>

                                </fieldset>
                            </form> 

                        </div>
                    </div> <!-- end row -->
                    <!-- end form -->
                </div> <!-- end s-content__main -->

            </div> <!-- end row -->

        </section> <!-- s-content -->
    </div>
</template>

<script>
export default {
    data(){
        return {
            countries:[],
            xregister:{
                name:'',
                email:'',
                mobile:'',
                country:'',
                password:''
            },
            xlogin:{
                email:'',
                password:''
            },
            pwd:''
        }
    },
    created(){
        this.loadcountries()
    },
    methods:{
        loadcountries(){
            this.$axios.get('https://restcountries.eu/rest/v2/all').then(response=>{
                this.countries=response.data
            })
        },
        register()
        {
            this.$axios.post(process.env.baseURL+"/insertuser",this.xregister).then(response=>{
                alert(response.data)
            })
        },
        signin(){
            this.$axios.post(process.env.baseURL+"/signin",this.xlogin).then(response=>{
                this.$cookies.set("auth",response.data.auth)
                this.$cookies.set("name",response.data.name)
                location.href="/"
            })
        }
    }
}
</script>

<style>

</style>
