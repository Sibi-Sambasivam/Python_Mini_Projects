print("Welcome to 1v1 battle\n")

choice = ""
player1Health = 1000
player2Health = 1000


player1 = input("Player 1, enter your nickname: ")
player2 = input("Player 2, enter your nickname: ")


while choice.lower() != "no":

   
    damageToPlayer2 = int(input(f"{player1}, how much damage do you want to do to {player2}? "))
    player2Health -= damageToPlayer2

   
    damageToPlayer1 = int(input(f"{player2}, how much damage do you want to do to {player1}? "))
    player1Health -= damageToPlayer1

   
    choice = input("Would you like to play again? ")


totalDamageToPlayer1 = 1000 - player1Health
totalDamageToPlayer2 = 1000 - player2Health


print(f"In total, {player1} did {totalDamageToPlayer2} damage to {player2}")
print(f"In total, {player2} did {totalDamageToPlayer1} damage to {player1}")


if totalDamageToPlayer1 > totalDamageToPlayer2:
    print(f"{player2} wins!")
elif totalDamageToPlayer2 > totalDamageToPlayer1:
    print(f"{player1} wins!")
else:
    print("It's a draw!")
