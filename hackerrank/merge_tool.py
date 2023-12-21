def merge_tool(string, k):
    for s in range(0, len(string), k):
        t = string[s:s+k]
        u = ""
        for char in t:
            if char not in u:
                u += char
        print(u)


if __name__ == "__main__":
    text = 'AABCAAADA'
    k_v = 3
    merge_tool(text, k_v)

