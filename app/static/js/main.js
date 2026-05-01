document.addEventListener('DOMContentLoaded', function() {
    const body = document.body;
    const themeToggle = document.getElementById('theme-toggle');
    const themeToggleIcon = document.getElementById('theme-toggle-icon');

    const applyTheme = (theme) => {
        body.setAttribute('data-theme', theme);
        if (themeToggleIcon) {
            themeToggleIcon.className = theme === 'dark' ? 'bi bi-sun' : 'bi bi-moon-stars';
        }
    };

    const savedTheme = localStorage.getItem('theme') || 'light';
    applyTheme(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const nextTheme = body.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
            localStorage.setItem('theme', nextTheme);
            applyTheme(nextTheme);
        });
    }
});

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
