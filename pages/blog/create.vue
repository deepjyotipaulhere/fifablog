<template>
    <div>
        <section class="s-content s-content--narrow" style="padding-top:0">
            
            <div class="row">
                <br>
                <h1 class="text-center" style="margin:0">Write your story</h1>
                <div class="col-full s-content__main">
                    <div class="row">
                        <div class="col-twelve tab-full">

                            <form name="cForm" id="cForm" method="post" action="">
                                <fieldset>
                                    <div class="form-field">
                                        <input name="cEmail" type="text" id="cEmail" class="full-width" placeholder="Give an appropriate title" v-model="post.title">
                                    </div>

                                    <div class="form-field">  
                                        <label for="content">Write you story here</label>                                      
                                        <textarea name="content" class="full-width" placeholder="Write your story here" v-model="post.content"></textarea>
                                    </div>

                                    <!-- <div class="form-field">
                                        <label for="content">Post photo - Image will be inserted at current cursor position</label> 
                                        <input type="file" name="" id="" accept="image/*" ref="file" @change="uploadphoto">
                                    </div> -->


                                    <button type="submit" class="submit btn full-width" @click.prevent="save">Save</button>
                                    <button type="submit" class="submit btn btn--primary full-width" @click.prevent="submit">Final Submit</button>

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
            post:{
                title:'',
                content:'',
                status:0,
                photos:[]
            }
        }
    },
    methods:{
        save(){
            this.$axios.post(process.env.baseURL+"/insertpost",this.post,{
                headers:{
                    'x-access-token':this.$cookies.get('auth')
                }
            }).then(response=>{
                alert(response.data)
            })
        },
        submit(){
            this.status=1
            this.save()
        },
        uploadphoto(){
            var reader = new FileReader();
            reader.readAsDataURL(this.$refs.file.files[0])
            reader.onload=()=>{
                this.post.photos.push({'name':this.$refs.file.files[0]['name'], 'file':reader.result})
                this.post.content=this.post.content+"\n:img:"+this.$refs.file.files[0]['name']+"::img:\n"
            }
        }
    }

}
</script>

<style>

</style>
