<template>
    <div>
        <section class="s-content s-content--narrow" style="padding-top:0">
            
            <div class="row">
                <br>
                <h1 class="text-center" style="margin:0">Write your story</h1>
                <div class="col-full s-content__main">
                    <div class="row">
                        <div class="col-twelve tab-full">

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
            blogs:[]
        }
    },
    methods:{
        getmyblogs(){
            this.$axios.get(process.env.baseURL+"/getmyblogs",
            {
                headers:{
                    'x-access-token':this.$cookies.get('auth')
                }
            }).then(response=>{
                this.blogs=response.data
            })
        }
    }
}
</script>

<style>

</style>
