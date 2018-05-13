

<template>
  <div>
    <p>Photo -> recipe</p>

      <Form>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </Form>
        <button v-on:click="submitFile()">Submit</button>
        <br>
        <p> {{ res }} </p>
        </div>
    </div>

</template>

<script>
import axios from "axios"

export default {
    data(){
      return {
        file: '',
        res: ''
      }
    },
  methods: {

    handleFileUpload(){
        this.file = this.$refs.file.files[0];
      },
            submitFile(){
            let formData = new FormData();

            formData.append('file', this.file);
            console.log(formData)

            axios.post( '/recipes',
                formData,
                {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
              }
            ).then(response => {
              this.res = response["data"][0];
          })
      },
  },
  // created () {
  //   this.getRandom()
  // }
}
</script>