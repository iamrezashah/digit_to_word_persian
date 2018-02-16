digit = input('لطفا یک عدد وارد کنید: \n');

# to remove additional spaces (because we just want numbers)
digit = digit.strip()

digits_string = '0123456789';
digits_word_1 = ('صفر','یک','دو','سه','چهار','پنج','شش','هفت','هشت','نه');
digits_word_10 = ('','','بیست','سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود');
digits_word_100 = ('','صد','دویست','سیصد','چهارصد','پانصد','ششصد','هفتصد','هشتصد','نه صد');
digits_word_1000 = ('','یک هزار','دو هزار','سه هزار','چهار هزار','پنج هزار',
                    'شش هزار', 'هفت هزار','هشت هزار','نه هزار');
digits_word_10000 = ('','','بیست','سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود');
digits_word_100000 = ('','صد','دویست','سیصد','چهارصد','پانصد','ششصد','هفتصد','هشتصد','نه صد');

digits_word_1000000 = ('','یک میلیون','دو میلیون','سه میلیون','چهار میلیون','پنج میلیون',
                       'شش میلیون', 'هفت میلیون','هشت میلیون','نه میلیون');
digits_word_10000000 = ('','','بیست','سی','چهل','پنجاه','شصت','هفتاد','هشتاد','نود');
digits_word_100000000 = ('','صد','دویست','سیصد','چهارصد','پانصد','ششصد','هفتصد','هشتصد','نه صد');

digits_word_1000000000 = ('','یک میلیارد','دو میلیارد','سه میلیارد','چهار میلیارد','پنج میلیارد',
                          'شش میلیارد', 'هفت میلیارد','هشت میلیارد','نه میلیارد');


digits_words = (digits_word_1,
                digits_word_10,
                digits_word_100,
                digits_word_1000,
                digits_word_10000,
                digits_word_100000,
                digits_word_1000000,
                digits_word_10000000,
                digits_word_100000000,
                digits_word_1000000000);

result_list = []

for i in range(len(digit)):
    digits_word = digits_words[i]
    digit_index = digits_string.index(digit[-(i+1)])

    # making result's words list
    result_list.insert(i, digits_word[digit_index])

result = ' و '.join(result_list[::-1])
print(result)
# akbarzadeh's brother : 09126670051