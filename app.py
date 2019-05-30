def fn(firstName, lastName, canVote=True, canDrive=True):
    print(firstName, end=" ")
    print(lastName)
    print("can vote", canVote, end=" ")
    print("can drive", canDrive)

fn('Saleel', 'Bagde')

print("---------------------------")
fn(lastName='Patil', firstName='Nitish')

print("---------------------------")
fn('Sharmin', lastName='Bagde')

fn('Vrushali', 'Bagde', False, False)
