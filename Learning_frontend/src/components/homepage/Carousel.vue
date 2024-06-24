<template>
    <div class="relative mt-80">
        <div class="first-carousel-part carousel-part top-20">
            <h1 class="text-[50px] main-title">{{ $t("homepage.createaccount.header") }}</h1>
            <p class="mt-8 mx-4 sm:mx-10 md:mx-20 lg:mx-36 text-font">{{ $t("homepage.createaccount.text") }}</p>
            <RouterLink to="/signup">
                <button class="mt-10 weird-button">
                    {{ $t("homepage.createaccount.button") }}
                </button>
            </RouterLink>
        </div>
        <div class="second-carousel-part carousel-part top-40">
            <h1 class="text-[50px] main-title" id="download">{{ $t("homepage.download.header") }}</h1>
            <p class="mt-8 mx-4 sm:mx-10 md:mx-20 lg:mx-36 text-font">{{ $t("homepage.download.text") }}</p>
            <a href="/login" target="_blank" class="group download-button-a mt-10">
                <span class="z-40">{{ $t("homepage.download.button1") }}</span>
                <svg class="z-40 ml-2 -mr-1 w-3 h-3 transition-all duration-300 group-hover:translate-x-1"
                    fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                        clip-rule="evenodd"></path>
                </svg>
                <div class="download-button-div">
                </div>
            </a>
            <br>
            <a href="/login" target="_blank" class="group download-button-a mt-10">
                <span class="z-40">{{ $t("homepage.download.button2") }}</span>
                <svg class="z-40 ml-2 -mr-1 w-3 h-3 transition-all duration-300 group-hover:translate-x-1"
                    fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                    <path fill-rule="evenodd"
                        d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
                        clip-rule="evenodd"></path>
                </svg>
                <div class="download-button-div">
                </div>
            </a>
        </div>
        <div class="first-carousel-part carousel-part top-60">
            <h1 class="text-[50px] main-title">{{ $t("homepage.socials.header") }}</h1>
            <p class="mt-8 mx-4 sm:mx-10 md:mx-20 lg:mx-36 text-font">{{ $t("homepage.socials.text") }}</p>
            <div class="mt-10 w-[100%] flex flex-row justify-center">
                <button class="facebook-button mx-auto">
                    <svg class="w-5 h-5 fill-current" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path
                            d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z" />
                    </svg>
                </button>
                <button class="twitter-button mx-auto">
                    <svg class="w-5 h-5 fill-current" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path
                            d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" />
                    </svg>
                </button>
                <button class="github-button mx-auto">
                    <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
                        aria-hidden="true" role="img" class="w-5" preserveAspectRatio="xMidYMid meet"
                        viewBox="0 0 24 24">
                        <g fill="none">
                            <path fill-rule="evenodd" clip-rule="evenodd"
                                d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385c.6.105.825-.255.825-.57c0-.285-.015-1.23-.015-2.235c-3.015.555-3.795-.735-4.035-1.41c-.135-.345-.72-1.41-1.23-1.695c-.42-.225-1.02-.78-.015-.795c.945-.015 1.62.87 1.845 1.23c1.08 1.815 2.805 1.305 3.495.99c.105-.78.42-1.305.765-1.605c-2.67-.3-5.46-1.335-5.46-5.925c0-1.305.465-2.385 1.23-3.225c-.12-.3-.54-1.53.12-3.18c0 0 1.005-.315 3.3 1.23c.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23c.66 1.65.24 2.88.12 3.18c.765.84 1.23 1.905 1.23 3.225c0 4.605-2.805 5.625-5.475 5.925c.435.375.81 1.095.81 2.22c0 1.605-.015 2.895-.015 3.3c0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"
                                fill="currentColor" />
                        </g>
                    </svg>
                </button>
            </div>
        </div>
        <div class="carousel-part bg-secondary text-white top-80 rounded-none">
            <h1 class="text-[50px] main-title" id="aboutus">{{ $t("homepage.aboutus.header") }}</h1>
            <p>{{ $t("homepage.aboutus.text") }}</p>
            <p class="mt-[50rem]">
                @All rights reserved
            </p>
        </div>
    </div>
</template>