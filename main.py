from meteor_data_class import MeteorDataEntry


def create_mass_label():
    """ creates the labels for the mass table """
    name_label_1 = 'NAME'
    mass_label = 'MASS (g)'

    print(f' ')
    print(f'{" ":<5}{name_label_1:<30}{mass_label:<30}')
    print(f'===============================================')


def create_mass_table(target_file):
    """ filters the text file for the required mass parameters """
    count_1 = 1
    meteor_mass_list = []

    for line in target_file:
        mass_list = line.split('\t')

        meteor_obj = MeteorDataEntry(*mass_list)

        if meteor_obj.mass != '' and float(meteor_obj.mass) > 2_900_000:
            print(f'{count_1:<5}{meteor_obj.name:<30}{meteor_obj.mass:<30}')
            meteor_mass_list.append(meteor_obj)
            count_1 += 1


def create_year_label():
    """ creates the labels for the year table """
    name_label_2 = 'NAME'
    year_label = 'YEAR'

    print(f' ')
    print(f'{" ":<5}{name_label_2:<30}{year_label:<30}')
    print(f'===============================================')


def create_year_tabel(target_file):
    """ filters the text file for the required year parameters """
    count_2 = 1
    meteor_year_list = []

    for line in target_file:
        year_list = line.split('\t')

        meteor_obj = MeteorDataEntry(*year_list)

        if meteor_obj.year != '' and 2013 <= int(meteor_obj.year) <= 2024:
            print(f'{count_2:<5}{meteor_obj.name:<30}{meteor_obj.year:<30}')
            meteor_year_list.append(meteor_obj)
            count_2 += 1


def main():
    """ executes functions """
    try:
        target_file = open("meteorite_landings_data.txt")
        target_file.readline()
    except IOError:
        print("Error")
        return None
    create_mass_label()
    create_mass_table(target_file)
    target_file.close()
    try:
        target_file = open("meteorite_landings_data.txt")
        target_file.readline()
    except IOError:
        print("Error")
        return None
    create_year_label()
    create_year_tabel(target_file)
    target_file.close()


if __name__ == '__main__':
    main()
