import os

if os.path.isfile('mastery.txt'):
    print('Sorry, file exists.')
else:
    with open('gimme_phi.txt', 'w') as f:
        f.write('The golden ratio is φ = ')
        f.write('{phi:.8f}'.format(phi=1.61803398875))
