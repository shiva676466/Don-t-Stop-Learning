"""Generator utilities for learning roadmaps and flowcharts."""
from typing import List, Dict


SKILLS = {
    'DSA': ['Arrays', 'Strings', 'Linked Lists', 'Stacks & Queues', 'Trees', 'Graphs', 'Hashing', 'Sorting', 'Searching'],
    'Web Development': ['HTML & CSS', 'JavaScript', 'DOM', 'HTTP & REST', 'Frontend Framework', 'Backend Basics', 'Databases', 'Deployment'],
    'Machine Learning': ['Linear Algebra', 'Probability', 'Data Processing', 'Supervised Learning', 'Model Evaluation', 'Neural Networks'],
    'DevOps': ['Linux Basics', 'Shell Scripting', 'CI/CD', 'Containers', 'IaC', 'Monitoring & Logging'],
    'Cloud': ['Cloud Concepts', 'Compute', 'Storage', 'Networking', 'Security', 'IaC', 'Monitoring'],
    'Mobile': ['Mobile Basics', 'Layouts & UI', 'Networking', 'Storage', 'Optimization', 'Publishing']
}


def generate_roadmap_tasks(skill: str, level: str, time_per_day: str) -> List[Dict]:
    topics = SKILLS.get(skill, ['Intro', 'Core', 'Advanced'])
    tasks = []
    for i, t in enumerate(topics, start=1):
        tasks.append({
            'id': i,
            'title': t,
            'description': f'Learn {t}',
            'due_date': f'Week {((i-1)//3)+1}',
            'is_completed': False,
        })
    return tasks

"""Generator utilities for learning roadmaps and Mermaid flowcharts.

This file provides a small, deterministic generator used by the
learning blueprint. It is intentionally lightweight so it can be
replaced later with a more sophisticated planner or model-driven
generator.
"""

from typing import List, Dict


SKILLS: Dict[str, List[str]] = {
    "DSA": [
        "Arrays",
        "Strings",
        "Linked Lists",
        "Stacks & Queues",
        "Trees",
        "Graphs",
        "Hashing",
        "Sorting",
        "Searching",
    ],
    "Web Development": [
        "HTML & CSS",
        "JavaScript",
        "DOM",
        "HTTP & REST",
        "Frontend Framework",
        "Backend Basics",
        "Databases",
        "Deployment",
    ],
    "Machine Learning": [
        "Linear Algebra",
        "Probability",
        "Data Processing",
        "Supervised Learning",
        "Model Evaluation",
        "Neural Networks",
    ],
    "DevOps": [
        "Linux Basics",
        "Shell Scripting",
        "CI/CD",
        "Containers",
        "Infrastructure as Code",
        "Monitoring & Logging",
    ],
    "Cloud": [
        "Cloud Concepts",
        "Compute",
        "Storage",
        "Networking",
        "Security",
        "IaC",
        "Monitoring",
    ],
    "Mobile": [
        "Mobile Basics",
        "Layouts & UI",
        "Networking",
        "Storage",
        "Optimization",
        "Publishing",
    ],
}


def generate_roadmap_tasks(skill: str, level: str, time_per_day: str) -> List[Dict]:
    """Produce a list of task dictionaries for a simple roadmap.

    Each task contains: id (int), title (str), description (str),
    due_date (str) and is_completed (bool).

    This is deterministic and safe for unit testing.
    """

    topics = SKILLS.get(skill, ["Intro", "Core", "Advanced"])[:]
    tasks: List[Dict] = []
    for i, title in enumerate(topics, start=1):
        tasks.append(
            {
                "id": i,
                "title": title,
                "description": f"Learn {title}",
                "due_date": f"Week {((i - 1) // 3) + 1}",
                "is_completed": False,
            }
        )

    return tasks


def mermaid_from_tasks(tasks: List[Dict]) -> str:
    """Convert a list of task dicts into a Mermaid flowchart string.

    The generated graph is a simple top-to-bottom chain with optional
    cross-links for readability when many nodes exist.
    """

    if not tasks:
        return "flowchart TB\nstart((Start))"

    lines: List[str] = ["flowchart TB"]

    # Create nodes
    for t in tasks:
        node_id = f"n{int(t['id'])}"
        # remove quotes to avoid breaking the mermaid literal
        label = str(t["title"]).replace('"', "'")
        lines.append(f"{node_id}[\"{label}\"]")

    # Chain edges
    for i in range(1, len(tasks)):
        lines.append(f"n{i} --> n{i+1}")

    # Add a couple of helpful cross-links for longer lists
    if len(tasks) >= 4:
        lines.append("n1 --> n3")
        if len(tasks) >= 6:
            lines.append("n2 --> n5")

    return "\n".join(lines)


def generate_roadmap(skill: str, level: str, time_per_day: str, goal: str) -> Dict:
    """High-level helper returning roadmap data and mermaid text.

    Returns a dict with keys: skill, level, time_per_day, goal, tasks, mermaid
    """

    tasks = generate_roadmap_tasks(skill, level, time_per_day)
    mermaid = mermaid_from_tasks(tasks)
    return {
        "skill": skill,
        "level": level,
        "time_per_day": time_per_day,
        "goal": goal,
        "tasks": tasks,
        "mermaid": mermaid,
    }


__all__ = [
    "SKILLS",
    "generate_roadmap_tasks",
    "mermaid_from_tasks",
    "generate_roadmap",
]