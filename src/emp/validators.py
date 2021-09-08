from django.core.exceptions import ValidationError

def validate_employID(value):
    x = str(value)
    if len(x) == 4:
        return value
    raise ValidationError('Employ ID must be 4 digit and should start with 10')

def validate_fname(value):
    return value.title()

def validate_lname(value):
    return value.title()

def validate_fladdraEmail(value):
    mail = str(value)
    if mail.endswith('@fladdra.com'):
        return value
    raise ValidationError("Fladdra Email must end with '@fladdra.com'")

def validate_mobile(value):
    if len(str(value)) != 10:
        raise ValidationError('Mobile number must be 10 digit!')
    else:
        return value

def validate_position(value):
    pos_list = ['Intern', 'Senior Developer', 'Junior Developer', 'HR', '-', 'Test']
    if value in pos_list:
        return value.title()
    else:
        raise ValidationError('This position is not valid!')

