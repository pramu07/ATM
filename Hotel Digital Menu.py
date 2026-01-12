print("Please scan the QR code")
def choose_items(items):
    selected_items = []
    while True:
        for idx, item in enumerate(items, start = 1):
            print(f"{idx}. {item}")
        choice = int(input("Choose an item by number (or enter 0 to finish): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(items):
            selected_items.append(items[choice - 1])
            print(f"You selected: {items[choice - 1]}")
        else:
            print("Invalid choice, please try again.")
    return selected_items
Hotal_menu = int(input("Enter \n1.NonVeg \n2.Veg : "))
if Hotal_menu == 1:
    # NonVeg Menu
    while True:
        NonVeg_items = int(input("Enter \n1.Sea Food \n.2 Mutton \n3.Chicken : "))
        Customer_menu = []

        if NonVeg_items == 1:
            # SeaFood items
            SeaFood_items = int(input("Enter \n1.Fish Dishes \n2.Shellfish \3.Squid/Calamari : "))
            if SeaFood_items == 1:
                Fish_Dishes = ["Grilled fish (e.g., salmon, kingfish)",
                               "Fish curry",
                               "Fish fry",
                               "Fish fingers"]

                print("Fish Dishes Menu : ")
                selected_items = choose_items(Fish_Dishes)
                Customer_menu.extend(selected_items)

            elif NonVeg_items == 2:
                # Shellfish items
                Shellfish = [ "Prawns (butter garlic prawns, prawn curry, prawn biryani)",
                          "Crabs (crab masala, crab soup)",
                          "Lobster (grilled, thermidor)"]

                print("Shellfish Menu : ")
                selected_items = choose_items(Shellfish)
                Customer_menu.extend(selected_items)

            elif NonVeg_items == 3:
                # Squid/Calamari items
                Squid_Calamari = ["Fried calamari",
                     "Stuffed squid",
                     "Squid curry"]

                print("Squid/Calamari menu : ")
                selected_items = choose_items(Squid_Calamari)
                Customer_menu.extend(selected_items)

        elif NonVeg_items == 2:
            # Mutton Items
            Mutton_items = int(input("Enter \n1.Starters \n2.Mutton Curries & Gravies \n3.Dry & Semi-Gravy \n4.Rice Items : "))
            if Mutton_items == 1:
                # Mutton Starters
                Mutton_Starters = ["Mutton Seekh Kebab",
                                   "Mutton Sheekh Kebab Roll",
                                   "Mutton Chops",
                                   "Mutton Tikka"]
                print("Mutton Starters : ")
                selected_items = choose_items(Mutton_Starters)
                Customer_menu.extend(selected_items)

            elif Mutton_items == 2:
                # Mutton Curries & Gravies
                Mutton_CurriesGravies = ["Mutton Curry",
                                         "Mutton Korma",
                                         "Chettinad Mutton Curry",
                                         "Mutton Nihari",
                                         "Mutton Kurma"]
                print("Mutton Curries & Gravies : ")
                selected_items = choose_items(Mutton_CurriesGravies)
                Customer_menu.extend(selected_items)

            elif Mutton_items == 3:
                # Dry & Semi-Gravy
                Dry_SemiGravy = ["Mutton Sukka (Dry)",
                                 "Mutton Pepper Fry",
                                 "Mutton Keema",
                                 "Mutton Liver Fry"]
                print("Dry & Semi-Gravy : ")
                selected_items = choose_items(Dry_SemiGravy)
                Customer_menu.extend(selected_items)

            elif Mutton_items == 4:
                # Rice Items
                Rice_Items = ["Mutton Biryani",
                              "Mutton Pulao",
                              "Keema Fried Rice"]
                print("Rice Items : ")
                selected_items = choose_items(Rice_Items)
                Customer_menu.extend(selected_items)
        elif NonVeg_items == 3:
            # Chicken
            Chicken_Items = int(input("Enter \n1."))
        else:
            print("Invalid choice, please try again.")

        Customer_Choice = int(input("Enter \n1. Choose More \n2. Exit : "))
        if Customer_Choice == 2:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break

else:
    while True:
        Veg_items = int(input("Enter \n1.Breakfast \n2.Appetizers \n3.Soups \n4.Salads \n5.Sides "
                                  "\n6.Desserts \n7.Beverages \n8.Main Courses \n9.Exit : "))
        Customer_menu = []

        if Veg_items == 1:
            # Breakfast items
            breakfast_items = [
                "Bacon and Eggs",
                "Sausage and Egg Muffin",
                "Ham and Cheese Omelette",
                "Chicken Sausage",
                "Smoked Salmon Bagel",
                "Breakfast Burrito (with bacon or sausage)",
                "Steak and Eggs",
                "Chicken and Waffles"
            ]
            print("Breakfast Menu : ")
            selected_items = choose_items(breakfast_items)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 2:
            # Appetizer items
            Appetizers = [
                "Chicken Wings",
                "Shrimp Cocktail",
                "Beef Nachos",
                "Crab Cakes",
                "Chicken Tenders",
                "Buffalo Wings",
                "Prawn Tempura",
                "Lamb Kebabs"
            ]
            print("Appetizers Menu : ")
            selected_items = choose_items(Appetizers)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 3:
            # Soup items 
            Soups = [
                "Chicken Noodle Soup",
                "Clam Chowder",
                "Beef Stew",
                "Seafood Bisque",
                "Lobster Soup",
            ]
            print("Soups menu : ")
            selected_items = choose_items(Soups)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 4:
            # Salad items 
            Salads = [
                "Caesar Salad (with chicken)",
                "Chicken Salad",
                "Tuna Salad",
                "Shrimp Salad",
                "Cobb Salad (with bacon and chicken)"
            ]
            print("Salads menu : ")
            selected_items = choose_items(Salads)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 5:
            # Side items 
            Sides = [
                "Mashed Potatoes with Gravy",
                "French Fries (served with chicken or fish)",
                "Coleslaw (with bacon bits)",
                "Rice Pilaf (with chicken or shrimp)",
                "Garlic Butter Shrimp"
            ]
            print("Sides menu : ")
            selected_items = choose_items(Sides)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 6:
            # Dessert items 
            Desserts = [
                "Fruit Tart",
                "Chocolate Mousse",
                "Cheesecake",
                "Sorbet/Ice Cream",
                "Baklava (without honey for vegan option)",
                "Rice Pudding",
                "Cheesecake (ensure no gelatin if strict non-veg)",
                "Chocolate Mousse (ensure no gelatin)",
                "Tiramisu (contains eggs)",
                "Bread Pudding (contains eggs)"
            ]
            print("Desserts menu : ")
            selected_items = choose_items(Desserts)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 7:
            # Beverage items 
            Beverages = [
                "Fruit Juices",
                "Smoothies",
                "Herbal Teas",
                "Coffee (with plant-based milk options)",
                "Mocktails",
                "Bloody Mary (contains clam juice)",
                "Milkshakes (contains dairy, eggs)"
            ]
            print("Beverages menu : ")
            selected_items = choose_items(Beverages)
            Customer_menu.extend(selected_items)

        elif Non_Veg_items == 8:
            # Main Courses items 
            Main_Courses = [
                "Grilled Chicken Breast",
                "Beef Steak",
                "Roast Lamb",
                "Grilled Salmon",
                "Chicken Curry",
                "Beef Stroganoff",
                "Fish and Chips",
                "Pork Chops",
                "Chicken Alfredo Pasta",
                "Seafood Paella"
            ]
            print("Main Courses : ")
            selected_items = choose_items(Main_Courses)
            Customer_menu.extend(selected_items)


        elif Non_Veg_items == 9:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break

        else:
            print("Invalid choice, please try again.")

        Customer_Choice = int(input("Enter \n1. Choose More \n2. Exit : "))
        if Customer_Choice == 2:
            print("Thanks for your choice")
            print("Your selected items:", Customer_menu)
            break

            # while True:
            #     Passenger_choice=input("Enter your choice (Economy class/ Business class/ First class): ").capitalize()
            #     if Passenger_choice=="Economy class":
            #         if Economy_class > 0:
            #             Economy_class -= 1
            #             ticket_price=5000
            #             if _Age_ >= 12:
            #                 ;ticket_price *= 0.5   # 50% discount
            #                 print("Booking Successful! and the ticket price is ", ticket_price)
            #             elif _Age_ <= 60:
            #                 ticket_price *= 0.8  # 20% discount
            #                 print("Booking Successful! and the ticket price is ", ticket_price)
            #         else:
            #             print("Economy class is not available now")
            #     elif Passenger_choice=="Business class":
            #         if Business_class > 0:
            #             Business_class -= 1
            #             ticket_price = 5000
            #             if _Age_ >= 12:
            #                 ticket_price *= 0.7   # 30% discount
            #                 print("Booking Successful! and the ticket price is ", ticket_price)
            #             elif _Age_ <= 60:
            #                 ticket_price *= 0.9  # 10% discount
            #                 print("Booking Successful! and the ticket price is ", ticket_price)
            #         else:
            #             print("Business class is not avalible now")
            #     else:
            #          print("Invalid class preference")