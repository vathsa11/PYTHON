import csv
def write(info):
        with open('student_information.csv', 'a', newline='') as csv_file:
            writer=csv.writer(csv_file)
            if csv_file.tell()==0:
                writer.writerow(['NAME', 'AGE', 'CONTACT NUMBER', 'E-MAIL ID'])
            writer.writerow(info)
if __name__=='__main__':
    n=int(input('Enter the number of students: '))
    i=1
    while i<=n:
        student_info=input('\nEnter the information for student {} in the following format (Name,Age,Contact_Number,E-mail_ID): '.format(i))
        info_list=student_info.split(',')
        print("\nEntered information:\nName: {}\nAge: {}\nContact Number: {}\nE-mail ID: {}".format(info_list[0], info_list[1], info_list[2], info_list[3]))
        choice=input('\nCheck whether the entered information correct (Y/N): ')
        if choice=='Y' or choice=='y':
            i+=1
            write(info_list)
        elif choice=='N' or choice=='n':
            print("\nPlease re-enter the correct values")
    print('\nTHANK YOU\n\t--------------------END--------------------')
