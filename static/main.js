token = localStorage.getItem('_jwtToken')
console.log(apiPatch)
if (!token){
  window.location.href = "login.html";
}
headers = {Authorization: token}

function logout(){
  localStorage.removeItem('_jwtToken ')
  console.log('logout')
  window.location.href = "login.html";
}

function mounted(){
    axios.get(apiPatch+"/types", {headers} )
      .then(res => {
          console.log(res.data)
          this.types = res.data
      })
      .catch(res => {
          if (res.response.status == 401){
              window.location.href = "login.html";
          }
      })
    params = {per_page: 12}
    axios.get(apiPatch+"/pokemon", {headers, params})
        .then(res => {
            this.pokemons = res.data;
            console.log(this.pokemons);
        })
        .catch(res => {
            if (res.response.status == 401){
                window.location.href = "login.html";
            }
        })
}

function nextPage(){
    this.page = this.page + 1
    params = {per_page: 12, page: this.page, ...this.filter}
    axios.get(apiPatch+"/pokemon", {headers, params})
        .then(res => {
            this.pokemons = res.data;
            console.log(this.pokemons);
        })
        .catch(res => {
            if (res.response.status == 401){
                window.location.href = "login.html";
            }
        })
}

function beforePage(){
    this.page = (this.page==0) ? 0 : this.page-1
    params = {per_page: 12, page: this.page, ...this.filter}
    axios.get(apiPatch+"/pokemon", {headers, params})
        .then(res => {
            this.pokemons = res.data;
            console.log(this.pokemons);
        })
        .catch(res => {
            if (res.response.status == 401){
                window.location.href = "login.html";
            }
        })
}

function applyFilter(){
    delete  this.filter.is_legendary;
    this.page = 0;
    if (this.is_legendary){
        this.filter.is_legendary = 1;
    }
    if(this.orderByFilter){
        this.filter.order_by = this.orderByFilter.by
        this.filter.order_by_dir = this.orderByFilter.dir
    }
    params = {per_page: 12, page: this.page, ...this.filter}
    axios.get(apiPatch+"/pokemon", {headers, params})
        .then(res => {
            this.pokemons = res.data;
            console.log(this.pokemons);
        })
        .catch(res => {
            if (res.response.status == 401){
                window.location.href = "login.html";
            }
        })
}

generations=[1,2,3,4,5,6];

var app = new Vue({
  el: '#app',
  data: {
      message: 'Hello Vue!',
      is_legendary: false,
      orderByFilter: null,
      generations: [1,2,3,4,5,6],
      types: [],
      pokemons: [],
      page: 0,
      filter: {
          type: null,
          generation: null,
          is_legendary: 0
      },
      orderBy: [
          {name: 'hp(desc)', by: 'hp', dir: 'desc'},
          {name: 'hp(asc)', by: 'hp', dir: 'asc'},
          {name: 'Ataque(desc)', by: 'attack', dir: 'desc'},
          {name: 'Ataque(asc)', by: 'attack', dir: 'asc'},
          {name: 'Defensa(desc)', by: 'defense', dir: 'desc'},
          {name: 'Defensa(asc)', by: 'defense', dir: 'asc'}
      ]
  },
  mounted: mounted,
  methods: {
      logout: logout,
      nextPage: nextPage,
      beforePage: beforePage,
      applyFilter: applyFilter

  }
})