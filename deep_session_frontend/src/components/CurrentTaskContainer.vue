<template>
  <div v-if="currentTask" class="current-task-container">
    <h3>Current Task in Work</h3>
    <div class="task-item">
      <span class="task-text">{{ currentTask.text }}</span>
      <span v-if="currentTask.time_spent" class="time-spent">
        Time Spent: {{ currentTask.time_spent }} seconds
      </span>
    </div>
    <div class="task-actions">
      <button @click="completeTask(currentTask.id)" class="btn toggle-btn">
        Complete
      </button>
      <button @click="undoComplete(currentTask.id)" class="btn undo-btn">
        Undo Complete
      </button>
    </div>
  </div>
  <div v-else class="no-task">
    <p>No task is currently in work.</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CurrentTask",
  data() {
    return {
      currentTask: null,
    };
  },
  async mounted() {
    await this.fetchCurrentTask();
  },
  methods: {
    async fetchCurrentTask() {
      try {
        const response = await axios.get(
          "http://localhost:8000/api/v1/tasks",
          {
            params: {
              status: "in_work",
            },
          }
        );
        this.currentTask = response.data[0] || null; // Assuming there is only one task in work
      } catch (error) {
        console.error("Failed to fetch current task:", error);
      }
    },
    async completeTask(taskId) {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${taskId}`, {
          status: "done",
        });
        await this.fetchCurrentTask(); // Refresh to show no task in work
      } catch (error) {
        console.error("Failed to complete task:", error);
      }
    },
    async undoComplete(taskId) {
      try {
        await axios.patch(`http://localhost:8000/api/v1/tasks/${taskId}`, {
          status: "in_work",
        });
        await this.fetchCurrentTask(); // Refresh to update current task
      } catch (error) {
        console.error("Failed to undo complete task:", error);
      }
    },
  },
};
</script>

<style scoped>
.current-task-container {
  background: #f1f1f1;
  border-radius: 8px;
  padding: 15px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
}

.task-item {
  display: flex;
  flex-direction: column;
}

.task-text {
  font-size: 18px;
  margin-bottom: 10px;
}

.time-spent {
  font-size: 14px;
  color: #666;
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

.undo-btn {
  background-color: #ffc107;
}

.undo-btn:hover {
  background-color: #e0a800;
}

.no-task {
  text-align: center;
  color: #999;
}
</style>
