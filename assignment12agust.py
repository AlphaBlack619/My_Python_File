class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def vat_calculator():
    try:
        price = float(input('Enter Price Sir\n'))
        vat = input('Enter VAT\n')
        p1 = float(vat[:-1])
        price2 = p1 * price/100 + price
        isfloat(p1)
        if vat[-1] != '%':
            raise CustomException("Last character must be %")
        if p1 <= 0 or price <= 0:
            raise CustomException("Operands can't be less than (OR) equals to 0")
        if type(price) == str:
            raise CustomException("Price must be float")
    except TypeError:
        print("Error: Wrong operand")
        vat_calculator()
    except IndexError:
        print("Invalid Index error")
        vat_calculator()
    except ZeroDivisionError:
        print('Invalid operand zero operations not allow')
        vat_calculator()
    except CustomException as error:
        print("Error:", str(error))
        vat_calculator()
    except KeyboardInterrupt:
        print("You Distorted the flow of the application")
        vat_calculator()
    except ValueError:
        print("Invalid value")
        vat_calculator()
    else:
        return price2


print(vat_calculator())
