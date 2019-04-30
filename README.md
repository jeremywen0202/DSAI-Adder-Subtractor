# DSAI Adder & Subtractor

## Prerequisite
- Python 3.6.7

## Install Dependency
```
$ pip install -r requirements.txt
```

## Usage
```
$ python3 main.py [-t TYPE] [-d DIGITS] [-e EPOCH] [-s SIZE]
```

|                            | Description                                    |
| ---                        | ---                                            |
| **General Options**        |                                                |
| -h, --help                 | show this help message and exit                |
| **Calculational Options**  | **Default `-t add`**                          |
| -t add                     | addition                                      |
| -t sub                     | subtraction                                    |
| -t add_sub                 | addition & subtraction                        |
| -t mul                     | multiplication                                |
| **Number of Digits**       | **Default `-d 3`**                            |
| -d 2                       | 2 digits                                      |
| -d 3                       | 3 digits                                      |
| -d 4                       | 4 digits                                      |
| **Number of epoches**      | **Default `-e 100`** 
| -e 50                      | 50  epoches
| -e 100                     | 100 epoches
| -e 200                     | 200 epoches
| **Number of training size**| **Default `-s big`**
| -s big                     | 80000 training data
| -s small                   | 50000 training data

## Model Information

| **Layer (type)**           | Output Shape                 | Param #
|    ---                     |    ---                       |    ---
| lstm_1 (LSTM)              | (None, 128)                  |  72192 
| repeat_vector_1            | (RepeatVecto (None, 5, 128)  | 0
| lstm_2 (LSTM)              | (None, 5, 128)               | 131584
| time_distributed_1         | (TimeDist (None, 5, 12)      | 1548
| Total params: 205,324      |                              |
| Trainable params: 205,324  |                              |
| Non-trainable params: 0    |                              |


## Result

這邊分成兩個部份來分析：
 - 第一個部份分析不同的calculation type: addition、subtraction、addition & subtraction、multiplication，並分兩種data size訓練：
   
   - Big data set: Training data : 18000, Validation data: 2000, Testing data: 60000
   - Small data set: Training data : 27000, Validation data: 3000, Testing data: 20000

 - 第二個部份比較不同的digits的準確度差異(e.g. 2 digits、3 digits、4 digits)

## First part: 3 digits with different calculation type and data sets

### Addition:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py
```
 - **Experiment result**
```
Iteration 1
Q 1+52    T 53   ☒  12  
Q 79+5    T 84   ☒  12  
Q 773+82  T 855  ☒  110 
Q 145+582 T 727  ☒  110 
Q 6+779   T 785  ☒  100 
Q 548+77  T 625  ☒  110 
Q 82+142  T 224  ☒  100 
Q 44+148  T 192  ☒  110 
Q 247+45  T 292  ☒  110 
Q 900+67  T 967  ☒  110 
MSG : Prediction
Testing  acc: 0.33954, Testing  loss: 1.8321
...
Iteration 50
Q 74+606  T 680  ☑  680 
Q 526+524 T 1050 ☑  1050
Q 74+606  T 680  ☑  680 
Q 681+0   T 681  ☑  681 
Q 55+463  T 518  ☑  518 
Q 165+717 T 882  ☑  882 
Q 32+13   T 45   ☑  45  
Q 44+72   T 116  ☑  116 
Q 10+301  T 311  ☑  311 
Q 63+717  T 780  ☑  780 
MSG : Prediction
Testing  acc: 0.98303, Testing  loss: 0.0772
...
Iteration 100
Q 54+99   T 153  ☑  153 
Q 270+77  T 347  ☑  347 
Q 471+218 T 689  ☑  689 
Q 77+390  T 467  ☑  467 
Q 542+37  T 579  ☑  579 
Q 370+37  T 407  ☑  407 
Q 37+705  T 742  ☑  742 
Q 18+52   T 70   ☑  70  
Q 616+1   T 617  ☑  617 
Q 2+719   T 721  ☑  721 
MSG : Prediction
Testing  acc: 0.99628, Testing  loss: 0.0141
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.9970|**0.2965**|1.8246|**0.3440**|1.8321|**0.33954**|
|5  |1.6617|**0.3836**|1.6440|**0.3867**|1.6463|**0.38742**|
|10 |1.3202|**0.5079**|1.2961|**0.5137**|1.2990|**0.51440**|
|30 |0.6375|**0.7808**|0.6939|**0.7391**|0.6949|**0.73730**|
|50 |0.0552|**0.9945**|0.0745|**0.9844**|0.0772|**0.98303**|
|80 |0.0068|**0.9999**|0.0196|**0.9960**|0.0199|**0.99534**|
|100|0.0030|**1.0000**|0.0135|**0.9966**|0.0141|**0.99628**|

#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000
 
```
$ python3 main.py -s small
```
 - **Experiment result**
```
Iteration 1
Q 0+945   T 945  ☒  158 
Q 693+8   T 701  ☒  158 
Q 6+249   T 255  ☒  12  
Q 8+406   T 414  ☒  15  
Q 94+361  T 455  ☒  108 
Q 90+159  T 249  ☒  108 
Q 111+16  T 127  ☒  128 
Q 564+1   T 565  ☒  12  
Q 668+260 T 928  ☒  118 
Q 909+79  T 988  ☒  110 
MSG : Prediction
Testing  acc: 0.35226, Testing  loss: 1.7853
...
Iteration 50
Q 271+948 T 1219 ☒  1229
Q 322+60  T 382  ☑  382 
Q 476+80  T 556  ☑  556 
Q 578+6   T 584  ☑  584 
Q 956+214 T 1170 ☒  1160
Q 289+894 T 1183 ☑  1183
Q 984+99  T 1083 ☑  1083
Q 86+25   T 111  ☑  111 
Q 0+463   T 463  ☑  463 
Q 506+788 T 1294 ☑  1294
MSG : Prediction
Testing  acc: 0.99576, Testing  loss: 0.0187
...
Iteration 100
Q 355+77  T 432  ☑  432 
Q 5+285   T 290  ☑  290 
Q 27+7    T 34   ☑  34  
Q 441+234 T 675  ☑  675 
Q 59+660  T 719  ☑  719 
Q 574+55  T 629  ☑  629 
Q 81+515  T 596  ☑  596 
Q 88+133  T 221  ☑  221 
Q 70+46   T 116  ☑  116 
Q 2+364   T 366  ☑  366 
MSG : Prediction
Testing  acc: 0.99819, Testing  loss: 0.0066
```  
|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.9019|**0.3245**|1.7916|**0.3521**|1.7853|**0.35226**|
|5  |1.4008|**0.4795**|1.3403|**0.5037**|1.3419|**0.49991**|
|10 |0.9792|**0.6428**|0.9571|**0.6498**|0.9608|**0.64869**|
|30 |0.0845|**0.9826**|0.1050|**0.9701**|0.1106|**0.96827**|
|50 |0.0085|**0.9997**|0.0188|**0.9957**|0.0187|**0.99576**|
|80 |0.0034|**0.9999**|0.0097|**0.9980**|0.0098|**0.99749**|
|100| 9.9177e-04 |**1.0000**|0.0063|**0.9987**|0.0066|**0.99819**|


### Subtractor:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py -t sub
```

```
Iteration 1
Q 405-57  T 348  ☒  166 
Q 921-52  T 869  ☒  161 
Q 71-57   T 14   ☒  16  
Q 164-45  T 119  ☒  16  
Q 541-68  T 473  ☒  16  
Q 881-12  T 869  ☒  188 
Q 612-25  T 587  ☒  16  
Q 618-62  T 556  ☒  16  
Q 707-55  T 652  ☒  166 
Q 54-33   T 21   ☒  16  
MSG : Prediction
Testing  acc: 0.34782, Testing  loss: 1.7367
...
Iteration 50
Q 775-465 T 310  ☑  310 
Q 627-65  T 562  ☑  562 
Q 208-6   T 202  ☑  202 
Q 687-60  T 627  ☑  627 
Q 748-71  T 677  ☑  677 
Q 68-55   T 13   ☑  13  
Q 403-18  T 385  ☑  385 
Q 844-721 T 123  ☑  123 
Q 438-84  T 354  ☑  354 
Q 717-368 T 349  ☑  349 
MSG : Prediction
Testing  acc: 0.98718, Testing  loss: 0.0469
...
Iteration 100
Q 398-16  T 382  ☑  382 
Q 927-325 T 602  ☑  602 
Q 454-14  T 440  ☑  440 
Q 618-3   T 615  ☑  615 
Q 884-2   T 882  ☑  882 
Q 587-75  T 512  ☑  512 
Q 236-51  T 185  ☑  185 
Q 969-23  T 946  ☑  946 
Q 656-35  T 621  ☑  621 
Q 770-7   T 763  ☑  763 
MSG : Prediction
Testing  acc: 0.99443, Testing  loss: 0.0194
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8844|**0.3259**|1.7407|**0.3444**|1.7367|**0.34782**|
|5  |1.4586|**0.4573**|1.4305|**0.4615**|1.4318|**0.46618**|
|10 |1.1175|**0.6137**|1.0839|**0.6339**|1.0880|**0.63224**|
|30 |0.1538|**0.9613**|0.1587|**0.9569**|0.1558|**0.95920**|
|50 |0.0351|**0.9942**|0.0474|**0.9865**|0.0469|**0.98718**|
|80 |0.0076|**0.9998**|0.0189|**0.9951**|0.0218|**0.99406**|
|100|0.0048|**1.0000**|0.0162|**0.9956**|0.0194|**0.99443**|


#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000

```
$ python3 main.py -t sub -s small
```

```
Iteration 1
Q 987-328 T 659  ☒  181 
Q 785-539 T 246  ☒  176 
Q 573-55  T 518  ☒  151 
Q 329-225 T 104  ☒  121 
Q 874-609 T 265  ☒  176 
Q 805-40  T 765  ☒  186 
Q 868-634 T 234  ☒  166 
Q 977-549 T 428  ☒  266 
Q 27-4    T 23   ☒  16  
Q 805-63  T 742  ☒  186 
MSG : Prediction
Testing  acc: 0.38109, Testing  loss: 1.6524
...
Iteration 50
Q 710-13  T 697  ☑  697 
Q 860-652 T 208  ☑  208 
Q 730-19  T 711  ☑  711 
Q 728-444 T 284  ☑  284 
Q 101-18  T 83   ☑  83  
Q 74-52   T 22   ☑  22  
Q 993-634 T 359  ☑  359 
Q 970-8   T 962  ☑  962 
Q 897-740 T 157  ☑  157 
Q 931-58  T 873  ☑  873 
MSG : Prediction
Testing  acc: 0.99454, Testing  loss: 0.0207
...
Iteration 100
Q 106-91  T 15   ☑  15  
Q 513-60  T 453  ☑  453 
Q 653-241 T 412  ☑  412 
Q 639-261 T 378  ☑  378 
Q 570-2   T 568  ☑  568 
Q 886-85  T 801  ☑  801 
Q 882-5   T 877  ☑  877 
Q 707-421 T 286  ☑  286 
Q 430-53  T 377  ☑  377 
Q 228-99  T 129  ☑  129 
MSG : Prediction
Testing  acc: 0.99845, Testing  loss: 0.0060
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8163|**0.3414**|1.6547|**0.3797**|1.6524|**0.38109**|
|5  |1.3009|**0.5270**|1.2304|**0.5646**|1.2369|**0.56110**|
|10 |0.8180|**0.7154**|0.7668|**0.7248**|0.7786|**0.71689,**|
|30 |0.0624|**0.9825**|0.0640|**0.9823**|0.0676|**0.97939**|
|50 |0.0107|**0.9990**|0.0196|**0.9952**|0.0207|**0.99454**|
|80 |0.0027|**1.0000**|0.0076|**0.9982**|0.0085|**0.99782**|
|100|0.0012|**1.0000**|0.0056|**0.9985**|0.0060|**0.99845**|


### Mix addition & subtraction:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py -t add_sub
```

```
Iteration 1
Q 10+59   T 69   ☒  11  
Q 48+53   T 101  ☒  11  
Q 240-79  T 161  ☒  11  
Q 600+755 T 1355 ☒  110 
Q 962-5   T 957  ☒  11  
Q 459+769 T 1228 ☒  110 
Q 781+154 T 935  ☒  110 
Q 996-94  T 902  ☒  110 
Q 31+113  T 144  ☒  111 
Q 9+308   T 317  ☒  111 
MSG : Prediction
Testing  acc: 0.35408, Testing  loss: 1.7792
...
Iteration 50
Q 146-43  T 103  ☑  103 
Q 977-864 T 113  ☒  122 
Q 400+89  T 489  ☑  489 
Q 770-2   T 768  ☑  768 
Q 416+100 T 516  ☑  516 
Q 69-54   T 15   ☒  25  
Q 184+681 T 865  ☒  864 
Q 239+3   T 242  ☑  242 
Q 449+8   T 457  ☑  457 
Q 44+79   T 123  ☑  123 
MSG : Prediction
Testing  acc: 0.91201, Testing  loss: 0.2537
...
Iteration 100
Q 74+502  T 576  ☑  576 
Q 6+83    T 89   ☑  89  
Q 94+960  T 1054 ☑  1054
Q 41+87   T 128  ☑  128 
Q 295-59  T 236  ☑  236 
Q 4+191   T 195  ☑  195 
Q 381+4   T 385  ☑  385 
Q 558+192 T 750  ☒  749 
Q 591+51  T 642  ☑  642 
Q 168+95  T 263  ☑  263 
MSG : Prediction
Testing  acc: 0.97009, Testing  loss: 0.0919
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.9422|**0.3229**|1.7824|**0.3520**|1.7792|**0.35408**|
|5  |1.6347|**0.4030**|1.6334|**0.4039**|1.6295|**0.40870**|
|10 |1.3788|**0.4867**|1.3516|**0.4919**|1.3526|**0.49073**|
|30 |0.7169|**0.7472**|0.7617|**0.7200**|0.7534|**0.72440**|
|50 |0.1867|**0.9486**|0.2543|**0.9147**|0.2537|**0.91201**|
|80 |0.0935|**0.9704**|0.1374|**0.9524**|0.1431|**0.95090**|
|100|0.0109|**0.9993**|0.0953|**0.9705**|0.0919|**0.97009**|


#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000

```
$ python3 main.py -t add_sub -s small
```

```
Iteration 1
Q 97-83   T 14   ☒  13  
Q 137+288 T 425  ☒  110 
Q 95+446  T 541  ☒  110 
Q 586-16  T 570  ☒  100 
Q 83+17   T 100  ☒  10  
Q 75+191  T 266  ☒  110 
Q 74+7    T 81   ☒  10  
Q 3+84    T 87   ☒  13  
Q 467-304 T 163  ☒  110 
Q 44+93   T 137  ☒  10  
MSG : Prediction
Testing  acc: 0.36667, Testing  loss: 1.7388
...
Iteration 50
Q 935-456 T 479  ☑  479 
Q 902+205 T 1107 ☒  1118
Q 745-33  T 712  ☑  712 
Q 331+578 T 909  ☑  909 
Q 904+333 T 1237 ☒  1236
Q 861-698 T 163  ☑  163 
Q 11+4    T 15   ☒  16  
Q 406-70  T 336  ☑  336 
Q 461-61  T 400  ☒  390 
Q 169+564 T 733  ☑  733 
MSG : Prediction
Testing  acc: 0.96190, Testing  loss: 0.1120
...
Iteration 100
Q 361-90  T 271  ☑  271 
Q 447+1   T 448  ☑  448 
Q 112-1   T 111  ☑  111 
Q 72+11   T 83   ☑  83  
Q 647-72  T 575  ☑  575 
Q 6+806   T 812  ☑  812 
Q 847-9   T 838  ☑  838 
Q 444-4   T 440  ☑  440 
Q 465+68  T 533  ☑  533 
Q 256+840 T 1096 ☒  1196
MSG : Prediction
Testing  acc: 0.98438, Testing  loss: 0.0471
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8746|**0.3403**|1.7350|**0.3671**|1.7388|**0.36667**|
|5  |1.4995|**0.4487**|1.4528|**0.4653**|1.4551|**0.46632**|
|10 |1.0894|**0.5962**|1.0714|**0.6034**|1.0707|**0.60299**|
|30 |0.2196|**0.9351**|0.2541|**0.9140**|0.2513|**0.91436**|
|50 |0.0633|**0.9831**|0.1069|**0.9635**|0.1120|**0.96190**|
|80 |0.0233|**0.9951**|0.0575|**0.9798**|0.0594|**0.98042**|
|100|0.0043|**1.0000**|0.0483|**0.9847**|0.0471|**0.98438**|


### Multiplication:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py -t mul
```

```
Iteration 1
Q 837*11  T 9207   ☒  1118  
Q 71*4    T 284    ☒  14    
Q 274*22  T 6028   ☒  1114  
Q 938*60  T 56280  ☒  11100 
Q 195*71  T 13845  ☒  1118  
Q 25*0    T 0      ☒  100   
Q 257*5   T 1285   ☒  1100  
Q 411*60  T 24660  ☒  1100  
Q 381*33  T 12573  ☒  1118  
Q 472*2   T 944    ☒  114   
MSG : Prediction
Testing  acc: 0.34756, Testing  loss: 1.7807
...
Iteration 50
Q 0*774   T 0      ☑  0     
Q 64*986  T 63104  ☒  63704 
Q 49*231  T 11319  ☒  11609 
Q 6*346   T 2076   ☒  2936  
Q 52*10   T 520    ☑  520   
Q 26*29   T 754    ☒  634   
Q 588*63  T 37044  ☒  37324 
Q 808*75  T 60600  ☒  62200 
Q 214*288 T 61632  ☒  62772 
Q 3*925   T 2775   ☒  2725  
MSG : Prediction
Testing  acc: 0.66193, Testing  loss: 0.8785
...
Iteration 100
Q 62*78   T 4836   ☒  4776  
Q 42*288  T 12096  ☒  12976 
Q 9*972   T 8748   ☒  8908  
Q 164*93  T 15252  ☒  15012 
Q 971*128 T 124288 ☒  122248
Q 83*362  T 30046  ☒  30426 
Q 8*453   T 3624   ☒  3744  
Q 46*281  T 12926  ☒  12206 
Q 976*6   T 5856   ☒  5876  
Q 75*604  T 45300  ☒  45500 
MSG : Prediction
Testing  acc: 0.68331, Testing  loss: 0.9594
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.9572|**0.2986**|1.7894|**0.3478**|1.7807|**0.34756**|
|5  |1.6547|**0.3710**|1.6492|**0.3739**|1.6441|**0.37578**|
|10 |1.4843|**0.4216**|1.4823|**0.4247**|1.4862|**0.42000**|
|30 |0.9706|**0.6395**|1.0041|**0.6201**|1.0024|**0.62080**|
|50 |0.7730|**0.7144**|0.8783|**0.6620**|0.8785|**0.66193**|
|80 |0.5757|**0.7957**|0.8638|**0.6860**|0.8689|**0.68426**|
|100|0.4550|**0.8461**|0.9616|**0.6866**|0.9594|**0.68331**|


#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000

```
$ python3 main.py -t mul -s small
```

```
Iteration 1
Q 126*8   T 1008   ☒  122   
Q 943*638 T 601634 ☒  111886
Q 9*551   T 4959   ☒  155   
Q 333*34  T 11322  ☒  11188 
Q 813*148 T 120324 ☒  111882
Q 265*54  T 14310  ☒  11500 
Q 217*917 T 198989 ☒  11199 
Q 162*353 T 57186  ☒  11155 
Q 0*229   T 0      ☒  120   
Q 66*3    T 198    ☒  12    
MSG : Prediction
Testing  acc: 0.37432, Testing  loss: 1.7029
...
Iteration 50
Q 680*679 T 461720 ☒  455520
Q 0*194   T 0      ☑  0     
Q 138*380 T 52440  ☒  50640 
Q 558*846 T 472068 ☒  482068
Q 640*7   T 4480   ☑  4480  
Q 591*7   T 4137   ☒  4377  
Q 16*11   T 176    ☒  156   
Q 5*57    T 285    ☑  285   
Q 883*248 T 218984 ☒  222244
Q 954*53  T 50562  ☒  51462 
MSG : Prediction
Testing  acc: 0.73622, Testing  loss: 0.6884
...
Iteration 100
Q 241*96  T 23136  ☒  23316 
Q 26*937  T 24362  ☒  24982 
Q 60*570  T 34200  ☑  34200 
Q 204*7   T 1428   ☑  1428  
Q 838*83  T 69554  ☒  69174 
Q 204*7   T 1428   ☑  1428  
Q 73*774  T 56502  ☒  56862 
Q 5*43    T 215    ☑  215   
Q 642*963 T 618246 ☒  615946
Q 374*75  T 28050  ☒  28350 
MSG : Prediction
Testing  acc: 0.75395, Testing  loss: 0.7708
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8546|**0.3337**|1.6923|**0.3768**|1.7029|**0.37432**|
|5  |1.5176|**0.4176**|1.4790|**0.4282**|1.4924|**0.42306**|
|10 |1.3134|**0.4871**|1.2762|**0.4929**|1.2876|**0.49063**|
|30 |0.7661|**0.7162**|0.8010|**0.6953**|0.8152|**0.68999**|
|50 |0.5734|**0.7889**|0.6728|**0.7412**|0.6884|**0.73622**|
|80 |0.3947|**0.8618**|0.6687|**0.7603**|0.6844|**0.75463**|
|100|0.3202|**0.8920**|0.7459|**0.7608**|0.7708|**0.75395**|



## Second part: different digits with same calculation type(add_sub)
### 2 digits:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py -t add_sub -d 2
```
|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.9641|**0.3686**|1.6606|**0.4468**|1.6698|**0.44148**|
|5  |1.2437|**0.5489**|1.1919|**0.5618**|1.2020|**0.55805**|
|10 |0.8220|**0.7150**|0.7942|**0.7107**|0.8020|**0.70366**|
|30 |0.1101|**0.9843**|0.1171|**0.9800**|0.1237|**0.97626**|
|50 |0.0190|**0.9987**|0.0312|**0.9928**|0.0337|**0.99292**|
|80 |0.0045|**0.9999**|0.0144|**0.9963**|0.0167|**0.99557**|
|100|0.0029|**1.0000**|0.0136|**0.9965**|0.0159|**0.99538**|

#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000

```
$ python3 main.py -t add_sub -d 2 -s small
```
|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8370|**0.3971**|1.5379|**0.4733**|1.5332|**0.47705**|
|5  |1.0913|**0.6016**|1.0360|**0.6203**|1.0270|**0.62985**|
|10 |0.5837|**0.8123**|0.5436|**0.8321**|0.5396|**0.83648**|
|30 |0.0384|**0.9965**|0.0443|**0.9933**|0.0448|**0.99265**|
|50 |0.0069|**0.9998**|0.0108|**0.9986**|0.0113|**0.99813**|
|80 |0.0021|**1.0000**|0.0049|**0.9991**|0.0055|**0.99885**|
|100|0.0012|**1.0000**|0.0034|**0.9996**|0.0041|**0.99910**|


### 3 digits:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py -t add_sub 
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.9422|**0.3229**|1.7824|**0.3520**|1.7792|**0.35408**|
|5  |1.6347|**0.4030**|1.6334|**0.4039**|1.6295|**0.40870**|
|10 |1.3788|**0.4867**|1.3516|**0.4919**|1.3526|**0.49073**|
|30 |0.7169|**0.7472**|0.7617|**0.7200**|0.7534|**0.72440**|
|50 |0.1867|**0.9486**|0.2543|**0.9147**|0.2537|**0.91201**|
|80 |0.0935|**0.9704**|0.1374|**0.9524**|0.1431|**0.95090**|
|100|0.0109|**0.9993**|0.0953|**0.9705**|0.0919|**0.97009**|


#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000

```
$ python3 main.py -t add_sub -s small
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8746|**0.3403**|1.7350|**0.3671**|1.7388|**0.36667**|
|5  |1.4995|**0.4487**|1.4528|**0.4653**|1.4551|**0.46632**|
|10 |1.0894|**0.5962**|1.0714|**0.6034**|1.0707|**0.60299**|
|30 |0.2196|**0.9351**|0.2541|**0.9140**|0.2513|**0.91436**|
|50 |0.0633|**0.9831**|0.1069|**0.9635**|0.1120|**0.96190**|
|80 |0.0233|**0.9951**|0.0575|**0.9798**|0.0594|**0.98042**|
|100|0.0043|**1.0000**|0.0483|**0.9847**|0.0471|**0.98438**|


### 4 digits:
#### a. Big data set
 - **Data Size**
   - Training data :    18000
   - Validation data :   2000
   - Testing data :     60000

```
$ python3 main.py -t add_sub -d 4
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.8803|**0.3454**|1.7217|**0.3728**|1.7113|**0.37783**|
|5  |1.5087|**0.4463**|1.5007|**0.4482**|1.5032|**0.44887**|
|10 |1.1973|**0.5477**|1.1784|**0.5491**|1.1868|**0.54794**|
|30 |0.6816|**0.7506**|0.7227|**0.7281**|0.7341|**0.72160**|
|50 |0.3599|**0.8728**|0.4909|**0.8161**|0.5099|**0.80654**|
|80 |0.1157|**0.9660**|0.3749|**0.8769**|0.4088|**0.86419**|
|100|0.0497|**0.9897**|0.4239|**0.8757**|0.4626|**0.86892**|


#### b. Small data set
 - **Data Size**
   - Training data :    27000
   - Validation data :   3000
   - Testing data :     20000

```
$ python3 main.py -t add_sub -d 4 -s small
```

|**Iteration**|**Training Loss**|**Training Accuracy**|**Validation Loss**|**Validation  Accuarcy**|**Testing  loss**|**Testing  acc**|
|---|---|---|---|---|---|---|
|1  |1.7877|**0.3683**|1.6432|**0.3953**|1.6453|**0.39181**|
|5  |1.3991|**0.4836**|1.3590|**0.4977**|1.3530|**0.50111**|
|10 |1.0488|**0.6010**|1.0349|**0.6085**|1.0324|**0.60828**|
|30 |0.5975|**0.7865**|0.6365|**0.7659**|0.6355|**0.76590**|
|50 |0.3118|**0.8920**|0.3983|**0.8519**|0.4024|**0.85047**|
|80 |0.0967|**0.9704**|0.2463|**0.9115**|0.2570|**0.90872**|
|100|0.0336|**0.9931**|0.2341|**0.9268**|0.2483|**0.92425**|


## Conclusion
### Different calculation type:
當訓練small data set時，不管是Addition、Subtraction、Addition & Subtraction、Multiplication表現都比訓練Big data set的準確度高。

**Big data set (Training: 18000, validation: 2000, testing: 60000, Iteration: 100)**
 - Addition (Acc: 0.99628)
 - Subtraction (Acc: 0.99443)
 - Addition & Subtraction (Acc: 0.97009)
 - Multiplication (Acc: 0.68331)

**Small data set (Training: 27000, validation: 3000, testing: 20000, Iteration: 100)**
 - Addition (Acc: 0.99819)
 - Subtraction (Acc: 0.99845)
 - Addition & Subtraction (Acc: 0.98438)
 - Multiplication (Acc: 0.75395)

### Different number of digit:
使用較少的digits，準確度也會越高。

**Big data set (Training: 18000, validation: 2000, testing: 60000, Iteration: 100)**
 - 2 digits (Acc: 0.99538)
 - 3 digits (Acc: 0.97009)
 - 4 digits (Acc: 0.86892)

**Small data set (Training: 27000, validation: 3000, testing: 20000, Iteration: 100)**
 - 2 digits (Acc: 0.99910)
 - 3 digits (Acc: 0.98438)
 - 4 digits (Acc: 0.92425)


## Authors
[Cheng-Da Wen](https://github.com/jeremywen0202)
