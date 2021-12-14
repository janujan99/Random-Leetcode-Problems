def permute(nums):
    permutations = []
    permute_nums(nums, [], set(),permutations)
    return permutations

def permute_nums(nums, curr, visited_indicies, perms):
    if len(curr) == len(nums) and not curr in perms:
        perms.append(curr)
        return
    for i in range(len(nums)):
        if not i in visited_indicies:
            permute_nums(nums, [x for x in curr]+[nums[i]], {y for y in visited_indicies}.union(set([i])), perms)
    return

print(permute([1,1,2]))