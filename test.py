import locale
from dialog import Dialog

# This is almost always a good thing to do at the beginning of your programs.
locale.setlocale(locale.LC_ALL, '')

# You may want to use 'autowidgetsize=True' here (requires pythondialog >= 3.1)
d = Dialog(dialog="dialog")
# For older versions, you can use:
#   d.add_persistent_args(["--backtitle", "My little program"])

# In pythondialog 3.x, you can compare the return code to d.OK, Dialog.OK or
# "ok" (same object). In pythondialog 2.x, you have to use d.DIALOG_OK, which
# is deprecated since version 3.0.0.
if d.yesno("Are you REALLY sure you want to see this?") == d.DIALOG_OK:
    d.msgbox("You have been warned...")

    # We could put non-empty items here (not only the tag for each entry)
    code, tags = d.checklist("What sandwich toppings do you like?",
                             choices=[("Catsup", "", 0),
                                      ("Mustard", "", 0),
                                      ("Pesto", "", 0),
                                      ("Mayonnaise", "", 1),
                                      ("Horse radish","", 1),
                                      ("Sun-dried tomatoes", "", 1)],cs
                             title="Do you prefer ham or spam?",
                             backtitle="And now, for something "
                             "completely different...")
    if code == d.DIALOG_OK:
        # 'tags' now contains a list of the toppings chosen by the user
        pass
else:
    code, tag = d.menu("OK, then you have two options:",
                       choices=[("(1)", "Leave this fascinating example"),
                                ("(2)", "Leave this fascinating example")])
    if code == d.DIALOG_OK:
        # 'tag' is now either "(1)" or "(2)"
        pass
