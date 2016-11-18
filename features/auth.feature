Feature: myflaskapp is secure in that users must log in and log out to access certain features

  Scenario: successful login
    Given myflaskapp is set up
      When we log in with "tomtom92" and "test12"
      Then we should see the alert "You are logged in."

#  Scenario: incorrect username
#    Given myflaskapp is set up
#      When we log in with "wrong_username" and "test12
#      Then we should see the alert "Username - Unknown username"
#
#  Scenario: incorrect password
#  Given myflaskapp is set up
#    When we log in with "tomtom92" and "wrong_password"
#    Then we should see the alert "Password - Invalid password"
#
#  Scenario: successful logout
#    Given myflaskapp is set up
#    When we logout
#    Then we should see the alert "You are logged out."