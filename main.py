from sorts_algorithms import bubble, merge_sort, print_merge

from Stadium import Stadium


def main():
    stadium1 = Stadium(200, 4500, "name")
    stadium2 = Stadium(250, 5000, "name")
    stadium3 = Stadium(400, 6000, "name")
    stadium4 = Stadium(300, 4800, "name")
    stadium5 = Stadium(500, 7000, "name")
    stadium6 = Stadium(450, 6500, "name")
    stadium7 = Stadium(470, 6500, "name")
    stadium8 = Stadium(490, 6500, "name")


    bubble_list = []
    bubble_list.append(stadium1.power_lighting)
    bubble_list.append(stadium2.power_lighting)
    bubble_list.append(stadium3.power_lighting)
    bubble_list.append(stadium4.power_lighting)
    bubble_list.append(stadium5.power_lighting)
    bubble_list.append(stadium6.power_lighting)
    bubble_list.append(stadium7.power_lighting)
    bubble_list.append(stadium8.power_lighting)
    bubble(bubble_list)

    merge_list = []
    merge_list.append(stadium1.number_viewers)
    merge_list.append(stadium2.number_viewers)
    merge_list.append(stadium3.number_viewers)
    merge_list.append(stadium4.number_viewers)
    merge_list.append(stadium5.number_viewers)
    merge_list.append(stadium6.number_viewers)
    merge_list.append(stadium7.number_viewers)
    merge_list.append(stadium8.number_viewers)
    merge_sort(merge_list)
    print_merge(merge_list)


main()
