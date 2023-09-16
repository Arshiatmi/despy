from despy import Descision, FinalDescision, Config


"""
You Can Change The Config IF You Want.
    FROM_ZERO :  Default Is False. Its For Descision Hash And If You Set It True
                Descision Hash Will Be Made From 0 ( First Index Would Be Assumed
                 As 0 ) And If Its False, First Index Will Be Assumed As 1.
"""
Config.FROM_ZERO = False


class CustomDescision(Descision):
    """
        I Wrote A Custom Descision Here. Its Exact Like Descision But In My Custom Way :)
        In Fact I Just Tried To print Derscision Hash Before Execute The Descision Process.
    """

    def execute(self, get_input=True):
        Config.print_descision_hash(
            pretext="Hash :", empty_text="You Are In Root.", end='\n')
        # Or Like This : Config.print_descision_hash()
        return super().execute(get_input)


betray_ally_and_kill_them = CustomDescision({
    "Trust John": CustomDescision({
        "Nothing": FinalDescision("You Have Been Killed :/"),
        "Kill John": FinalDescision("John Didnt Let You Kill Him. You Have Been Killed :/"),
    }, "John Brings You Somewhere Strange. What You Are Gonna Do?"),
    "Kill John": FinalDescision("John Didnt Let You Kill Him. You Have Been Killed :/"),
}, "A Person Named John Came To You. He Says He Can Help You To Join Enemies.")

stick_with_ally_and_kill_them = CustomDescision({
    "Accept": FinalDescision("The Made You Quit The Military :/"),
    "Refuse": CustomDescision({
        "Accept": FinalDescision("The Made You Quit The Military :/"),
        "Refuse": FinalDescision("Fernando Killed You :/"),
    }, "Fernando Insists.")
}, "Seems That Hard For Your Friends To Trust You Again.Fernando Came You You And Ask You To Quit The Fight.What Do You Do ?")

main_descision = CustomDescision({
    "kill enemy": CustomDescision({
        "Kill Other Enemy.": FinalDescision("You Won !"),
        "Show Mercy": FinalDescision("You Have Been Killed."),
    }, "Another Enemy Appeared. What You Are Gonna Do ?"),
    "join enemy": CustomDescision({
        "Betray Ally And Kill Them.": betray_ally_and_kill_them,
        "Stick With Ally And Kill Enemies.": stick_with_ally_and_kill_them
    }, "Your Allies Beg You To Come Back."),
    "show mercy": FinalDescision("They Killed You :/"),
})

"""
Way 1 :
    while main_descision.has_next_descision():
        selected_index, selected_text, main_descision = (main_descision.execute())
    main_descision(True)

Way 2 :
    for i in main_descision.run_cycle():
        print(i)

Way 3 :
    list(main_descision.run_cycle())
"""

list(main_descision.run_cycle())
