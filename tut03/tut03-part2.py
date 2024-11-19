def make_permutn(s):
    def permute(chars, l, r):
        if l == r:
            permutation.add(''.join(chars))
        else:
            for i in range(l, r + 1):
                chars[l], chars[i] = chars[i], chars[l]
                permute(chars, l + 1, r)
                chars[l], chars[i] = chars[i], chars[l]

    permutation = set()
    chars = list(s)
    permute(chars, 0, len(chars) - 1)
    return list(permutation)


s = input("Enter a string: ")
permutn = make_permutn(s)
print(permutn)