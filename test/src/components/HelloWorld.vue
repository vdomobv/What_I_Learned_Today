<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <button @click="ChildToParent">클릭</button>
    <!-- <h2>{{$store.state.message}} </h2> -->
    <h2>state로 바로 접근하기 보다 computed에 정의 후 접근 권장 {{ message}} </h2>
    <h3>길이 : {{messageLength }} </h3>
    <h3>x2 : {{doubleLength }} </h3>
    <input type="text" @keyup.enter="changeMessage" v-model="inputData">
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  data() {
    return {
      inputData : null,
    }
  },
  computed: {
    message() {
      return this.$store.state.message
    }, 
    messageLength() {
      return this.$store.getters.messageLength
    },
    doubleLength() {
      return this.$store.getters.doubleLength
    }
  },
  methods : {
    changeMessage() {
      const newMessage = this.inputData
      this.$store.dispatch('changeMessage', newMessage)
      this.inputData = null
    },
    ChildToParent() {
      this.$emit('child-to-parent')
    }
  },
  beforeCreated() {
    console.log("beforeCreated");
  },
  created() {
    console.log("created");
  },
  beforeMount() {
    console.log("beforeMount");
  },
  mounted() {
    console.log("mounted");
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
