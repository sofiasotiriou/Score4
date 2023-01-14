LANG = "UTF-8"
# Ορισμός συνάρτησης η οποιά εμφανίζει το ταμπλό
def print_game(table, ColumnNumber) :
    counter = 0
    for column in zip(*table) :
        if counter == 1 :
            print((6*ColumnNumber)*"-")
        print(' '.join(column))
        counter += 1
    print((6*ColumnNumber)*"-")

#Ορισμός συνάρτησης η οποία υπολογίζει και εμφανίζει το σκορ
def Score(Pawn, Winner, Alike) :
    """
    >>>Score("X", Winner, 5)
    [0, 5]
    """
    if Pawn == "O" :
        Winner[0] += Alike
        print("Νικητής του γύρου είναι ο παίκτης 1!")
    else :
        Winner[1] += Alike
        print("Νικητής του γύρου είναι ο παίκτης 2!")
    print("Το Σκορ είναι:", Winner[0], "-", Winner[1])
    print("")
    return Winner

#Ορισμός συνάρτησης η οποία μετατρέπει μια τετράδα σε αστεράκια και ολίσθηση προς τα κάτω των πιονιών
def Vanish(ColCount, table):
    for i in range(1, ColumnNumber+1) :
        for j in range(ColCount[i], 9) :
            if table[i][j] ==  "   *|" :
                for l in range(j, ColCount[i]-1, -1) : 
                    if l == 1 :
                        table[i][l] = "    |"
                    else :
                        table[i][l] = table[i][l-1]
                ColCount[i] += 1
    return table, ColCount   

print ("Καλωσήλθατε στο παιχνίδι!")
choice =input("Επιθυμείτε νέο παιχνίδι (Ν) ή φόρτωση παιχνιδιού από αρχείο (S); ")
Winner = [0, 0]
if choice == "N" :
    ColumnNumber = int(input("Δώστε αριθμό στηλών παιχνιδιού (5-10): "))
    #Δημιουργία του άδειου ταμπλό σε περίπτωση νέου παιχνιδιού
    l0 = [" "]
    for i in range(65, 73) :
        l0.append(chr(i)+"|")
    table = [l0]
    for j in range(1, ColumnNumber+1) :
        list = ["  "+str(j)+"  "]
        for k in range(1, 9) :
                list.append("    |")
        table.append(list)
    #Δημιουργία των μετρητών που αντιπροσωπεύουν τη σειρα στην οποία βρίσκεται το πανώ πάω πιόνι σε κάθε στήλη
    ColCount = [-1]
    for a in range(1, ColumnNumber+1) :
        ColCount.append(9)
    print_game(table, ColumnNumber)

elif choice == "S" :
    #Άνοιγμα αρχείου csv
    FileOpen = input("Ποιό είναι το όνομα του αρχείου΄;")
    import csv
    F = open(FileOpen,"r") 
    CSVfile = csv.reader(F, delimiter=";")
    #Μετατροπή του csv αρχείου σε πίνακα
    rows = []
    RowNumber = 0
    for row in CSVfile:
        rows.append(row)
        if RowNumber == 0  : 
            ColumnNumber = row[0].count(",") + 1 
            FullColumn = len(row[0]) 
        RowNumber += 1
    #Δημιουργία ενός άδειου ταμπλό
    l0 = [" "]
    for i in range(65, 73) :
        l0.append(chr(i)+"|")   
    table = [l0]
    for j in range(1, ColumnNumber+1) :
        list = ["  "+str(j)+"  "]
        for k in range(1, 9) :
                list.append("    |")
        table.append(list)
    #Δημιουργία του ταμπλό όπως αυτό είχε αποθηκευτεί στο αρχείο csv
    row = 1
    for i in range(0, 8) :
        Column = 1
        for j in range(0, FullColumn) :
            if rows[i][0][j] == "0" :
                table[Column][row] = "    |"
                Column += 1
            elif rows[i][0][j] == "1" :
                table[Column][row] = "   O|"
                Column += 1
            elif rows[i][0][j] == "2" :
                table[Column][row] = "   X|"
                Column += 1
        row += 1  
    #Μεταφορά του σκορ απο το αρχείο csv
    Winner[0] = int(rows[8][0][0])
    Winner[1] = int(rows[8][0][2])
    #Δημιουργία των μετρητών που αντιπροσωπεύουν τη σειρα στην οποία βρίσκεται το πανώ πάω πιόνι σε κάθε στήλη
    ColCount = [-1]
    for i in range(1, ColumnNumber+1) :
        c = 9
        for j in range(1,9) :
            if table[i][j] ==  "   O|" or table[i][j] ==  "   X|" :
                c -= 1
        ColCount.append(c)
    print_game(table, ColumnNumber)
    print("Το Σκορ είναι: ",Winner[0],"-",Winner[1])

counter2 = 1
Answer = " "
flag = False
#Ξεκίνημα του νέου γύρου
while Answer != 's' :
    if counter2 == 1 :
        Col = int(input("Παίκτης 1: Επέλεξε στήλη για το πιόνι σου:"))
        Pawn = "O"
        counter2 += 1
    else :
        Col = int(input("Παίκτης 2: Επέλεξε στήλη για το πιόνι σου:"))
        Pawn = "X"
        counter2 -= 1
    while Col > ColumnNumber or Col < 1 :
        print("Δεν υπάρχει η στήλη", Col )
        Col = int(input("Δώστε νέο αριθμό στήλης."))
    while ColCount[Col] == 1 :
        print("H  στήλη",Col,  "είναι γεμάτη")
        Col = int(input("Δώστε νέο αριθμό στήλης"))
    ColCount[Col] -= 1
    S = ColCount[Col]
    table[Col][S] = "   "+Pawn+"|"
#Οριζόντιος έλεγχος
    AlikeHor = 1     
    AlikePosHor = 1
    ca = 2
    while ca <= ColumnNumber :
        if table[ca][S] == table[ca-1][S] and table[ca][S] != "    |" :
            AlikeHor += 1
            AlikePosHor += 1
        else:
            if AlikeHor< 4 :
                AlikeHor = 1
                AlikePosHor = ca
        ca += 1
    if AlikeHor >= 4 :
        flag = True
        parameter = AlikeHor
        while AlikeHor > 0 :  
            table[AlikePosHor][S] =  "   *|"
            AlikePosHor -= 1
            AlikeHor -= 1
#Κάθετος Έλεγχος  
    Vert = False
    if ColCount[Col]+3 <= 8 :       
        if table[Col][S] == table[Col][S+1] and table[Col][S] != "    |"   :
            if table[Col][S] == table[Col][S+2] :
                if table[Col][S] == table[Col][S+3] :
                    flag = True
                    Vert = True
                    table[Col][S] = "   *|"
                    table[Col][S+1] = "   *|"
                    table[Col][S+2] = "   *|"
                    table[Col][S+3] = "   *|"
                    print_game(table, ColumnNumber) 
                    print("")
                    table[Col][S] = "    |"
                    table[Col][S+1] = "    |"
                    table[Col][S+2] = "    |"
                    table[Col][S+3] = "    |"
                    parameter = 4
                    print_game(table, ColumnNumber)
                    ColCount[Col] += 4
#Διαγώνιος έλεγχος 1
    if Vert != True :
        i = Col 
        j = ColCount[Col]
        flag1 = True 
        while  i-1 >= 1 and j-1 >= 1 and flag1 == True : 
            if table[i][j] == table[i-1][j-1] :
                i -= 1 
                j -= 1 
            else:
                flag1 = False 
        c1 = 1
        flag2 = True
        while i+1 <= ColumnNumber and j+1 <= 8  and flag2 == True: 
            if table[i][j] == table[i+1][j+1] :
                c1 += 1
                i += 1 
                j += 1
            else:
                flag2 = False 
        alikeDiag1 = c1
        if alikeDiag1 >= 4:
            flag = True
            parameter =  alikeDiag1
            while alikeDiag1 > 0:
                    table[i][j] =  "   *|"
                    i -= 1
                    j -= 1
                    alikeDiag1 -= 1
#Διαγώνιος Έλεγχος 2
        i = Col 
        j = ColCount[Col]
        flag3 = True 
        while i+1 <= ColumnNumber and j-1 >= 1  and flag3 == True :
            if table[i][j] == table[i+1][j-1]  :
                i += 1 
                j -= 1 
            else:
                flag3 = False 
        c2 = 1
        flag4 = True
        while i-1 >=1 and j+1 <= 8 and flag4 == True :
            if table[i][j] == table[i-1][j+1]  :
                c2 += 1
                i -= 1 
                j += 1
            else:
                flag4 = False 
        alikeDiag2 = c2
        if alikeDiag2 >= 4:
            flag = True
            parameter =  alikeDiag2
            while alikeDiag2 > 0 :
                    table[i][j] =  "   *|"
                    i += 1
                    j -= 1
                    alikeDiag2 -= 1
#Εμφάνιση του πίνακα σε περίπτωση νίκης πριν και μετά τη μετατροπή σε αστεράκια και την ολίσθηση προς τα κάτω 
    if flag == True  :
        if Vert == False :
            print_game(table, ColumnNumber) 
            Vanish(ColCount, table)
            print("")
            print_game(table, ColumnNumber)
        Score(Pawn, Winner, parameter)
    else :
        print_game(table, ColumnNumber)
    
    while flag == True :   
        flag = False 
#Οριζόντιος έλεγχος σε περίπτωση δημιουργίας τετράδας κατά την ολίσθηση προς τα κάτω 
        for l in range(1,9):
            for k in range(2,ColumnNumber+1):
                AlikeHor = 1     
                AlikePosHor = 1
                if table[k][l] == table[k-1][l] and table[k][l] != "    |" :
                    AlikeHor += 1
                    AlikePosHor += 1
                else:
                    if AlikeHor< 4 :
                        AlikeHor = 1
                        AlikePosHor = k
            if AlikeHor >= 4 :
                flag = True
                parameter = AlikeHor
                Pawn2 = table[AlikePosHor][l]
                while AlikeHor > 0 :  
                    table[AlikePosHor][l] =  "   *|"
                    AlikePosHor -= 1
                    AlikeHor -= 1
        Vert = False       
#Κάθετος έλεγχος σε περίπτωση δημιουργίας τετράδας κατά την ολίσθηση προς τα κάτω 
        AlikeVert = 0
        PosLast = 3
        Vert = False
        for j in range(1, ColumnNumber) :
            for i in range(1, 8) :
                if table[j][i] == table[j][i+1] and table[j][i] != "    |" :
                    AlikeVert += 1
                    PosLast += 1 
                    Column = j
                else :
                    AlikeVert = 1
                    PosLast = i + 1 
            if AlikeVert >= 4 :
                Pawn2 = table[Column][PosLast]
                parameter = AlikeVert
                flag = True
                Vert = True 
                for j in range(PosLast, PosLast - AlikeVert, -1) :
                    table[Column][j] = "   *|"
                print_game(table, ColumnNumber)
                for j in range(8, 4, -1) :
                    table[Column][j] = table[Column][j-4]
                    table[Column][j-4] = "    |"
                ColCount[Column] = ColCount[Column] + 4
                print("")
                print_game(table, ColumnNumber)
#Διαγώνιος έλεγχος 1 σε περίπτωση δημιουργίας τετράδας κατά την ολίσθηση προς τα κάτω 
        if Vert != True :
            alikeDiag = 1
            for k in range (1, ColumnNumber+1) :
                st = k
                line = 1
                while line < 8 and st< ColumnNumber :
                    if table[st][line] == table[st+1][line+1] and table[st][line] != "    |" :
                        st += 1
                        line += 1
                        alikeDiag += 1
                    else:
                        if alikeDiag < 4:
                            alikeDiag = 1
                            st += 1
                            line +=1
                if alikeDiag >= 4 : 
                    flag = True 
                    parameter = alikeDiag
                    Pawn2 = table[st][line]
                    while alikeDiag > 0 :
                        table[st][line] = "   *|"
                        st -= 1
                        line -= 1
                        alikeDiag -= 1
            alikeDiag = 1
            for k in range (2, 9) :
                st = 1
                line = k
                while line < 8 and st < ColumnNumber :
                    if table[st][line] == table[st+1][line+1] and table[st][line] != "    |" :
                        st += 1
                        line += 1
                        alikeDiag += 1
                    else:
                        if alikeDiag < 4:
                            alikeDiag = 1
                            st += 1
                            line +=1
                if alikeDiag >= 4 :
                    flag = True 
                    parameter = alikeDiag
                    Pawn2 = table[st][line]
                    while alikeDiag > 0 :
                        table[st][line] = "   *|"
                        st -= 1
                        line -= 1
                        alikeDiag -= 1
#Διαγώνιος έλεγχος 2 σε περίπτωση δημιουργίας τετράδας κατά την ολίσθηση προς τα κάτω 
            alikeDiag = 1
            for k in range (1 , ColumnNumber+1):
                st = k
                line = 1
                while st < ColumnNumber  and line < 8:
                    if table[st][line] == table[st-1][line+1] and table[st][line] != "    |" :
                        st -= 1
                        line += 1
                        alikeDiag += 1
                    else:
                        if alikeDiag < 4:
                            alikeDiag = 1
                            st -= 1
                            line +=1
                if alikeDiag >= 4 :
                    flag = True 
                    parameter = alikeDiag
                    Pawn2 = table[st][line]
                    while alikeDiag> 0 :
                        table[st][line] = "   *|"
                        st += 1
                        line -= 1
                        alikeDiag -= 1
            alikeDiag = 1
            for k in range (2 ,9) :
                st = ColumnNumber
                line = k
                while st > 1  and line < 8:
                    if table[st][line] == table[st-1][line+1] and table[st][line] != "    |" :
                        st -= 1
                        line += 1
                        alikeDiag += 1
                    else:
                        if alikeDiag < 4:
                            alikeDiag = 1
                            st -= 1
                            line +=1
                if alikeDiag >= 4 :
                    flag = True 
                    parameter = alikeDiag
                    Pawn2 = table[st][line]
                    while alikeDiag> 0 :
                        table[st][line] = "   *|"
                        st += 1
                        line -= 1
                        alikeDiag -= 1
#Εμφάνιση του πίνακα και δημιουργία αστεριών σε περίπτωση δημιουργίας τετράδας κατά την ολίσθηση προς τα κάτω 
        if flag == True  :
            if Vert == False :
                print_game(table, ColumnNumber) 
                Vanish(ColCount, table)
                print("")
                print_game(table, ColumnNumber)
        print("Βρέθηκαν κι άλλα συνεχόμενα πιόνια!")
        if Pawn2 == "   O|" :
            Winner[0] += parameter 
            print("Ο παίκτης 1 πήρε άλλους:", parameter, "πόντους!")
        else :
            Winner[1] += parameter
            print("Ο παίκτης 2 πήρε άλλους:", parameter, "πόντους!")
        print("Το Σκορ είναι:", Winner[0], "-", Winner[1])
        print("")
        flag= False
#Περίπτωση γεμάτου ταμπλό
    FullBoard = True
    for i in range(1, ColumnNumber+1) :
        if ColCount[i] != 1 :
            FullBoard = False
    if FullBoard :
        if Winner[0] > Winner[1] :
            print("Το ταμπλό γέμισε. Νικητής του παιχνιδιού είναι ο παίκτης 1!")
        elif Winner[1] > Winner[0] :
            print("Το ταμπλό γέμισε. Νικητής του παιχνιδιού είναι ο παίκτης 2!")
        elif Winner[0] == Winner[1] :
            print("Το ταμπλό γέμισε και δεν υπάρχει νικητής!")
    if counter2 == 1 :
        Answer = input(str('Πατηστε οποιοδήποτε πλήκτρο για να συνεχίσετε.\nΓια παύση του παιχνιδιού και αποθήκευση του αρχείου επιλέξτε "s": '))
        if Answer != "s": 
#Δημιουργία άδειου ταμπλό σε περίπτωση που γεμίσει αλλά οι παίκτες θέλουν να συνεχίσουν το παιχνίδι
            if FullBoard :
                ColumnNumber = int(input("Δώσε αριθμό στηλών παιχνιδιού (5-10): "))
                l0 = [" ", ]
                for i in range(65, 73) :
                    l0.append(chr(i)+"|")
                table = [l0]
                for j in range(1, ColumnNumber+1) :
                    list = ["  "+str(j)+"  "]
                    for k in range(1, 9) :
                            list.append("    |")
                    table.append(list)
                print_game(table, ColumnNumber)
        else :
#Αποθήκευση του παιχνιδιού σε περίπτωση που οι παίκτες θέλουν να το διακόψουν 
            import csv
            FileName = input("Δωστε όνομα αρχείου: ")
            TableCSV = []
            for i in range(1, 9): 
                list = []
                for j in range(1, ColumnNumber+1):
                    if table[j][i]== "    |" :
                        list.append(0)
                    elif table[j][i] == "   O|" :
                        list.append(1)
                    else :
                        list.append(2)
                TableCSV.append(list)
            TableCSV.append(Winner)
            with open(FileName, 'w+', newline="") as File :
                csvwriter = csv.writer(File)
                csvwriter.writerows(TableCSV)
            print("Το παιχνίδι αποθηκεύτηκε!")