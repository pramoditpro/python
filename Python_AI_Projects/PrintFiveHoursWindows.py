from datetime import datetime, timedelta

def calculate_windows(start_time: datetime, num_windows: int = 5) -> list:
    windows = []
    for i in range(num_windows):
        window_start = start_time + timedelta(hours=5 * i)
        window_end   = window_start + timedelta(hours=5)
        windows.append((i + 1, window_start, window_end))
    return windows

def print_table(windows: list, now: datetime):
    # Column widths
    col1, col2, col3, col4 = 10, 22, 22, 14

    # Header
    header = (
        f"{'Window':<{col1}}"
        f"{'Start Time':<{col2}}"
        f"{'End Time':<{col3}}"
        f"{'Status':<{col4}}"
    )
    separator = "-" * (col1 + col2 + col3 + col4)

    print("\n" + "=" * (col1 + col2 + col3 + col4))
    print("         CLAUDE 5-HOUR WINDOW CALCULATOR")
    print("=" * (col1 + col2 + col3 + col4))
    print(header)
    print(separator)

    for num, start, end in windows:
        if now < start:
            status = "⏳ Upcoming"
        elif start <= now < end:
            # Calculate time remaining
            remaining = end - now
            mins = int(remaining.total_seconds() // 60)
            hrs  = mins // 60
            mins = mins % 60
            status = f"✅ ACTIVE ({hrs}h {mins}m left)"
        else:
            status = "✔ Expired"

        fmt = "%d-%b-%Y %I:%M %p"
        row = (
            f"Window {num:<{col1 - 7}}"
            f"{start.strftime(fmt):<{col2}}"
            f"{end.strftime(fmt):<{col3}}"
            f"{status:<{col4}}"
        )
        print(row)

    print(separator)
    print(f"\n  Current time : {now.strftime('%d-%b-%Y %I:%M %p')}")
    print()

def get_start_time() -> datetime:
    print("\n╔══════════════════════════════════════════╗")
    print("║   Claude 5-Hour Window Calculator 🪟     ║")
    print("╚══════════════════════════════════════════╝")
    print("\nWhen do you want the first window to start?")
    print("  [1] Right now (current time)")
    print("  [2] Enter a custom time")
    choice = input("\nEnter choice (1 or 2): ").strip()

    now = datetime.now()

    if choice == "1":
        return now
    elif choice == "2":
        while True:
            time_input = input("Enter start time (HH:MM, 24hr format, e.g. 09:15): ").strip()
            try:
                t = datetime.strptime(time_input, "%H:%M")
                # Use today's date with entered time
                start = now.replace(hour=t.hour, minute=t.minute, second=0, microsecond=0)
                # If entered time is earlier than current time, assume it already started today
                return start
            except ValueError:
                print("❌ Invalid format. Please enter time as HH:MM (e.g. 09:15)")
    else:
        print("Invalid choice. Using current time.")
        return now

def main():
    start_time = get_start_time()
    now        = datetime.now()
    windows    = calculate_windows(start_time, num_windows=5)
    print_table(windows, now)

    # Find active window and give tip
    for num, start, end in windows:
        if start <= now < end:
            remaining = end - now
            mins = int(remaining.total_seconds() // 60)
            print(f"  💡 Tip: You are in Window {num}. It resets in {mins // 60}h {mins % 60}m.")
            print(f"     Unused messages do NOT carry over to Window {num + 1}.\n")
            break

if __name__ == "__main__":
    main()