def permute(nums):
    permutations = []
    permute_nums(nums, [], permutations)
    return permutations

def permute_nums(nums, curr, perms):
    if len(curr) == len(nums) and not curr in perms:
        perms.append(curr)
        return
    for num in nums:
        if not num in set(curr):
            permute_nums(nums, [x for x in curr]+[num], perms)
    return

print(permute([1,2,3]))