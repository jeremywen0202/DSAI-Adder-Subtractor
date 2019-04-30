from keras.models import Sequential
from keras import layers
import numpy as np
from six.moves import range
import argparse
import sys 
import io
import random
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class CharacterTable(object):
    def __init__(self, chars):
        self.chars = sorted(set(chars))
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))

    def encode(self, C, num_rows):
        x = np.zeros((num_rows, len(self.chars)))
        for i, c in enumerate(C):
            x[i, self.char_indices[c]] = 1
        return x

    def decode(self, x, calc_argmax=True):
        if calc_argmax:
            x = x.argmax(axis=-1)
        return ''.join(self.indices_char[i] for i in x)

class colors:
    ok = '\033[92m'
    fail = '\033[91m'
    close = '\033[0m'

if __name__ == '__main__':
    print('')
    print('usage: python3 main.py [-t TYPE] [-d DIGITS] [-e EPOCH] [-s SIZE]')
    print('general options:')
    print('  -h, --help                 show this help message and exit')
    print('calculational options: (default: -t add)')
    print('  -t add                     addition')
    print('  -t sub                     subtraction')
    print('  -t add_sub                 addition mix with subtraction')
    print('  -t mul                     multiplication')
    print('digits: (default: -d 3)')
    print('  -d 2                       two-digits')
    print('  -d 3                       three-digits')
    print('  -d 4                       four-digits')
    print('number of epoch: (default: -e 100)')
    print('  -e 50                      50 epochs')
    print('  -e 100                     100 epochs')
    print('  -e 200                     200 epochs')
    print('number of training size: (default: -s big)')
    print('  -s small                   50000 training data')
    print('  -s big                     80000 training data')
    print('')

    parser = argparse.ArgumentParser()

    parser.add_argument('-t',
                default='add',
                dest='cal_type',
                help='calculational options: (default: add)')

    parser.add_argument('-d',
                default=3,
                type=int,
                dest='digits',
                help='number of digits: (default: 3)')

    parser.add_argument('-e',
                default=100,
                type=int,
                dest='epoch',
                help='training epoch: (default: 100)')

    parser.add_argument('-s',
                default='big',
                type=str,
                dest='size',
                help='training size: {big: 80000, small: 50000} (default: -s big)')

    args = parser.parse_args()
    cal_type = args.cal_type
    GEN_TYPE = {
        'add': '0123456789+ ',
        'sub': '0123456789- ',
        'add_sub': '0123456789+- ',
        'mul': '0123456789* ' 
    }.get(cal_type, -1)

    TRAINING_SIZE = 80000 if args.size.upper() == 'BIG' else 50000 
    DIGITS = args.digits
    REVERSE = True 
    MAXLEN = DIGITS + 1 + DIGITS
    chars = GEN_TYPE
    ctable = CharacterTable(chars)
    RNN = layers.LSTM
    HIDDEN_SIZE = 128
    BATCH_SIZE = 128
    LAYERS = 1
    epoch = args.epoch
    
    questions = []
    expected = []
    seen = set()

    operator = {
        'add': ['+'],
        'sub': ['-'],
        'add_sub': ['+', '-'],
        'mul': ['*']
    }
    ops = operator.get(cal_type, [None])

    print('Generating data...')
    while len(questions) < TRAINING_SIZE:
        f = lambda: int(''.join(np.random.choice(list('0123456789')) for i in range(np.random.randint(1, DIGITS + 1))))
        g = lambda: random.choice(ops)
        a, b, op = f(), f(), g()

        if DIGITS > 2:
            if op == '-':
                a, b = sorted((a, b), reverse=True)
            key = tuple((a, b, op))

            if key in seen:
                continue
            seen.add(key)

        if cal_type == 'add_sub':
            if op == '+':
                q = '{}+{}'.format(a,b)
                query = q + ' ' * (MAXLEN - len(q))
                ans = str(a+b)
            else: 
                q = '{}-{}'.format(a,b)
                query = q + ' ' * (MAXLEN - len(q))
                ans = str(a-b)
            ans += ' ' * (DIGITS + 1 - len(ans))
        elif cal_type == 'add':
            q = '{}+{}'.format(a,b)
            query = q + ' ' * (MAXLEN - len(q))
            ans = str(a+b)
            ans += ' ' * (DIGITS + 1 - len(ans))
        elif cal_type == 'sub':
            q = '{}-{}'.format(a, b)
            query = q + ' ' * (MAXLEN - len(q))
            ans = str(a - b)
            ans += ' ' * (DIGITS + 1 - len(ans))
        else:
            q = '{}*{}'.format(a,b)
            query = q + ' ' * (MAXLEN - len(q))
            ans = str(a*b)
            ans += ' ' * (2 * DIGITS - len(ans))

        if REVERSE:
            query = query[::-1]
        questions.append(query)
        expected.append(ans)
    print('Total questions:', len(questions))
    
    print('Vectorization...')
    x = np.zeros((len(questions), MAXLEN, len(chars)), dtype=np.bool)

    if cal_type == 'mul':
        y = np.zeros((len(questions),  DIGITS * 2, len(chars)), dtype=np.bool)
    else:
        y = np.zeros((len(questions),  DIGITS + 1, len(chars)), dtype=np.bool)
    for i, sentence in enumerate(questions):
        x[i] = ctable.encode(sentence, MAXLEN)
    if cal_type == 'mul':
        for i, sentence in enumerate(expected):
            y[i] = ctable.encode(sentence, DIGITS * 2)
    else:
        for i, sentence in enumerate(expected):
            y[i] = ctable.encode(sentence, DIGITS + 1)
    
    indices = np.arange(len(y))
    np.random.shuffle(indices)
    x = x[indices]
    y = y[indices]
    
    if args.size.upper() == 'BIG':
        train_x = x[:20000]
        train_y = y[:20000]
        test_x = x[20000:]
        test_y = y[20000:]
    else:
        train_x = x[:30000]
        train_y = y[:30000]
        test_x = x[30000:]
        test_y = y[30000:]
        
    split_at = len(train_x) - len(train_x) // 10
    (x_train, x_val) = train_x[:split_at], train_x[split_at:]
    (y_train, y_val) = train_y[:split_at], train_y[split_at:]
    
    print('Training Data:')
    print(x_train.shape)
    print(y_train.shape)
    print('Validation Data:')
    print(x_val.shape)
    print(y_val.shape)
    print('Testing Data:')
    print(test_x.shape)
    print(test_y.shape)

    print('Build model...')
    model = Sequential()
    model.add(RNN(HIDDEN_SIZE, input_shape=(MAXLEN, len(chars))))
    if cal_type=='mul':
        model.add(layers.RepeatVector(DIGITS * 2))
    else:
        model.add(layers.RepeatVector(DIGITS + 1))

    for _ in range(LAYERS):
        model.add(RNN(HIDDEN_SIZE, return_sequences=True))
    
    model.add(layers.TimeDistributed(layers.Dense(len(chars), activation='softmax')))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.summary()
    
    for iteration in range(1, epoch+1):
        print()
        print('-' * 50)
        print('Iteration', iteration)
        model.fit(x_train, y_train,
                  batch_size=BATCH_SIZE,
                  epochs=1,
                  validation_data=(x_val, y_val))
    
        for i in range(10):
            ind = np.random.randint(0, len(x_val))
            rowx, rowy = x_val[np.array([ind])], y_val[np.array([ind])]
            preds = model.predict_classes(rowx, verbose=0)
            q = ctable.decode(rowx[0])
            correct = ctable.decode(rowy[0])
            guess = ctable.decode(preds[0], calc_argmax=False)
            print('Q', q[::-1] if REVERSE else q, end=' ')
            print('T', correct, end=' ')
            if correct == guess:
                print(colors.ok + '\u2611' + colors.close, end='  ')
            else:
                print(colors.fail + '\u2612' + colors.close, end='  ')
            print(guess)
        if iteration % 5 == 0 or iteration == 1:
            test_loss, test_acc = model.evaluate(test_x, test_y, batch_size = BATCH_SIZE, verbose=False)
            print("MSG : Prediction")
            print("Testing  acc: {:.5f}, Testing  loss: {:.4f}".format(test_acc, test_loss))
