"""
Implementation of Penalty Management
Purpose: Manages penalty-related functionalities, such as viewing outstanding penalties and processing penalty payments.
         It interacts with the penalties and borrowings tables in our database.
"""

class PenaltyManagement:
    def __init__(self, dbConnection) -> None:
        self.conn = dbConnection
        self.cursor = self.conn.cursor()

    def managePenalties(self, userId):
        """
        Purpose: Displays outstanding penalties for the user, allows them to select a penalty, and pay it partially or in full.
        Parameter: userId: string, the ID of the user whose penalties are being managed.
        Returns: None
        """
        cursor = self.conn.cursor()

        # Display unpaid penalties
        cursor.execute('''
            SELECT pid, amount - IFNULL(paid_amount, 0) AS due_amount
            FROM penalties
            WHERE bid IN (
                SELECT bid FROM borrowings WHERE member=?
            ) AND (paid_amount IS NULL OR paid_amount < amount)
        ''', (userId,))
        penalties = cursor.fetchall()

        # Check if the user has unpaid penalties
        if not penalties:
            print("No unpaid penalties.")
            return

        # Display unpaid penalties to the user
        print("\nUnpaid Penalties:")
        for pid, due_amount in penalties:
            print(f"Penalty ID: {pid}, Due Amount: ${due_amount}")

        # Prompt user to enter a penalty ID to pay
        penaltyId = input("\nEnter Penalty ID to pay or type 'exit' to return to Menu: ")
        if penaltyId.lower() == 'exit':
            return  # User chose to exit

        # Fetch selected penalty details
        cursor.execute('SELECT amount, IFNULL(paid_amount, 0) FROM penalties WHERE pid=?', (penaltyId,))
        penalty = cursor.fetchone()
        
        if not penalty:
            print("Penalty ID not found.")
            return

        while(True):
            pay_full = input("Pay the full due amount? (y/n): ").lower()
            if pay_full == 'y':
                paymentAmount = penalty[0] - penalty[1]  # Full due amount
                break
            else:
                paymentAmount = float(input(f"Enter payment amount for Penalty with Penalty ID {penaltyId} (Max ${penalty[0] - penalty[1]}): "))
                if paymentAmount <= 0 or paymentAmount > penalty[0]:
                    print("Invalid payment amount. Transaction cancelled.")
                else:
                    break

        totalPaid = penalty[1] + paymentAmount  # Calculate total amount paid after this payment
        cursor.execute("UPDATE penalties SET paid_amount = ? WHERE pid = ?", (totalPaid, penaltyId))
        self.conn.commit()
        print(f"Payment of ${paymentAmount} processed successfully for Penalty with Penalty ID {penaltyId}. Remaining Due: ${penalty[0] - penalty[1] - paymentAmount}")