<template>
  <NavBar v-if="$route.name != 'homepage'" />
  <router-view />
</template>

<style>
body,
html {
  background-color: #000000;
}
</style>

<script setup>
import { useRoute } from 'vue-router'
import NavBar from './components/navbar/NavBar.vue'
import { onMounted, ref } from 'vue';

const route = useRoute()

const routeName = ref('')

onMounted(() => {
  routeName.value = route.path
})
</script>