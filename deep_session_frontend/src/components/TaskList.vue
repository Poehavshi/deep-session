<template>
  <div>
    <h2>Tasks</h2>
    <ul>
      <li v-for="task in tasks" :key="task.id">
        <span :style="{ textDecoration: task.done ? 'line-through' : 'none' }">
          {{ task.text }}
        </span>
        <button @click="toggleDone(task)">
          {{ task.done ? "Undo" : "Done" }}
        </button>
        <button @click="editTask(task)">Edit</button>
        <button @click="deleteTask(task.id)">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TaskList',
  data() {
    return {
      tasks: [],
    };
  },
  async mounted() {
    await this.fetchTasks();
  },
  methods: {
    async fetchTasks() {
      try {
        const response = await axios.get('http://localhost:8000/api/v1/tasks');
        this.tasks = response.data;
      } catch (error) {
        console.error('Failed to fetch tasks:', error);
      }
    },
    async toggleDone(task) {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${task.id}`, {
          done: !task.done  // Toggle the done status
        });
        task.done = !task.done;  // Update locally to reflect the change immediately
      } catch (error) {
        console.error('Failed to toggle task status:', error);
      }
    },
    editTask(task) {
      this.$emit('edit-task', task);
    },
    async deleteTask(taskId) {
      try {
        await axios.delete(`http://localhost:8000/api/v1/tasks/${taskId}`);
        await this.fetchTasks();
      } catch (error) {
        console.error('Failed to delete task:', error);
      }
    }
  }
};
</script>

<style scoped>
ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin: 10px 0;
}

button {
  margin-left: 10px;
}
</style>
