months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

def main():
    date = get_date()
    print(date)

def get_date():
    while True:
        entry = input("Date: ").strip()

        try:
            if "/" in entry:
                month, day, year = entry.split("/")
            else:
                month_name, day, year = entry.replace(",", "").split()
                month = months.index(month_name.title()) + 1

            month = int(month)
            day = int(day)
            year = int(year)

            if month < 1 or month > 12:
                continue
            if day < 1 or day > 31:
                continue
        
            return f"{year:04}-{month:02}-{day:02}"
    
        except (ValueError, IndexError):
            continue

main()
