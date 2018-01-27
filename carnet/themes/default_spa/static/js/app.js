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
                        {{ config.title }}
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
                                <li v-if="config.all_posts.length > 0" v-for="p in config.all_posts">
                                    <router-link :to="{ name: 'Post', params: { id: p.path } }">{{ p.title }}</router-link>
                                </li>
                                <li v-else>
                                    <a href="#">No posts</a>
                                </li>
                            </ul>
                        </li>

                        <li class="dropdown">
                            <a href="#"
                               class="dropdown-toggle"
                               data-toggle="dropdown"
                               role="button"
                               aria-haspopup="true"
                               aria-expanded="false">Pages <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">
                                <li v-if="config.all_pages.length > 0" v-for="p in config.all_pages">
                                    <router-link :to="{ name: 'Page', params: { id: p.path } }">{{ p.title }}</router-link>
                                </li>
                                <li v-else>
                                    <a href="#">No pages</a>
                                </li>
                            </ul>
                        </li>

                        <li class="dropdown">
                            <a href="#"
                               class="dropdown-toggle"
                               data-toggle="dropdown"
                               role="button"
                               aria-haspopup="true"
                               aria-expanded="false">Categories <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">
                                <li v-if="config.all_categories.length > 0" v-for="c in config.all_categories">
                                    <router-link :to="{ name: 'Category', params: { id: c.name } }">{{ c.name }}</router-link>
                                </li>
                                <li v-else>
                                    <a href="#">No categories</a>
                                </li>
                            </ul>
                        </li>

                        <li class="dropdown">
                            <a href="#"
                               class="dropdown-toggle"
                               data-toggle="dropdown"
                               role="button"
                               aria-haspopup="true"
                               aria-expanded="false">Tags <span class="caret"></span>
                            </a>
                            <ul class="dropdown-menu">
                                <li v-if="config.all_tags.length > 0" v-for="t in config.all_tags">
                                    <router-link :to="{ name: 'Tag', params: { id: t.name } }">{{ t.name }}</router-link>
                                </li>
                                <li v-else>
                                    <a href="#">No categories</a>
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

    props: ['config']
})

/* -------------------------------------------------------------------------- */

Vue.component('posts-list', {
    template: `
        <div v-if="posts.length > 0" id="posts-list">
            <ul v-for="p in posts">
                <li>
                    <router-link :to="{ name: 'Post', params: { id: p.path } }">{{ p.title }}</router-link>
                    <span v-if="p.tags.length > 0">| tags:</span>
                    <router-link v-for="t in p.tags" :key="t" :to="{ name: 'Tag', params: { id: t } }">{{ t }} </router-link>
                    <span v-if="p.categories.length > 0">| categories:</span>
                    <router-link v-for="c in p.categories" :key="c" :to="{ name: 'Category', params: { id: c } }">{{ c }} </router-link>
                </li>
            </ul>
        </div>
        <div v-else id="posts-list">
            <h3>No posts</h3>
            <hr class="intro-divider">
        </div>
    `,

    props: ['posts']
})

/* -------------------------------------------------------------------------- */

Vue.component('pages-list', {
    template: `
        <div v-if="pages.length > 0" id="pages-list">
            <ul v-for="p in pages">
                <li>
                    <router-link :to="{ name: 'Page', params: { id: p.path } }">{{ p.title }}</router-link>
                    <span v-if="p.tags.length > 0">| tags:</span>
                    <router-link v-for="t in p.tags" :key="t" :to="{ name: 'Tag', params: { id: t } }">{{ t }} </router-link>
                    <span v-if="p.categories.length > 0">| categories:</span>
                    <router-link v-for="c in p.categories" :key="c" :to="{ name: 'Category', params: { id: c } }">{{ c }} </router-link>
                </li>
            </ul>
        </div>
        <div v-else id="pages-list">
            <h3>No posts</h3>
            <hr class="intro-divider">
        </div>
    `,

    props: ['pages']
})

/* -------------------------------------------------------------------------- */

Vue.component('categories-list', {
    template: `
        <div v-if="categories.length > 0" id="categories-list">
            <ul v-for="c in categories">
                <li>
                    <router-link :to="{ name: 'Category', params: { id: c.name } }">{{ c.name }}</router-link>
                </li>
            </ul>
        </div>
        <div v-else id="categories-list">
            <h3>No categories</h3>
            <hr class="intro-divider">
        </div>
    `,

    props: ['categories']
})

/* -------------------------------------------------------------------------- */

Vue.component('tags-list', {
    template: `
        <div v-if="tags.length > 0" id="tags-list">
            <ul v-for="t in tags">
                <li>
                    <router-link :to="{ name: 'Tag', params: { id: t.name } }">{{ t.name }}</router-link>
                </li>
            </ul>
        </div>
        <div v-else id="tags-list">
            <h3>No tags</h3>
            <hr class="intro-divider">
        </div>
    `,

    props: ['tags']
})

/* -------------------------------------------------------------------------- */

const Post = {
    template: `
        <div id="post">
            <div class="row">
                <div class="col-md-12">
                    <h1>{{ post.title }}</h1>
                        <p class="text-muted">
                            Published by {{ post.author }} on {{ post.published }}
                            <br/>
                            Categories: <router-link v-for="c in post.categories" :key="c" :to="{ name: 'Category', params: { id: c } }">{{ c }} </router-link>
                            <br/>
                            Tags: <router-link v-for="t in post.tags" :key="t" :to="{ name: 'Tag', params: { id: t } }">{{ t }} </router-link>
                        </p>

                        <hr class="intro-divider">

                        <!-- HTML interpolation used on provided content already escaped -->
                        <span v-html="post.html"></span>
                </div>
            </div>
        </div>
    `,

    props: ['post']
}

const Posts = {
    template: `
        <div id="posts">
            <div class="page-header">
                <h1>Posts</h1>
            </div>

            <posts-list :posts="config.all_posts"></posts-list>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    }
}

/* -------------------------------------------------------------------------- */

const Page = {
    template: `
        <div id="page">
            <div class="row">
                <div class="col-md-12">
                    <h1>{{ page.title }}</h1>
                        <p class="text-muted">
                            Published by {{ page.author }} on {{ page.published }}
                            <br/>
                            Categories: <router-link v-for="c in page.categories" :key="c" :to="{ name: 'Category', params: { id: c } }">{{ c }} </router-link>
                            <br/>
                            Tags: <router-link v-for="t in page.tags" :key="t" :to="{ name: 'Tag', params: { id: t } }">{{ t }} </router-link>
                        </p>

                        <hr class="intro-divider">

                        <!-- HTML interpolation used on provided content already escaped -->
                        <span v-html="page.html"></span>
                </div>
            </div>
        </div>
    `,

    props: ['page']
}

const Pages = {
    template: `
        <div id="pages">
            <div class="page-header">
                <h1>Pages</h1>
            </div>

            <pages-list :pages="config.all_pages"></pages-list>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    }
}

/* -------------------------------------------------------------------------- */

const Category = {
    template: `
        <div id="category">
            <div class="page-header">
                <h1>Category <em>{{ category.name }}</em></h1>
            </div>

            <div v-if="category.pages.length > 0" class="row">
                <div class="col-md-12">
                    <h2>Pages</h2>
                    <hr class="intro-divider">

                    <pages-list :pages="category.pages"></pages-list>
                </div>
            </div>

            <div v-if="category.posts.length > 0" class="row">
                <div class="col-md-12">
                    <h2>Posts</h2>
                    <hr class="intro-divider">

                    <posts-list :posts="category.posts"></posts-list>
                </div>
            </div>
        </div>
    `,

    props: ['category']
}

const Categories = {
    template: `
        <div id="categories">
            <div class="page-header">
                <h1>Categories</h1>
            </div>

            <categories-list :categories="config.all_categories"></categories-list>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    }
}

/* -------------------------------------------------------------------------- */

const Tag = {
    template: `
        <div id="tag">
            <div class="page-header">
                <h1>Tag <em>{{ tag.name }}</em></h1>
            </div>

            <div v-if="tag.pages.length > 0" class="row">
                <div class="col-md-12">
                    <h2>Pages</h2>
                    <hr class="intro-divider">

                    <pages-list :pages="tag.pages"></pages-list>
                </div>
            </div>

            <div v-if="tag.posts.length > 0" class="row">
                <div class="col-md-12">
                    <h2>Posts</h2>
                    <hr class="intro-divider">

                    <posts-list :posts="tag.posts"></posts-list>
                </div>
            </div>
        </div>
    `,

    props: ['tag']
}

const Tags = {
    template: `
        <div id="tags">
            <div class="page-header">
                <h1>Tags</h1>
            </div>

            <tags-list :tags="config.all_tags"></tags-list>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    }
}

/* -------------------------------------------------------------------------- */

const Home = {
    template: `
        <div id="home">
            <div class="page-header">
                <h1>{{ config.title }} <small>{{ config.subtitle }}</small></h1>
            </div>

            <div v-if="pagedPosts.length > 0"
                 v-for="p in pagedPosts">
                <img v-if="p.header_image"
                     class="img-responsive"
                     alt="Post header image"
                     :src="p.header_image" />

                <h1><router-link :to="{ name: 'Post', params: { id: p.path } }">{{ p.title }}</router-link></h1>

                <p class="text-muted">
                    Published by {{ p.author }} on {{ p.published }}
                    <br/>
                    Categories: <router-link v-for="c in p.categories" :key="c" :to="{ name: 'Category', params: { id: c } }">{{ c }} </router-link>
                    <br/>
                    Tags: <router-link v-for="t in p.tags" :key="t" :to="{ name: 'Tag', params: { id: t } }">{{ t }} </router-link>
                </p>

                <!-- HTML interpolation used on provided content already escaped -->
                <span v-html="p.html"></span>
                <hr class="intro-divider">
            </div>
            <div v-else>
                <h2>No posts</h2>
                <hr class="intro-divider">
            </div>

            <nav aria-label="Page navigation">
                <ul class="pager">
                    <li v-if="postPage < postPageMax" class="previous">
                        <router-link key="previous" :to="{ name: 'Home', query: { page: this.postPage + 1 } }"><span aria-hidden="true">&larr;</span> Older</router-link>
                    </li>

                    <li v-if="postPage > 0" class="next">
                        <router-link key="next" :to="{ name: 'Home', query: { page: this.postPage - 1 } }">Newer <span aria-hidden="true">&rarr;</span></router-link>
                    </li>
                </ul>
            </nav>
        </div>
    `,

    data: function() {
        return {
            config: global_config
        }
    },

    props: {
        page: {
            default: '0'
        }
    },

    computed: {
        pageOffset: function() {
            return Math.floor(this.page)
        },

        numPosts: function() {
            return this.config.all_posts.length
        },

        postsPerPage: function() {
            return this.config.posts_per_page
        },

        postPageMax: function() {
            return Math.floor(this.numPosts / this.postsPerPage)
        },

        postPage: function () {
            return Math.max(Math.min(this.pageOffset, this.postPageMax), 0)
        },

        pagedPosts: function() {
            var start = Math.min(this.numPosts, this.postsPerPage * this.postPage)
            var end = Math.min(this.numPosts, start + this.postsPerPage)
            return this.config.all_posts.slice(start, end)
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
            <navbar-component :config="config"></navbar-component>

            <div class="container">
                <transition name="router-fade" mode="out-in">
                    <router-view></router-view>
                </transition>
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

const routes = [
    { path: '/', component: Home, name: 'Home', props: (route) => ({ page: route.query.page }) },
    { path: '/posts/', component: Posts, name: 'Posts' },
    { path: '/posts/:id', component: Post, name: 'Post', props: (route) => ({ post: _all_posts[route.params.id] }) },
    { path: '/pages/', component: Pages, name: 'Pages' },
    { path: '/pages/:id', component: Page, name: 'Page', props: (route) => ({ page: _all_pages[route.params.id] }) },
    { path: '/categories/', component: Categories, name: 'Categories' },
    { path: '/categories/:id', component: Category, name: 'Category', props: (route) => ({ category: _all_categories[route.params.id] }) },
    { path: '/tags/', component: Tags, name: 'Tags' },
    { path: '/tags/:id', component: Tag, name: 'Tag', props: (route) => ({ tag: _all_tags[route.params.id] }) },
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
