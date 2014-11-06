############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

print 'Temperiture...'
T = int(raw_input())

if T > 105 and T > 102:
    print 'go to hopitol'
if T > 102 and T >= 100:
    print 'have you been sick in the last 24 hours??? 1 = yes 2 = no'
    ans = raw_input()
    if ans == 1:
        print 'Go to hospitol'
    if ans == 2:
        print ' your good move along'

    