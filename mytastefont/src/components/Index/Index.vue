<template>
    <el-container>
        <el-header>
            <Header></Header>
        </el-header>
        <el-main style="padding: 0">
            <carousel></carousel>
            <local-travel-module></local-travel-module>
            <province-travel-module></province-travel-module>
            <domestic-travel-module></domestic-travel-module>
        </el-main>
        <el-footer>
            <Footer></Footer>
        </el-footer>
    </el-container>
</template>

<script>
    import Header from '@/components/Common/Header'
    import Footer from '@/components/Common/Footer'
    import Carousel from '@/components/Index/Carousel'
    import LocalTravelModule from '@/components/Index/LocalTravelModule'
    import DomesticTravelModule from '@/components/Index/DomesticTravelModule'
    import ProvinceTravelModule from '@/components/Index/ProvinceTravelModule'

    export default {
        name: "Index",
        data() {
            return {}
        },
        components: {
            Header,
            Footer,
            Carousel,
            LocalTravelModule,
            ProvinceTravelModule,
            DomesticTravelModule,

        }
    }
</script>

<style scoped>


</style>