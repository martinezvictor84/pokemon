login = function login(e){
  if (this.user && this.pass){
    axios.post('http://127.0.0.1:5000/login', {
      username: this.user,
      password: this.pass
    })
        .then(response => {
          console.log(response.data)
          localStorage._jwtToken = response.data.token;
           window.location.href = "index.html";
        })
        .catch(response => {
          this.errorMessage = "Credenciales invalidas";
        })
    e.preventDefault();
    }
}

register = function register(e){
  this.errorMessage = ''
  if (this.user && this.pass){
    this.errorMessage = ''
    axios.post('http://127.0.0.1:5000/register', {
      'username': this.user,
      'password': this.pass
    }).then(response => {
      this.user = null;
      this.pass = null;
      alert('Registro Exitoso');
    }).catch( error => {
     this.errorMessage = error.response.data.message;
    })
  }
  e.preventDefault();
}

var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!',
    pass: null,
    user: null,
    errorMessage: ''
  },
  methods: {
    login: login,
    register: register
  }
});