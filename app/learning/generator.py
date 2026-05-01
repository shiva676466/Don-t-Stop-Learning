# app/learning/generator.py

TEMPLATES = {
    'DSA': {
        'beginner': [
            ('Arrays – Basics', 'Learn indexing, traversing, insertion, deletion. Solve 2 easy problems.'),
            ('Arrays – Two Pointers', 'Understand two‑pointer technique. Solve 1 problem.'),
            ('Strings – Basics', 'String operations, reversing, palindrome check. Solve 2 easy problems.'),
            ('Linked Lists – Introduction', 'Singly linked list creation, traversal, insertion. Solve 1 problem.'),
            ('Stacks & Queues', 'Stack operations, queue operations, applications. Solve 1 problem.'),
            ('Recursion – Fundamentals', 'Factorial, Fibonacci, tree recursion. Solve 2 easy problems.'),
            ('Sorting – Basic Algorithms', 'Bubble, Selection, Insertion sort. Implement them.'),
            ('Searching – Linear & Binary', 'Understand binary search. Solve 1 problem.'),
        ],
        'intermediate': [
            ('Trees – Binary Trees', 'Traversal (pre, in, post), height, diameter. Solve 2 problems.'),
            ('Binary Search Trees', 'Insert, delete, search, validate BST. Solve 1 problem.'),
            ('Graphs – BFS & DFS', 'Graph representation, BFS, DFS. Solve 1 problem.'),
            ('Dynamic Programming – Introduction', 'Fibonacci, coin change, knapsack. Solve 2 problems.'),
            ('Hashing', 'Hash maps, sets, collision handling. Solve 1 problem.'),
            ('Heaps & Priority Queues', 'Min heap, max heap, heap sort. Solve 1 problem.'),
            ('Greedy Algorithms', 'Activity selection, fractional knapsack. Solve 1 problem.'),
        ],
        'advanced': [
            ('Advanced Graphs', 'Dijkstra, Bellman Ford, Floyd Warshall. Solve 1 problem.'),
            ('Tries', 'Insert, search, auto‑complete. Solve 1 problem.'),
            ('Segment Trees', 'Build, query, update. Solve 1 problem.'),
            ('Advanced DP', 'Edit distance, matrix chain multiplication. Solve 1 problem.'),
            ('Backtracking', 'N‑Queens, Sudoku solver. Solve 1 problem.'),
            ('Bit Manipulation', 'Tricks, power set, subset sums. Solve 1 problem.'),
            ('System Design Basics', 'Load balancing, caching, microservices.'),
        ]
    },
    'Web Development': {
        'beginner': [
            ('HTML Basics', 'Tags, forms, semantic HTML. Build a personal page.'),
            ('CSS Basics', 'Selectors, box model, flexbox. Style your HTML page.'),
            ('JavaScript Basics', 'Variables, loops, functions, DOM manipulation. Add interactivity.'),
            ('Responsive Design', 'Media queries, mobile‑first design. Make your page responsive.'),
            ('Git & GitHub', 'Init, commit, push, pull. Put your project on GitHub.'),
            ('Bootstrap or Tailwind', 'Use a CSS framework to redesign your page quickly.'),
            ('Basic Terminal', 'Command line basics, file navigation.'),
            ('Mini Project', 'Build a simple landing page from scratch.'),
        ],
        'intermediate': [
            ('Advanced JavaScript', 'ES6, promises, async/await, modules.'),
            ('Frontend Framework (React)', 'Components, state, props, hooks. Build a to‑do app.'),
            ('Backend Basics (Node.js or Flask)', 'Routes, requests, responses. Create a simple API.'),
            ('Databases (SQL)', 'Tables, CRUD, joins. Connect your app to a database.'),
            ('REST APIs', 'Design and build a full REST API for your project.'),
            ('Authentication', 'JWT, sessions, OAuth basics. Add login to your app.'),
            ('Deployment', 'Deploy a full‑stack app to Render / Vercel.'),
        ],
        'advanced': [
            ('State Management (Redux)', 'Store, actions, reducers. Integrate into React app.'),
            ('Testing (Unit & Integration)', 'Jest, React Testing Library. Write tests.'),
            ('CI/CD', 'GitHub Actions, automated deployment.'),
            ('WebSockets', 'Real‑time chat app.'),
            ('Performance Optimization', 'Lazy loading, code splitting, memoization.'),
            ('Security', 'XSS, CSRF, SQL injection, security headers.'),
            ('System Design', 'Scalable architecture, caching, database sharding.'),
        ]
    }
}

def generate_roadmap_tasks(skill, level, time_per_day):
    """
    Returns a list of dicts with 'title', 'description', 'order', 'due_date'.
    Adjusts number of tasks per week based on time_per_day.
    """
    skill = skill.strip()
    level = level.lower()
    time_str = time_per_day.lower()   # e.g. '1 hour', '30 minutes', '2 hours'

    # Extract numeric hours for rough adjustment
    try:
        words = time_str.split()
        if 'hour' in words:
            hours = float(words[0])
        elif 'min' in words:
            hours = float(words[0]) / 60
        else:
            hours = 1.0
    except:
        hours = 1.0

    # Base task list from template
    base_tasks = TEMPLATES.get(skill, {}).get(level, [])
    if not base_tasks:
        base_tasks = [('Start Learning', 'Explore resources and set up your environment.')]

    # Spacing: one task per day? For simplicity, we assign one task per day,
    # but if hours per day is small (< 0.5h), we might only assign 3-4 tasks per week.
    # For MVP, just return all tasks in order, with due_date "Week X, Day Y".
    tasks = []
    day_counter = 0
    for idx, (title, desc) in enumerate(base_tasks):
        week = day_counter // 7 + 1
        day = day_counter % 7 + 1
        due = f"Week {week}, Day {day}"
        tasks.append({
            'title': title,
            'description': desc,
            'order': idx,
            'due_date': due
        })
        # If time is limited, add extra day between tasks (skip a day)
        if hours < 0.5:
            day_counter += 2   # one task every two days
        else:
            day_counter += 1

    return tasks