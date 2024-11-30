class UserInputValidator():
    def validate_positive_integers(self, list : list):
        self.__return_list = []
        for i in list:
            try:
                num = int(i)
                if num < 0:
                    continue
                else:
                    self.__return_list.append(num)
            except ValueError:
                continue
        self.__validation_success()
        return self.__return_list
    
    def __validation_success(self):
        print("List validated")
