months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


while True:
    try:
        date = str(input("Date: "))
        if "/" in date:
            m, d, y = date.split("/")
            m, d, y = int(m), int(d), int(y)

            if 1 <= m <= 12 and 1 <= d <= 31:
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break

        elif "," in date:
            md, y = date.split(",")
            m, d = md.split()

            if m in months:
                m = months.index(m) + 1
                d, y = int(d), int(y)

                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y:04d}-{m:02d}-{d:02d}")
                    break

    except (ValueError, IndexError):
        pass
