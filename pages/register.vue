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
        <div class="bx--grid">
            <div class="bx--form-item">
                <input id="text-input-3" type="text" class="bx--text-input" placeholder="Enter your full name" v-model="register.name">
                <label for="text-input-3" class="bx--label">Full Name</label>
            </div>
            <br>
            <div class="bx--form-item">
                <input id="text-input-3" type="text" class="bx--text-input" placeholder="Enter your email" v-model="register.email">
                <label for="text-input-3" class="bx--label">Email</label>
            </div>
            <br>
            <div class="bx--row">
                <div class="bx--col-sm-12 bx--col-lg-3 bx--col-xxl-3">
                    <div class="bx--form-item">
                        <div class="bx--select">
                            <label for="select-id" class="bx--label">Nationality</label>
                            <select  id="select-id" class="bx--select-input" v-model="register.country">
                                <option class="bx--select-option" value=""  disabled selected hidden>Choose an option</option>
                                <option class="bx--select-option" :value="x.alpha2Code" v-for="(x,i) in countries" :key="i" >{{x.name}} ({{"+"+x.callingCodes[0]}})</option>
                            </select>
                            <svg class="bx--select__arrow" width="10" height="5" viewBox="0 0 10 5">
                                <path d="M0 0l5 4.998L10 0z" fill-rule="evenodd" />
                            </svg>
                        </div>
                    </div>

                </div>
                <div class="bx--col-sm-12 bx--col-lg-9 bx--col-xxl-9">
                    <div class="bx--form-item">
                        <input id="text-input-3" type="text" class="bx--text-input" placeholder="Enter your mobile" v-model="register.mobile">
                        <label for="text-input-3" class="bx--label">Mobile</label>
                    </div>
                </div>
            </div>
            
            <br>
            <div class="bx--form-item">
                <div data-date-picker data-date-picker-type="range" class="bx--date-picker bx--date-picker--range">
                    <div class="bx--date-picker-container">
                        <label for="date-picker-1" class="bx--label">Travelled to Russia</label>
                        <input type="text" id="date-picker-1" class="bx--date-picker__input" pattern="\d{1,2}/\d{1,2}/\d{4}" placeholder="mm/dd/yyyy"
                            data-date-picker-input-from v-model="register.fromdate" />
                    </div>
                    <div class="bx--date-picker-container">
                        <label for="date-picker-2" class="bx--label">Travel finished</label>
                        <input type="text" id="date-picker-2" class="bx--date-picker__input" pattern="\d{1,2}/\d{1,2}/\d{4}" placeholder="mm/dd/yyyy"
                            data-date-picker-input-to  v-model="register.todate"/>
                    </div>
                    <svg data-date-picker-icon class="bx--date-picker__icon" width="14" height="16" viewBox="0 0 14 16">
                    <path d="M0 5h14v1H0V5zm3-5h1v4H3V0zm7 0h1v4h-1V0zM0 2.5A1.5 1.5 0 0 1 1.5 1h11A1.5 1.5 0 0 1 14 2.5v12a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 0 14.5v-12zm1 0v12a.5.5 0 0 0 .5.5h11a.5.5 0 0 0 .5-.5v-12a.5.5 0 0 0-.5-.5h-11a.5.5 0 0 0-.5.5z"
                        fill-rule="nonzero" />
                    </svg>
                </div>
            </div>
            <br>
            <div class="bx--form-item">
                <input id="text-input-3" type="text" class="bx--text-input" placeholder="Optional placeholder text" v-model="register.password">
                <label for="text-input-3" class="bx--label">Choose a password</label>
            </div>
            <br>
            <div class="bx--form-item">
                <input id="text-input-3" type="text" class="bx--text-input" placeholder="Optional placeholder text" v-model="pwd">
                <label for="text-input-3" class="bx--label">Re-enter the password</label>
            </div>
            <br><br>
            <div class="bx--form-item">
                <button class="bx--btn bx--btn--primary" type="button" @click="register">Register</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return {
            countries:[],
            register:{
                name:'',
                email:'',
                mobile:'',
                country:'',
                fromdate:'',
                todate:'',
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
            
        }
    }
}
</script>

<style>

</style>
