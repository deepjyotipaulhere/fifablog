<template>
    <div>
        <div class="header">
            <div class="bx--grid">
                <div class="bx--row">
                    <div class="bx--col-xs-12 " style="padding:2rem 0">
                        <h1 class="page-title" style="margin:0">Blog {{$route.params.id}}</h1>
                        <h5 style="color:#5a6872;font-weight:400;margin:0">by </h5>
                        <h5>
                            <nuxt-link :to="'/'" style="float:right">&lt; Back to home</nuxt-link>
                        </h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {

}
</script>

<style>

</style>
