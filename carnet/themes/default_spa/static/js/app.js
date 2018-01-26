Vue.component('navbar-component', {
    template: `
        <nav class="navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <button type="button"
                            class="navbar-toggle collapsed"
                            data-toggle="collapse"
                            data-target="#navbar-collapse-id"
                            aria-expanded="false">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                    <router-link :to="{ name: 'Home' }" class="navbar-brand">
                        {{ global_config.title }}
                    </router-link>
                </div>

                <div class="collapse navbar-collapse" id="navbar-collapse-id">
                    <ul class="nav navbar-nav">
                        <li class="dropdown">
                            <a href="#"
                               class="dropdown-toggle"
                               data-toggle="dropdown"
                               role="button"
                               aria-haspopup="true"
                               aria-expanded="false">Posts <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">
                                <li v-if="global_config.all_posts.length > 0" v-for="p in global_config.all_posts">
                                    <router-link :to="{ name: 'Post', params: { id: p.path } }">{{ p.title }}</router-link>
                                </li>
                                <li v-if="global_config.all_posts.length == 0">
                                    <a href="#">No posts</a>
                                </li>
                            </ul>
                        </li>
                    </ul>
                    <form class="navbar-form navbar-right">
                        <div class="form-group">
                            <input type="text" class="form-control" placeholder="Search">
                        </div>
                    </form>
                </div>
            </div>
        </nav>
    `,

    data: function() {
        return {
            global_config: global_config
        }
    },
})

/* -------------------------------------------------------------------------- */

const Home = {
    template: `
        <div id="home">
            <div class="page-header">
                <h1>{{ global_config.title }} <small>{{ global_config.subtitle }}</small></h1>
            </div>

            <div v-if="global_config.all_posts.length > 0"
                 v-for="p in global_config.all_posts">
                <img v-if="p.header_image"
                     class="img-responsive"
                     alt="Post header image"
                     :src="p.header_image" />

                <h1><router-link :to="{ name: 'Post', params: { id: p.path } }">{{ p.title }}</router-link></h1>

                <p class="text-muted">
                    Published by {{ p.author }} on {{ p.published }}
                    <br/>
                    Categories: <router-link v-for="c in p.categories" :key="c" :to="{ name: 'Home' }">{{ c }} </router-link>
                    <br/>
                    Tags: <router-link v-for="t in p.tags" :key="t" :to="{ name: 'Home' }">{{ t }} </router-link>
                </p>

                <!-- HTML interpolation used on provided content already escaped -->
                <span v-html="p.html"></span>
                <hr class="intro-divider">
            </div>
            <div v-if="global_config.all_posts.length == 0">
                <h2>No posts</h2>
                <hr class="intro-divider">
            </div>
    </div>
    `,

    data: function() {
        return {
            global_config: global_config
        }
    },
}

const Post = {
    template: `
        <div id="post">
            <div class="row">
                <div class="col-md-12">
                    <h1>{{ post.title }}</h1>
                        <p class="text-muted">
                            Published by {{ post.author }} on {{ post.published }}
                            <br/>
                            Categories: <router-link v-for="c in post.categories" :key="c" :to="{ name: 'Home' }">{{ c }} </router-link>
                            <br/>
                            Tags: <router-link v-for="t in post.tags" :key="t" :to="{ name: 'Home' }">{{ t }} </router-link>
                        </p>

                        <hr class="intro-divider">

                        <!-- HTML interpolation used on provided content already escaped -->
                        <span v-html="post.html"></span>
                </div>
            </div>
        </div>
    `,

    props: ['post'],
}

/* -------------------------------------------------------------------------- */

const App = {
    template: `
        <div id="app">
            <navbar-component></navbar-component>

            <div class="container">
                <transition name="router-fade" mode="out-in">
                    <router-view></router-view>
                </transition>
            </div>
        </div>
    `
}

/* -------------------------------------------------------------------------- */

const routes = [
    { path: '/', component: Home, name: 'Home' },
    { path: '/posts/:id', component: Post, name: 'Post', props: (route) => ({ post: _all_posts[route.params.id] }) }
]

const router = new VueRouter({
    routes: routes
})

/* -------------------------------------------------------------------------- */

var app = new Vue({
    el: '#app',
    router,
    render: h => h(App)
})
