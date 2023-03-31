
def inverse(string):
    """
    Inverse une chaîne de caractères en utilisant une fonction récursive.
    Args:
        string (str): une chaîne de caractères à inverser
    Returns:
        str: la chaîne de caractères inversée
    """
    # cas de base: si la chaîne est de longueur 1, retourner la chaîne
    if len(string) == 1:
        return string
    else:
        # retourner le dernier caractère de la chaîne concaténé au résultat de l'appel récursif
        return string[-1] + inverse(string[:-1])


# def main
if __name__ == "__main__":
    string_to_inverse = input("Enter a string to inverse: ")
    print(inverse(string_to_inverse))
