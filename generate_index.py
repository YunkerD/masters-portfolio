import os

def collect_html_links_by_semester(base_dirs):
    semester_links = {"semester1": [], "semester2": []}
    for base in base_dirs:
        semester = "semester1" if "semester1" in base else "semester2"
        for root, _, files in os.walk(base):
            for file in files:
                if file.endswith(".html"):
                    rel_path = os.path.join(root, file).replace("\\", "/")
                    link_html = f'<li><a href="{rel_path}">{file}</a></li>'
                    semester_links[semester].append(link_html)
    return semester_links

def build_html(semester_links):
    with open("index.html", "r", encoding="utf-8") as f:
        lines = f.readlines()

    def replace_section(lines, section_id, new_links):
        start = next(i for i, line in enumerate(lines) if f'id="{section_id}"' in line)
        ul_start = start + 1
        ul_end = next(i for i in range(ul_start, len(lines)) if "</ul>" in lines[i])
        return lines[:ul_start] + new_links + lines[ul_end:]

    lines = replace_section(lines, "semester1-list", semester_links["semester1"])
    lines = replace_section(lines, "semester2-list", semester_links["semester2"])

    with open("index.html", "w", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    semester_links = collect_html_links_by_semester([
        "notebooks/semester1", "notebooks/semester2",
        "projects/semester1", "projects/semester2"
    ])
    build_html(semester_links)

    def count_html_files(base_dirs):
    total = 0
    for base in base_dirs:
        for root, _, files in os.walk(base):
            total += sum(1 for file in files if file.endswith(".html"))
    return total

if __name__ == "__main__":
    semester_links = collect_html_links_by_semester([
        "notebooks/semester1", "notebooks/semester2",
        "projects/semester1", "projects/semester2"
    ])
    build_html(semester_links)

    total_files = count_html_files(["projects/semester1"])
    progress = min(100, int((total_files / 10) * 100))  # Adjust denominator as needed

    print(f"Semester 1 progress: {progress}%") 