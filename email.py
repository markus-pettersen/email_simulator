#An Email Simulation
class Email:
    """An email object containing four variables:
    if the email has been read, if it is spam, who sent it and the contents
    """
    # Class variables, both initialised to false:
    has_been_read = False
    is_spam = False

    def __init__(self, email_contents, from_address):
        self.from_address = from_address
        self.email_contents = email_contents
    
    def mark_as_read(self):
        """When called, this method changes the has_been_read variable to
        True
        """
        self.has_been_read = True
    
    def mark_as_spam(self):
        """When called, this method changes the is_spam variable to True"""
        self.is_spam = True

def add_email(contents, address):
    """Creates a new instance of the Email object and appends it to the
    inbox
    """
    inbox.append(Email(contents, address))

def get_count():
    """Returns the length of the inbox list (i.e. the number of emails in the
    inbox
    """
    return len(inbox)

def get_email(index):
    """Returns the contents of an email using its index in the inbox, calls
    the mark_as_read method to mark the email as read
    """
    email = inbox[index]
    email.mark_as_read()
    return email.email_contents

def get_unread_emails():
    """Iterates through all the emails in the inbox and returns a list of
    those that have not been read
    """
    unread_emails = []
    for email in inbox:
        if not email.has_been_read:
            unread_emails.append(email)
    return unread_emails

def get_spam_emails():
    """Iterates through all the emails in the inbox and returns a list of
    those that are marked as spam
    """
    spam_emails = []
    for email in inbox:
        if email.is_spam:
            spam_emails.append(email)
    return spam_emails

def delete(num):
    """Deletes the email in the inbox with the given index"""
    del inbox[num]

def read_emails():
    """The function called when the user selects read emails from the main
    menu. Here the user can scroll the emails back and forth or select a
    specific email using its index. Also can mark the currently displayed
    index as spam.
    """
    # Count is used as the index. Initialised at 0:
    count = 0
    # Loops until user returns to the main menu:
    while True:
        # Adds one to the count because lists are zero indexed and calls
        # get_count function
        print(f"Email {count + 1} of {get_count()}")
        # Get email with the count will retrieve the email from inbox:
        curr_contents = get_email(count)
        curr_email = inbox[count]
        curr_sender = curr_email.from_address
        # Prints the sender and the contents on two lines:
        print(f"From: {curr_sender}")
        print(curr_contents)
        # Submenu - User can choose from these options:
        read_choice = input('''Select option:
        Next - n            Previous - p
        Select - sel
        Mark as Spam - s
        Back to menu - b
        ''').lower()
        if read_choice == "n" and count < get_count() - 1:
            # Scroll forward. Not when on the last email.
            count += 1
        elif read_choice == "p" and count > 0:
            # Scroll backwards. Not when on the first email.
            count -= 1
        elif read_choice == "s":
            # Mark as spam. Calls the spam method on the current email.
            print("Email marked as spam")
            curr_email.mark_as_spam()
        elif read_choice == "sel":
            # User can change the 'count' variable manually by entering a
            # number:
            while True:
                # Catch errors from invalid input:
                try:
                    user_pick = int(input(f"Select email by number" \
                        f"(1 - {get_count()}): "))
                    break
                except:
                    print("Invalid input!")
            if user_pick not in range (1, get_count() + 1):
                print("No email found")
            else:
                # Changes the count to user's email. Adjusted for
                # zero-indexing
                count = user_pick - 1
                print(count)
        elif read_choice == "b":
            print("Returning to main menu...")
            return
        else: # Default case
            print("Oops, try again")

def list_unread():
    """Retrieves all the emails with a False has_been_read boolean and adds
    them to a list. Prints the length of the list and enumerates through
    the list to print the emails to the console
    """
    unread_emails = get_unread_emails()
    print(f"You have {len(unread_emails)} unread emails:")
    for index, email in enumerate(unread_emails):
        print(f"{index + 1}. {email.email_contents} from {email.from_address}")
    print()

def list_spam():
    """Retrieves all the emails with a True is_spam boolean and adds them to a
    list. Prints the length of the list and enumerates through the list to
    print the emails to the console
    """
    spam_emails = get_spam_emails()
    print(f"You have {len(spam_emails)} spam emails:")
    for index, email in enumerate(spam_emails):
        print(f"{index + 1}. {email.email_contents} from {email.from_address}")
    print()

def delete_email():
    """User can delete an email using its index in the inbox"""
    while True:
        try: # Catch invalid input here:
            delete_email = int(input(f"Select email by number (1 - {get_count()}): "))
            break
        except:
            print("Invalid input!")
    if delete_email not in range (1, get_count() + 1):
        # Check if the index is valid. 
        print("No email found")
    else:
        # Delete the email accounting for the index
        print(f"Email {delete_email} deleted!")
        delete(delete_email - 1)

def add_email_to_inbox():
    """This function is used to simulate receiving a new email.
    User can specify who the email came from and what it contains"""
    user_address = input("Enter the address: ")
    user_content = input("Enter the content: ")
    add_email(user_content, user_address)

# Main part of the program:
# Set up an inbox:
inbox = []

# Call the add_email function a few times to populate the inbox
add_email("No 1. Diet Pill", "Alpha")
add_email("Second", "Bravo")
add_email("Three available places", "Charlie")
add_email("Fourth December", "Delta")

# Loop for the menu. User can select an option or quit
while True:
    print(f"You have {get_count()} emails in your inbox")
    user_choice = input('''What would you like to do:
        Read emails - r
        List unread - un
        List spam - sp
        Delete an email - d
        Add an email to inbox - a
        Quit? - q
        ''').lower()
    if user_choice == "r":
        if get_count() > 0:
            read_emails()
        else:
            print("No emails")
    elif user_choice == "un":
        list_unread()
    elif user_choice == "sp":
        list_spam()
    elif user_choice == "d":
        delete_email()
    elif user_choice == "a":
        add_email_to_inbox()
    elif user_choice == "q":
        print("Goodbye")
        exit()
    else:
        print("Oops - incorrect input")