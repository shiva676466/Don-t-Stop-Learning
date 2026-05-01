document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.task-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskId = this.dataset.taskId;
            fetch(`/task/${taskId}/toggle`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const taskDiv = document.getElementById(`task-${taskId}`);
                    if (taskDiv) {
                        taskDiv.classList.toggle('completed', data.is_completed);
                    }
                } else {
                    alert('Error toggling task.');
                    this.checked = !this.checked;
                }
            })
            .catch(err => {
                console.error(err);
                alert('Network error.');
                this.checked = !this.checked;
            });
        });
    });
});
