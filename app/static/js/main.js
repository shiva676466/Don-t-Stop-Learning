// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Toggle task completion via AJAX
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
                    // Optional: update visual feedback
                    const taskDiv = document.getElementById(`task-${taskId}`);
                    if (taskDiv) {
                        const title = taskDiv.querySelector('strong');
                        if (data.is_completed) {
                            title.style.textDecoration = 'line-through';
                        } else {
                            title.style.textDecoration = 'none';
                        }
                    }
                } else {
                    alert('Error toggling task.');
                    // Revert checkbox state if needed
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