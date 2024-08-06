<template>
  <div class="form-container">
    <h2 class="form-header">{{ task?.id ? 'Edit Task' : 'Create Task' }}</h2>
    <form @submit.prevent="submitTask" class="task-form">
      <input v-model="taskData.text" placeholder="Task description" class="form-input" />
      <div class="form-buttons">
        <button type="submit" class="btn submit-btn">{{ task?.id ? 'Update' : 'Create' }}</button>
        <button v-if="task" @click="cancelEdit" class="btn cancel-btn">Cancel</button>
      </div>
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
        this.taskData = {...newTask};
      } else {
        this.taskData = {text: ''};
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
.form-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.form-header {
  font-size: 24px;
  margin-bottom: 20px;
  color: #333;
}

.task-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.form-input {
  margin: 10px 0;
  padding: 10px;
  width: 100%;
  max-width: 400px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 16px;
}

.form-buttons {
  display: flex;
  gap: 10px;
}

.btn {
  border: none;
  border-radius: 4px;
  padding: 10px 15px;
  color: #fff;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.submit-btn {
  background-color: #007bff;
}

.submit-btn:hover {
  background-color: #0056b3;
}

.cancel-btn {
  background-color: #dc3545;
}

.cancel-btn:hover {
  background-color: #c82333;
}
</style>
