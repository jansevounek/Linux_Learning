<template>
    <div class="flex flex-col top-12 relative h-[100%] w-screen">
        <div class="lectures-list">
            <div class="lectures-part-list">
                <h1 class="part-title">The Basics</h1>
                <div class="lecture-box">
                    <h1 class="lecture-title">The Basics</h1>
                    <button class="lecture-button">Learn</button>
                    <RouterLink to="/trycommands" class="lecture-button">
                        <button>Try</button>
                    </RouterLink>
                    <button class="lecture-button">Test</button>
                </div>
                <div class="lecture-box">
                    <h1 class="lecture-title">Cd, ls, mkdir</h1>
                    <button class="lecture-button">Learn</button>
                    <button class="lecture-button">Try</button>
                    <button class="lecture-button">Test</button>
                </div>
            </div>
            <div class="lectures-part-list">
                
            </div>
        </div>
    </div>
</template>

<script setup>
</script>
