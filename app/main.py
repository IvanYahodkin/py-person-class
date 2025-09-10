class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for human in people:
        Person(human["name"], human["age"])

    for human in people:
        instance = Person.people[human["name"]]

        if "wife" in human and human["wife"]:
            instance.wife = Person.people[human["wife"]]

        if "husband" in human and human["husband"]:
            instance.husband = Person.people[human["husband"]]

    return list(Person.people.values())
