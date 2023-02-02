## This is our main file, where solutions are printed to the text file.

# Import modules
import cash_on_hand,overheads,profit_loss

# Call other modules cash_on_hand, overheads, profit lost with module.function()
def main():
    """
    - This function will get functions from other modules and execute
    - No parameters required.
    """
    overheads.highest_overhead_amt()
    cash_on_hand.COH_diff()
    profit_loss.net_profit_diff()
    
    
# Will print out the summary report text file, consolidating everything.
main()
