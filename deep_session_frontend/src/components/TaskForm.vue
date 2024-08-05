<template>
  <div>
    <h2>{{ task?.id ? 'Edit Task' : 'Create Task' }}</h2>
    <form @submit.prevent="submitTask">
      <input v-model="taskData.text" placeholder="Task description" />
      <button type="submit">{{ task?.id ? 'Update' : 'Create' }}</button>
      <button v-if="task" @click="cancelEdit">Cancel</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TaskForm',
  props: {
    task: Object
  },
  data() {
    return {
      taskData: {
        text: ''
      }
    };
  },
  watch: {
    task(newTask) {
      if (newTask) {
        this.taskData = { ...newTask };
      } else {
        this.taskData = { text: '' };
      }
    }
  },
  methods: {
    async submitTask() {
      if (this.taskData.id) {
        await this.updateTask();
      } else {
        await this.createTask();
      }
      // Emit an event to update the task list
      this.$emit('task-updated');
    },
    async createTask() {
      try {
        await axios.post('http://localhost:8000/api/v1/tasks', this.taskData);
        this.taskData.text = '';
      } catch (error) {
        console.error('Failed to create task:', error);
      }
    },
    async updateTask() {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${this.taskData.id}`, this.taskData);
      } catch (error) {
        console.error('Failed to update task:', error);
      }
    },
    cancelEdit() {
      this.$emit('task-updated');
    }
  }
};
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

input {
  margin: 10px 0;
  padding: 8px;
  width: 80%;
  max-width: 300px;
}

button {
  margin: 5px;
  padding: 5px 10px;
}
</style>