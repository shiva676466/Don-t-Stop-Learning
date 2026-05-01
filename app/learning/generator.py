"""Generator utilities for learning roadmaps and Mermaid flowcharts.

This module provides a small, deterministic generator used by the learning
blueprint. It exposes an expanded SKILLS catalog and produces Mermaid
flowcharts that group tasks per week for easier visualization and
client-side pan/zoom support.
"""

from typing import List, Dict


# Expanded skills/domains
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
    "Security": [
        "Intro to Security",
        "Web Security Basics",
        "Authentication & Authorization",
        "OWASP Top 10",
        "Secure Coding Practices",
    ],
    "Data Engineering": [
        "ETL Concepts",
        "Data Modeling",
        "SQL at Scale",
        "Batch & Streaming",
        "Data Warehousing",
    ],
    "MLOps": [
        "Model Versioning",
        "Serving Models",
        "Monitoring Models",
        "CI/CD for ML",
    ],
    "Embedded": [
        "C Basics",
        "Microcontroller Fundamentals",
        "Peripheral Interfaces",
        "RTOS Basics",
    ],
}


def generate_roadmap_tasks(skill: str, level: str, time_per_day: str) -> List[Dict]:
    """Produce a list of task dictionaries for a simple roadmap.

    Each task contains: id (int), order (int), title (str), description (str),
    due_date (str) and is_completed (bool).
    """

    topics = SKILLS.get(skill, ["Intro", "Core", "Advanced"])[:]
    tasks: List[Dict] = []
    for i, title in enumerate(topics, start=1):
        tasks.append(
            {
                "id": i,
                "order": i - 1,
                "title": title,
                "description": f"Learn {title}",
                "due_date": f"Week {((i - 1) // 3) + 1}",
                "is_completed": False,
            }
        )

    return tasks


def mermaid_from_tasks(tasks: List[Dict]) -> str:
    """Convert a list of task dicts into a Mermaid flowchart string grouped by week.

    Node ids are generated incrementally (n1, n2, ...) to avoid collisions
    when tasks come from multiple sources.
    """

    if not tasks:
        return "flowchart TB\nstart((Start))"

    lines: List[str] = ["flowchart TB\n\tclassDef week fill:#f8f9ff,stroke:#e9ecef;\n"]

    # Organize tasks by week preserving order
    weeks: Dict[str, List[Dict]] = {}
    for t in tasks:
        week = t.get("due_date", "Week 1")
        weeks.setdefault(week, []).append(t)

    node_map: Dict[str, str] = {}
    flat_nodes: List[str] = []
    counter = 1

    for w_idx, (week, items) in enumerate(sorted(weeks.items()), start=1):
        lines.append(f"\tsubgraph {week.replace(' ', '_')}")
        for t in items:
            node_id = f"n{counter}"
            counter += 1
            node_map[f"{week}:{t['title']}"] = node_id
            flat_nodes.append(node_id)
            label = str(t["title"]).replace('"', "'")
            lines.append(f"\t\t{node_id}[\"{label}\"]")
        lines.append("\tend")

    # Connect nodes in chronological order across weeks
    for i in range(len(flat_nodes) - 1):
        lines.append(f"\t{flat_nodes[i]} --> {flat_nodes[i+1]}")

    # Small heuristics for cross-links
    if len(flat_nodes) >= 4:
        lines.append(f"\t{flat_nodes[0]} --> {flat_nodes[2]}")
    if len(flat_nodes) >= 6:
        lines.append(f"\t{flat_nodes[1]} --> {flat_nodes[4]}")

    return "\n".join(lines)


def generate_roadmap(skill: str, level: str, time_per_day: str, goal: str) -> Dict:
    """High-level helper returning roadmap data and mermaid text."""

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