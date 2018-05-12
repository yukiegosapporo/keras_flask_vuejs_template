

<template>
  <div>
    <p>Home page</p>
    <p>Random number from backend: gone</p>

      <Form>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </Form>
        <button v-on:click="submitFile()">Submit</button>
    </div>

</template>

<script>
import axios from "axios"

export default {
    data(){
      return {
        file: '',
      }
    },
  methods: {

    handleFileUpload(){
        this.file = this.$refs.file.files[0];
      },
            submitFile(){
        /*
                Initialize the form data
            */
            let formData = new FormData();

            /*
                Add the form data we need to submit
            */
            formData.append('file', this.file);
            console.log(formData)
        /*
          Make the request to the POST /single-file URL
        */
            axios.post( '/recipes',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(function(){
          console.log('SUCCESS!!');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
      },

    getRecipe() {
      // this.setState({droppedfile: acceptedFiles})
      const path = `http://localhost:5000/recipes`
      axios.post(path, this.file)
      // let req = superagent.post(window.location.href + 'recipes');
      acceptedFiles.forEach(file => {
        req.attach(['file'], file);
      });
      req.end((err, res) => {
        this.setState({objects: res.body})
      let proxyurl = "https://cors-anywhere.herokuapp.com/";
      let ep = proxyurl.concat(
        'http://www.recipepuppy.com/api/',
        '?q=',
        this.state.objects[0])
      if(this.state.objects.length>0){
      fetch(ep, {
          mode: 'cors'
        })
      .then(results => results.json())
      .then(j => {
          this.setState({response: j['results']});
          console.log(j)
        });

    }
        if (err) console.log('err: ', err);
      })
    }


  },
  // created () {
  //   this.getRandom()
  // }
}
</script>