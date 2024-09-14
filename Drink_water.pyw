from plyer import notification as n


def notify():
    n.notify(
        title="That's enough.\nGo Drink Some Water.\nIt's time to take a break!",
        message="you have passed 1hr while working",
        app_icon="C:\\Users\\DELL\\Desktop\\icons\\ico\\coffee.ico",
        timeout=8,
    )


if __name__ == "__main__":
    notify()
