DEFAULT_INVITEES_PATH="./Input/Names/invited_names.txt"
DEFAULT_LETTER_PATH="./Input/Letters/starting_letter.txt"
DEFAULT_OUTPUT_PATH="./Output/ReadyToSend/"

def invitee_parser(filepath:str=DEFAULT_INVITEES_PATH)-> list:
    """
    Parses a filepath that contains a list of invitees.
    The invitee list must be constructed as follows:

        <name>\n
        <name_2>\n
        .
        .
        .
        <name_n>\n

    Args:
        filepath (str, optional): Filepath to a letter to parse, defaults to default letter path.

    Returns:
        list: A list of invitees

        Sample input (a new line is omitted but present at end of each line):
        Aang
        Zuko
        Appa

        Sample output: ['Aang', 'Zuko', 'Appa']
    """
    
    with open(filepath, 'r') as f:
        invitees = f.readlines()
    
    invitees_parsed = []
    for invitee in invitees:
        invitees_parsed.append(invitee.strip())

    return invitees_parsed


def invitation_raw_constructor(invitees:list, letter:str=DEFAULT_LETTER_PATH) -> dict:
    """
    Writes to the Output (ReadyToSend) folder with the
    invitations.
    
    The letter must include a [ ] where you will insert the name,
    for example:
        
        Hello [ ],
            ...
        Thanks again and hope to meet you soon, [ ].

        - Diego

    Args:
        invitees (list): A list of invitees
        letter (str, optional): An optional filepath for the letter to parse

    Returns:
        (dict): A dict containing a list of lines for the invitation
    """
    with open(letter, 'r') as f:
        lines = f.readlines()
    invitations = {}
    for invitee in invitees:
        invitation = []
        for line in lines:
            invitation.append(line.replace("[name]", invitee))
        invitations[invitee] = invitation
    return invitations


def invitation_constructor(invitations:dict, output_filepath:str=DEFAULT_OUTPUT_PATH) -> None:
    """
    Saves the invitations on a filepath, defaults to "Output",
    each containing the name of the invitee as the filename

    Ex: diego.txt

    Args:
        invitations (list): A raw construction of invitations given by invitation_raw_constructor
    """
    for invitee, invitation  in invitations.items():    
        path = output_filepath + invitee + ".txt"
        with open(path, 'w') as f:
            for line in invitation:
                f.write(line)


if __name__ == '__main__':
    invitees = invitee_parser()
    raw_invites = invitation_raw_constructor(invitees)
    invitation_constructor(raw_invites)
