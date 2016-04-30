using System;
using System.Text.RegularExpressions;


namespace Exercism
{
    public class PhoneNumber
    {
        public string Number { get; private set; }

        string _areaCode;
        public string AreaCode
        {
            get { return Number.Substring(0, 3); }
        }

        string _firstPart
        {
            get { return Number.Substring(3, 3); }
        }

        string _secondPart
        {
            get { return Number.Substring(6, 4); }
        }


        public PhoneNumber(string number)
        {
            var nonDigit = new Regex("[^\\d]");
            var digits = nonDigit.Replace(number, "");
            var invalid = "0000000000";

            if (digits.Length == 10) {
                Number = digits;
            } else if (digits.Length == 11 && digits[0] == '1') {
                Number = digits.Substring(1, 10);
            } else {
                Number = invalid;
            }
        }

        public override string ToString()
        {
            return String.Format("({0}) {1}-{2}", AreaCode, _firstPart, _secondPart);
        }
    }
}
