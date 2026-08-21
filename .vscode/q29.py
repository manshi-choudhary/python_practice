from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def fun():
    try :
        with(open(BASE_DIR /"f1.txt") as f1,open(BASE_DIR /"f2.txt") as f2,open(BASE_DIR /"f3.txt") as f3):
                a= f1.read()
                print(a)
                b= f2.read()
                print(b)
                c= f3.read()
                print(c)
        return


    except Exception as e:
        print(e)
        return

    finally:
         print("these were the files")

fun()
        