# GPIO(dac, GPIO.OUT, initial = GPIO.LOW)
# GPIO(led, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def acp():
    b = 0
    while b < 250:
        ar = [0, 0, 0, 0, 0, 0, 0, 0]
        b = 0
        c = 0
        for i in range(8):
            c += 2 ** (7 - i)
            signal = binary2decimal(c)

            compValue = GPIO.input(comp)
            time.sleep(0.001)

            if compValue == 0:
                ar[i] = 1
                c -= 2 ** (7 - i)
            else:
                ar[i] = 1
                b += 2 ** (7 - i)
        V = b / 256 * 3.3
        print("Digital Value : {}, input Value = {:.2f}".format(b, V))
        mas.append(b)

    GPIO.output(troyka, 0)
    while b > 0:
        ar = [0, 0, 0, 0, 0, 0, 0, 0]
        b = 0
        c = 0

        for i in range(8):
            c += 2 ** (7 - i)
            signal = binary2decimal(c)
            compValue = GPIO.input(4)
            time.sleep(0.001)

            if compValue == 0:
                ar[i] = 0
                c -= 2 ** (7 - i)
            else:
                ar[i] = 1
                b += 2 ** (7 - i)
        V = b / 256 * 3.3
        print("Digital Value : {}, input Value = {:.2f}".format(b, V))
        mas.append(b)


try:
    acp()
    with open("data.txt", "w") as f:
        f.write("\n".join(mas))

finally:
    mas = np.array(mas)
    plot.plot(mas)
    plot.show()
