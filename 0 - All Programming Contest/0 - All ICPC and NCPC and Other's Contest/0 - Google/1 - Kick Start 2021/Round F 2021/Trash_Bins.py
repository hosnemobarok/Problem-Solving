# Problem link: --> https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435bae/0000000000887c32

def Solution():

    t = int(input())
    for case in range(1, t+1):
        size = int(input())
        st = input()

        if "0" not in st:
            print("Case #%d: %d" % (case, 0))

        elif st[0] == "0" and st[-1] == "1":
            OneF = st.find("1")
            OneSum = OneF * (OneF + 1) // 2

            Str = st[OneF:]
            zSt = ""
            for i in Str:
                if i == "1":
                    zSt += " "
                else:
                    zSt += i
            zSp = zSt.split()
            res = 0
            for i in range(len(zSp)):
                s = zSp[i].count("0")
                String = zSp[i]
                mid = s // 2

                leftS = String[:mid]
                rightS = String[mid:]
                lnTh = len(leftS) * (len(leftS) + 1) // 2
                rnTh = len(rightS) * (len(rightS) + 1) // 2

                res += lnTh
                res += rnTh
            sl = res + OneSum
            print("Case #%d: %d" % (case, sl))



        elif st[0] == "1" and st[-1] == "1":
            zSt = ""
            for i in st:
                if i == "1":
                    zSt += " "
                else:
                    zSt += i
            zSp = zSt.split()
            res = 0
            for i in range(len(zSp)):
                s = zSp[i].count("0")
                String = zSp[i]
                mid = s // 2

                leftS = String[:mid]
                rightS = String[mid:]
                lnTh = len(leftS) * (len(leftS) + 1) // 2
                rnTh = len(rightS) * (len(rightS) + 1) // 2

                res += lnTh
                res += rnTh
            print("Case #%d: %d"%(case, res))

        else:
            leftZero = st.find("1")
            rightZero = st[::-1].find("1")

            lZeroSum = leftZero*(leftZero+1) // 2
            rZeroSum = rightZero*(rightZero+1) // 2
            lrTotalZero = lZeroSum + rZeroSum

            leftS = st[leftZero:]

            mainString = leftS[:-rightZero]

            mString = ""
            for i in mainString:
                if i == "1":
                    mString += " "
                else:
                    mString += i

            mSpl = mString.split()
            res = 0
            for i in range(len(mSpl)):
                s = mSpl[i].count("0")
                String = mSpl[i]
                mid = s // 2

                leftS = String[:mid]
                rightS = String[mid:]
                lnTh = len(leftS) * (len(leftS) + 1) // 2
                rnTh = len(rightS) * (len(rightS) + 1) // 2

                res += lnTh
                res += rnTh

            solve = res + lrTotalZero
            print("Case #%d: %d" % (case, solve))

Solution()
