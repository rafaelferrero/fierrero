const routes = [
  {
    path: '/',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      {
        path: '',
        component: () => import('pages/Index.vue')
      }
    ]
  },
  {
    path: '/listados',
    component: () => import('layouts/MyLayout.vue'),
    children: [
      {
        path: 'empresas', // here it is, route /listados/empresas
        component: () => import('pages/Empresas.vue')
      },
      {
        path: 'personas', // here it is, route /user/posts
        component: () => import('pages/Personas.vue')
      }
    ]
  }
]

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  })
}

export default routes
