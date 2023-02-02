def traffic_light(pedestrian, time, state, count):
    sigG, sigY, sigR = 0, 0, 0

    if state == 'red':
        if count < 60:
            count += 1
            sigR = 1
        else:
            state = 'green'
            sigG = 1
    elif state == 'green':
        if pedestrian:
            if count >= 60:
                state = 'yellow'
                sigY = 1
            else:
                count += 1
                sigG = 1
        else:
            count = 0
            sigG = 1
    elif state == 'yellow':
        if count < 5:
            count += 1
            sigY = 1
        else:
            state = 'red'
            sigR = 1
            count = 0
    elif state == 'pending':
        if count < 60:
            count += 1
        else:
            state = 'yellow'
            sigY = 1
            count = 0

    return sigG, sigY, sigR, state, count


if __name__ == '__main__':
    time = 0
    state = 'red'
    count = 0
    pedestrian = False

    while time <= 200:
        if time == 70:
            pedestrian = True

        sigG, sigY, sigR, state, count = traffic_light(
            pedestrian, time, state, count)
        print("Time: ", time, " Pedestrian: ", pedestrian, " State: ", state,
              " Count: ", count, " sigG: ", sigG, " sigY: ", sigY, " sigR: ", sigR)

        time += 1
        pedestrian = False
