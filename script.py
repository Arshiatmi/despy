from despy import Descision, FinalDescision


betray_ally_and_kill_them = Descision({
    "Trust John": Descision({
        "Nothing": FinalDescision("You Have Been Killed :/"),
        "Kill John": FinalDescision("John Didnt Let You Kill Him. You Have Been Killed :/"),
    }, "John Brings You Somewhere Strange. What You Are Gonna Do?"),
    "Kill John": FinalDescision("John Didnt Let You Kill Him. You Have Been Killed :/"),
}, "A Person Named John Came To You. He Says He Can Help You To Join Enemies.")

stick_with_ally_and_kill_them = Descision({
    "Accept": FinalDescision("The Made You Quit The Military :/"),
    "Refuse": Descision({
        "Accept": FinalDescision("The Made You Quit The Military :/"),
        "Refuse": FinalDescision("Fernando Killed You :/"),
    }, "Fernando Insists.")
}, "Seems That Hard For Your Friends To Trust You Again.Fernando Came You You And Ask You To Quit The Fight.What Do You Do ?")

main_descision = Descision({
    "kill enemy": Descision({
        "Kill Other Enemy.": FinalDescision("You Won !"),
        "Show Mercy": FinalDescision("You Have Been Killed."),
    }, "Another Enemy Appeared. What You Are Gonna Do ?"),
    "join enemy": Descision({
        "Betray Ally And Kill Them.": betray_ally_and_kill_them,
        "Stick With Ally And Kill Enemies.": stick_with_ally_and_kill_them
    }, "Your Allies Beg You To Come Back."),
    "show mercy": FinalDescision("They Killed You :/"),
})

# while a.has_next_descision():
#     selected_index, selected_text, a = (a.execute())
# a(True)

for i in main_descision.run_cycle():
    print(i)
