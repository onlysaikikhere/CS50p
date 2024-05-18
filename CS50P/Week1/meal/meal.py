def main():
    answer = input("Enter Time")
    time = convert(answer)
    if 7<=time<=8:
        print("breakfast time")
    if 12<=time<=13:
        print("lunch time")
    if 18<=time<=19:
        print("dinner time")

def convert(time):
    hours , minutes = time.split(":")
    new_minute = float(minutes)/60
    return float(hours)+ new_minute

if __name__ == "__main__":
    main()
