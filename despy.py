from typing import Any
from exceptions import ChoiceNotFound, UnknownError, DescisionJumpError


class Descision:
    def __init__(self, choices: [list, dict], question: str = ""):
        if type(choices) == list:
            self.choices = choices
            self.descision_map = {}
        elif type(choices) == dict:
            self.choices = list(choices.keys())
            self.descision_map = choices
            for i, j in choices.items():
                j._add_to_hash(self.choices.index(i))
        else:
            raise ValueError(
                "The Value Of Choices Must Be List Or Dictionary.")
        self.question = question
        self.descision_hash = ""

        self.is_descision = True
        self.return_format = "i,t,d"  # Selected_index, Selected_text, Next Descision
        self.choosed_index = -1
        self.choosed_text = ""

    def __select_choice(self, choice_index, choice_text):
        self.choosed_index = choice_index
        self.choosed_text = choice_text

    def after(self, choice, next_descision):
        try:
            self.choices[choice]
            self.descision_map[choice] = next_descision
            next_descision._add_to_hash(choice)
        except:
            index = self.choices.index(choice)
            self.descision_map[index] = next_descision
            next_descision._add_to_hash(index)

    def _add_to_hash(self, index_to_add):
        self.descision_hash = self.descision_hash + str(index_to_add)

    def __pretty_print(self, choices):
        for c, i in enumerate(choices):
            print(c+1, "->", i)

    def __return_content(self):
        answer = []
        for i in self.return_format.split(","):
            if i == "i":
                if self.choosed_index == -1:
                    raise DescisionJumpError(
                        "You Did'nt Run This Descision and You Are Not Allowed To Execute This.")
                answer.append(self.choosed_index)
            elif i == "t":
                if self.choosed_text == "":
                    raise DescisionJumpError(
                        "You Did'nt Run This Descision and You Are Not Allowed To Execute This.")
                answer.append(self.choosed_text)
            elif i == "d":
                try:
                    answer.append(self.descision_map[self.choosed_index])
                except:
                    try:
                        answer.append(self.descision_map[self.choosed_text])
                    except:
                        answer.append(None)
        return answer

    def __call__(self):
        self.execute()

    def execute(self):
        try:
            if self.question:
                print(self.question)
            self.__pretty_print(self.choices)
            index = int(input())
            self.__select_choice(index-1, self.choices[index-1])
            return self.__return_content()
        except IndexError:
            raise ChoiceNotFound("There Is Not Such Choice.")
        except Exception as e:
            raise UnknownError(e)

    def has_next_descision(self, choice=None):
        if choice:
            try:
                self.descision_map[choice]
                return True
            except:
                return False
        else:
            if self.descision_map:
                return True
            return False

    def run_cycle(self):
        target_object = self
        while target_object.has_next_descision():
            selected_index, selected_text, target_object = target_object.execute()
            yield [selected_index, selected_text]
        target_object(True)


class FinalDescision:
    def __init__(self, text=""):
        self.text = text
        self.descision_hash = ""

    def _add_to_hash(self, index_to_add):
        self.descision_hash = self.descision_hash + str(index_to_add)

    def __call__(self, print_text=False):
        if self.text:
            if print_text:
                print(self.text)
            else:
                return self.text

    def has_next_descision(self):
        return False
