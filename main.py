from datetime import date, datetime,timedelta


def get_birthdays_per_week(users):
    print(users)
    if users==[]:
        return {}
   
    dict_birthsdays={"Monday":[], "Tuesday":[], "Wednesday":[], "Thursday":[], "Friday":[]}
    current_date = date.today() 
    current_weekday = current_date.weekday()
    for dict in users:
        for  key in dict:
            if key!='name':
                continue
            user_date=dict["birthday"].replace(year=current_date.year)
            delta_days=user_date-current_date
            birthday_weekday = user_date.strftime('%A')
            delta_days_year=dict["birthday"].replace(year=current_date.year+1)-(current_date+timedelta(days=7))
            if 8>delta_days.days>=0 or delta_days_year.days<8:
                if birthday_weekday in("Tuesday", "Wednesday", "Thursday", "Friday"):
                    print(dict['name'])
                    dict_birthsdays[birthday_weekday].append(dict['name'])
                else:
                    print(dict['name'])
                    dict_birthsdays["Monday"].append(dict['name'])
    count=0        
    new_dict_birthsdays={}              
    for i in dict_birthsdays:
        if dict_birthsdays[i]!=[]:
            new_dict_birthsdays[i]=dict_birthsdays[i]
            count+=1
    if count!=0:
        return new_dict_birthsdays
    else:
        return {}
if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        
   
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
