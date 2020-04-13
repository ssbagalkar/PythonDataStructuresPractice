# https://leetcode.com/problems/the-skyline-problem/
# https://github.com/mission-peace/interview/blob/master/python/geometry/skylinedrawing.py

def get_skyline(buildings):
    building_points = []
    for building in buildings:
        building_points.append([building[0], building[2], "start"])
        building_points.append([building[1], building[2], "end"])

    building_points = sorted(building_points, key=lambda x: x[0])

    # handle edge cases:
    for ii in range(1, len(building_points)):
        if building_points[ii][0] == building_points[ii-1][0]:
            # 3 things can happen:
            # If both have same starting, first take the building with highest height
            if building_points[ii][2] == "start" and building_points[ii-1][2] == "start":
                if building_points[ii][1] > building_points[ii-1][1]:
                    building_points[ii], building_points[ii-1] = building_points[ii-1], building_points[ii]
            # if both have same ending, first take the lowest height one
            elif building_points[ii][2] == "end" and building_points[ii-1][2] == "end":
                if building_points[ii][1] < building_points[ii-1][1]:
                    building_points[ii], building_points[ii-1] = building_points[ii-1], building_points[ii]
            else:
                if building_points[ii][2] == "start":
                    building_points[ii], building_points[ii-1] = building_points[ii-1], building_points[ii]

    queue = {}
    queue[0] = 1
    prev_max_height = 0
    result = []
    for building_point in building_points:
        if building_point[2] == "start":
            if building_point[1] in queue:
                queue[building_point[1]] = queue[building_point[1]] + 1
            else:
                queue[building_point[1]] = 1

        else:
            if queue[building_point[1]] == 1:
                del queue[building_point[1]]
            else:
                queue[building_point[1]] = queue[building_point[1]] - 1

        current_max_height = max(queue.keys())

        if prev_max_height != current_max_height:
            result.append([building_point[0], current_max_height])
            prev_max_height = current_max_height
    return result


if __name__ == '__main__':
    buildings = [[1, 3, 4], [3, 4, 4], [2, 6, 2], [8, 11, 4], [7, 9, 3], [10, 11, 2]]
    print(get_skyline(buildings))