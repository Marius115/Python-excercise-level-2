# Your code goes here:
def render_person(name, bod, eye, age, gender):
    sentence = f'{name} is a {age} years old {gender} born in {bod} with {eye} eyes'
    return sentence


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))