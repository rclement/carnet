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

            <div class="row">
                <div class="col-md-6">
                    <form>
                        <div class="form-group">
                            <label for="title">Title</label>
                            <input type="text" class="form-control" id="title" :value="config.title">
                        </div>

                        <div class="form-group">
                            <label for="subtitle">Subtitle</label>
                            <input type="text" class="form-control" id="subtitle" :value="config.subtitle">
                        </div>

                        <div class="form-group">
                            <label for="author">Author</label>
                            <input type="text" class="form-control" id="author" :value="config.author">
                        </div>

                        <button type="submit" class="btn btn-primary">Save</button>
                    </form>
                </div>
            </div>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    }
}

/* -------------------------------------------------------------------------- */

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

/* -------------------------------------------------------------------------- */

const PageEdit = {
    template: `
        <div id="page">
            <div class="row">
                <div class="col-md-12">
                    <h2>Page Edit</h2>

                    <p>Last edit on {{ page.published }}.</p>

                    <form>
                        <div class="form-group">
                            <label for="pageTitle">Title</label>
                            <input type="text" class="form-control" id="pageTitle" :value="page.title">
                        </div>

                        <div class="form-group">
                            <label for="pageAuthor">Author</label>
                            <input type="text" class="form-control" id="pageAuthor" :value="page.author">
                        </div>

                        <div class="form-group">
                            <label for="pageBody">Body</label>
                            <textarea class="form-control" id="pageBody" rows="10">{{ page.body }}</textarea>
                        </div>

                        <button type="submit" class="btn btn-primary">Save</button>
                    </form>
                </div>
            </div>
        </div>
    `,

    props: ['page']
}

const Pages = {
    template: `
        <div id="pages">
            <div class="row">
                <div class="col-md-12">
                    <h2>Pages</h2>

                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Title</th>
                                    <th>Author</th>
                                    <th>Published</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-for="p in config.all_pages"
                                    v-on:click="editPage(p)">
                                    <td>{{ p.title }}</td>
                                    <td>{{ p.author }}</td>
                                    <td>{{ p.published }}</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    },

    methods: {
        editPage: function(page) {
            this.$router.push({
                name: 'PageEdit',
                params: { id: page.path }
            })
        }
    }
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
                                <router-link :to="{ name: 'Posts' }">Posts ({{ config.all_posts.length }})</router-link>
                            </li>
                            <li role="presentation" :class="{ active: currentRoute === 'Pages' }">
                                <router-link :to="{ name: 'Pages' }">Pages ({{ config.all_pages.length }})</router-link>
                            </li>
                        </ul>

                        <transition name="router-fade" mode="out-in">
                            <router-view></router-view>
                        </transition>
                    </div>
                </div>
            </div>
        </div>
    `,

    data: function() {
        return {
            config: global_config,
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
    { path: '/pages/edit/:id', component: PageEdit, name: 'PageEdit', props: (route) => ({ page: _all_pages[route.params.id] }) },
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
