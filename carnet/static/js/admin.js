Vue.component('flashed-messages', {
    template: `
        <div id="flashed-messages" v-if="categorized.length > 0">
            <div v-for="m in categorized"
                 class="alert alert-dismissible"
                 :class="{ 'alert-info': m.category === 'info', 'alert-warning': m.category === 'warning', 'alert-danger': m.category === 'danger' }"
                 role="alert">
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                {{ m.message }}
            </div>
        </div>
    `,

    props: ['messages'],

    computed: {
        categorized: function() {
            var transform = {
                'critical': 'danger',
                'error': 'danger',
                'info': 'info',
                'warning': 'warning',
                'debug': 'info',
                'notset': 'info',
                'message': 'info',
            }

            var msg = this.messages
            for (var i = 0; i < msg.length; ++i) {
                var cat = msg[i].category
                if (cat in transform) {
                    msg[i].category = transform[cat]
                } else {
                    msg[i].category = 'info'
                }
            }
            return msg
        }
    }
})

/* -------------------------------------------------------------------------- */

const Dashboard = {
    template: `
        <div id="dashboard">
            <div class="row">
                <div class="col-md-12">
                <h2>Dashboard</h2>
                </div>
            </div>
        </div>
    `
}

const Posts = {
    template: `
        <div id="posts">
            <div class="row">
                <div class="col-md-12">
                <h2>Posts</h2>
                </div>
            </div>
        </div>
    `
}

const Pages = {
    template: `
        <div id="pages">
            <div class="row">
                <div class="col-md-12">
                <h2>Pages</h2>
                </div>
            </div>
        </div>
    `
}

/* -------------------------------------------------------------------------- */

const PageNotFound = {
    template: `
        <div id="page-not-found">
            <div class="page-header">
                <h1>Page not found</h1>
            </div>

            <p>Sorry, but the page you requested does not exist.</p>
        </div>
    `
}

/* -------------------------------------------------------------------------- */

const App = {
    template: `
        <div id="app">
            <div class="container">
                <div class="row">
                    <div class="col-md-12">
                        <flashed-messages :messages="flashedMessages"></flashed-messages>

                        <div class="page-header">
                            <h1>Carnet Admin</h1>
                        </div>

                        <ul class="nav nav-pills">
                            <li role="presentation" :class="{ active: currentRoute === 'Dashboard' }">
                                <router-link :to="{ name: 'Dashboard' }">Dashboard</router-link>
                            </li>
                            <li role="presentation" :class="{ active: currentRoute === 'Posts' }">
                                <router-link :to="{ name: 'Posts' }">Posts</router-link>
                            </li>
                            <li role="presentation" :class="{ active: currentRoute === 'Pages' }">
                                <router-link :to="{ name: 'Pages' }">Pages</router-link>
                            </li>
                        </ul>

                        <div class="container">
                            <transition name="router-fade" mode="out-in">
                                <router-view></router-view>
                            </transition>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `,

    data: function() {
        return {
            flashedMessages: flashedMessages
        }
    },

    computed: {
        currentRoute: function() {
            return this.$route.name
        }
    }
}

/* -------------------------------------------------------------------------- */

const routes = [
    { path: '/', component: Dashboard, name: 'Dashboard' },
    { path: '/posts', component: Posts, name: 'Posts' },
    { path: '/pages', component: Pages, name: 'Pages' },
    { path: "*", component: PageNotFound, name: 'PageNotFound' }
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
