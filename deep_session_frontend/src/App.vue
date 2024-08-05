<template>
  <div id="app">
    <h1>Deep Session</h1>
    <task-list ref="taskList" @edit-task="selectTask" />
    <task-form :task="selectedTask" @task-updated="refreshTasks" />
  </div>
</template>

<script>
import TaskList from './components/TaskList.vue';
import TaskForm from './components/TaskForm.vue';

export default {
  name: 'App',
  components: {
    TaskList,
    TaskForm
  },
  data() {
    return {
      selectedTask: null,
    };
  },
  methods: {
    selectTask(task) {
      this.selectedTask = task;
    },
    refreshTasks() {
      this.selectedTask = null;
      this.$refs.taskList.fetchTasks();
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>