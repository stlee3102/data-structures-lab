"""Functions to parse a file containing villager data."""

filename = open("villagers.csv")

def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    species_set = set()
    for line in filename:
      line = line.rstrip()
      tokens = line.split("|")
      species = tokens[1]
      species_set.add(species)

    return species_set


def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list[list]: a list of lists
    """

    villagers = []
    for line in filename:
      line = line.rstrip()
      tokens = line.split("|")
      name = tokens[0]
      species_in_list = tokens[1]

      if species_in_list == species:
        villagers.append(name)

    return sorted(villagers)


def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.
    (Fitness, Nature, Education, Music, Fashion, and Play)

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    Fitness = []
    Nature = []
    Education = []
    Music = []
    Fashion = []
    Play = []

    big_list = [Fitness, Nature, Education, Music, Fashion, Play]
    list_of_hobbies = ["Fitness", "Nature", "Education", "Music", "Fashion", "Play"]
    
    for line in filename:
      line = line.rstrip()
      tokens = line.split("|")
      name = tokens[0]
      hobby_in_list = tokens[3]
      for i in range(len(list_of_hobbies)):
        if hobby_in_list == list_of_hobbies[i]:
          big_list[i].append(name)
    
    for hobby in big_list:
      hobby.sort()
    return big_list


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    for line in filename:
      line = line.rstrip()
      tokens = line.split("|")
      name = tokens[0]
      species = tokens[1]
      personality = tokens[2]
      hobby = tokens[3]
      motto = tokens[4]

      my_tuple = (name, species, personality, hobby, motto)
      all_data.append(my_tuple)

    return all_data





def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    for line in filename:
      line = line.rstrip()
      tokens = line.split("|")
      name_in_list = tokens[0]
      motto = tokens[4]
      if name_in_list == name:
        return motto
    
    return None



def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""

    new_set = set()
    orig_personality = None

    for line in filename:
      line = line.rstrip()
      tokens = line.split("|")
      name_in_list = tokens[0]
      personality = tokens[2]
      
      if name == name_in_list:
        orig_personality = personality
        break
    
    if orig_personality:
      for line in open("villagers.csv"):
        line = line.rstrip()
        tokens = line.split("|")
        name_in_list = tokens[0]
        print(name_in_list)
        personality = tokens[2]
        if personality == orig_personality:
          new_set.add(name_in_list)

    return new_set 

print(find_likeminded_villagers(filename, 'Curt'))
