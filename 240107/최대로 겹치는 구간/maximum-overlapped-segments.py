def find_max_overlap(lines):
    sorted_lines = sorted(lines, key=lambda x: x[0])

    max_overlap_count = 0
    current_overlap_count = 0
    previous_end = float('-inf')

    for start, end in sorted_lines:
        if start > previous_end:
            current_overlap_count = 1
        else:
            current_overlap_count += 1

        max_overlap_count = max(max_overlap_count, current_overlap_count)
        previous_end = max(previous_end, end)

    return max_overlap_count

if __name__ == "__main__":
    n = int(input())
    lines = []

    for _ in range(n):
        x1, x2 = map(int, input().split())
        lines.append((x1, x2))

    result = find_max_overlap(lines)
    print(result-1)