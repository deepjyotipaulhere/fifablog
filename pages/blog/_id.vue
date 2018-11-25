<template>
    <div>
        <section class="s-content s-content--narrow s-content--no-padding-bottom">

            <div class="row">
                <div class="s-content__header col-full">
                    <h1 class="s-content__header-title">
                        {{data.title}}
                    </h1>
                    <ul class="s-content__header-meta">
                        <li class="date">December 16, 2017</li>
                        <li class="cat">
                            {{data.name}}
                        </li>
                    </ul>
                </div>
                <div class="col-full s-content__main">
                    
                           <pre style="padding:0;font-family:inherit;background-color:transparent">{{data.content}}</pre>

                </div> <!-- end s-content__main -->

            </div> <!-- end row -->

        </section> <!-- s-content -->
    </div>
</template>

<script>
export default {
    data(){
        return {
            data:{}
        }
    },
    created(){
        this.load()
    },
    methods:{
        load(){
            this.$axios.get(process.env.baseURL+"/getblogs/"+this.$route.params.id).then(response=>{
                this.data=response.data
            })
        },
    }
}
</script>

<style>

</style>
