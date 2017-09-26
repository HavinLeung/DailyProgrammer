f = open('input_daily330.txt', 'r')
circles = list(map(float, f.read().replace('\n', ',').split(',')))
max_x = min_x = circles[0]
max_y = min_y = circles[1]
for i in range(2,len(circles), 3):
    current_max_x = circles[i-2] + circles[i]
    current_min_x = circles[i-2] - circles[i]
    current_max_y = circles[i-1] + circles[i]
    current_min_y = circles[i-1] - circles[i]
    if current_max_x > max_x:
        max_x = current_max_x
    if current_max_y > max_y:
        max_y = current_max_y
    if current_min_x < min_x:
        min_x = current_min_x
    if current_min_y < min_y:
        min_y = current_min_y

print('(%.3f, %.3f), (%.3f, %.3f), (%.3f, %.3f), (%.3f, %.3f)' % (min_x, min_y, min_x, max_y, max_x, max_y, max_x, min_y))
f.close()
