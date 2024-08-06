<template>
  <div class="task-container">
    <h2 class="task-header">Tasks</h2>
    <ul class="task-list">
      <li v-for="task in tasks" :key="task.id" class="task-item">
        <span :class="['task-text', task.status]" :style="{ textDecoration: task.status === 'done' ? 'line-through' : 'none' }">
          {{ task.text }}
        </span>
        <div class="task-actions">
          <button @click="takeInWork(task.id)" class="btn toggle-btn">Take in Work</button>
          <button @click="editTask(task)" class="btn edit-btn">Edit</button>
          <button @click="deleteTask(task.id)" class="btn delete-btn">Delete</button>
          <button @click="completeTask(task.id)" class="btn toggle-btn">Complete</button>
          <button v-if="task.status === 'done'" @click="undoComplete(task.id)" class="btn undo-btn">Undo Complete</button>
        </div>
        <span v-if="task.time_spent" class="time-spent">Time Spent: {{ task.time_spent }} seconds</span>
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
    },
    async takeInWork(taskId) {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${taskId}`, { status: 'in_work' });
        await this.fetchTasks();
      } catch (error) {
        console.error('Failed to take task in work:', error);
      }
    },
    async completeTask(taskId) {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${taskId}`, { status: 'done' });
        await this.fetchTasks();
      } catch (error) {
        console.error('Failed to complete task:', error);
      }
    },
    async undoComplete(taskId) {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${taskId}`, { status: 'in_work' });
        await this.fetchTasks();
      } catch (error) {
        console.error('Failed to undo complete task:', error);
      }
    },
  }
};
</script>

<style scoped>
.task-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.task-header {
  font-size: 24px;
  color: #333;
  margin-bottom: 20px;
}

.task-list {
  list-style-type: none;
  padding: 0;
}

.task-item {
  background: #f9f9f9;
  border-radius: 8px;
  margin: 10px 0;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.task-text {
  flex: 1;
  font-size: 18px;
  margin-right: 15px;
}

.task-text.in_work {
  color: red;
}

.task-actions {
  display: flex;
  gap: 10px;
}

.btn {
  border: none;
  border-radius: 4px;
  padding: 8px 12px;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.toggle-btn {
  background-color: #007bff;
}

.toggle-btn:hover {
  background-color: #0056b3;
}

.edit-btn {
  background-color: #28a745;
}

.edit-btn:hover {
  background-color: #218838;
}

.delete-btn {
  background-color: #dc3545;
}

.delete-btn:hover {
  background-color: #c82333;
}

.time-spent {
  font-size: 14px;
  color: #666;
  margin-top: 10px;
}
</style>
