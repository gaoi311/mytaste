<template>
    <div>
        <Header></Header>
        <carousel></carousel>
        <local-travel-module></local-travel-module>
        <province-travel-module></province-travel-module>
        <domestic-travel-module></domestic-travel-module>
        <Footer></Footer>
    </div>
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