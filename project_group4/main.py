## This is our main file, where solutions are printed to the text file.

# Import modules
import cash_on_hand,overheads,profit_loss

# Call with module.function()
def main():
    
    overheads.highest_overhead_amt()
    profit_loss.net_profit_diff()
    cash_on_hand.COH_diff()
    
    
    

# Will print out the summary report text file, consolidating everything.
main()
