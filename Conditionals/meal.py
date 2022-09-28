def main():
    ans = input("What time is it? ")
    time = convert(ans)
    if time >= 7 and time <= 8:
        print('Breakfast time')
    if time >= 12 and time <= 13:
        print('Lunch time')
    if time >=  18 and time <= 19:
        print('Dinner time')



def convert(time):
    hours, minutes = time.split(":")
    new_minutes = float(minutes) / 60
    return float(hours) + new_minutes



if __name__ == "__main__":
    main()
