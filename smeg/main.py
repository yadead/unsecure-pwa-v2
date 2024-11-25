import data_handler as sanitiser
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='security_log.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s')

if __name__ == '__main__':
 
    password = 1234abcd
    try:
        print (f"The password as the byte string : {sanitiser.check_password(password).hex()} is ready to be encryted" )
    except TypeError:
        logger.error(f"Type errors for password:{password}")
        print("TypeError has been logged")
    except ValueError as inst:
        print(f"Not a valid password because it has {inst.args}.")
    except Exception as inst:
        print(f"Log as a {type(inst)}")