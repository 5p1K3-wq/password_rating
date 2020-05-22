import urwid


def has_digit(password):
    return any(letter.isdigit() for letter in password)


def has_letters(password):
    return any(not letter.isdigit() for letter in password)


def has_upper_letters(password):
    return any(letter.isupper() for letter in password)


def has_lower_letters(password):
    return any(letter.islower() for letter in password)


def has_symbols(password):
    return any(not letter.isdigit() and not letter.isalpha() for letter in password)


def doesnt_consist_of_symbols(password):
    return any(letter.isdigit() and not letter.isalpha() for letter in password)


def is_very_long(password):
    if len(password) < 12:
        return False
    return True


def on_change_password(edit, new_edit_text):
    score = 0
    password_verification = [has_digit, is_very_long, has_letters, has_upper_letters, has_lower_letters, has_symbols,
                             doesnt_consist_of_symbols]
    for checking_password in password_verification:
        if checking_password(new_edit_text):
            score += 2
    fill.set_text('Рейтинг пароля: %s' % score)


if __name__ == "__main__":
    text = urwid.Edit(u'Введите пароль: ', mask='*')
    fill = urwid.Text('')
    menu = urwid.Pile([text, fill])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(text, 'change', on_change_password)
    urwid.MainLoop(menu).run()
