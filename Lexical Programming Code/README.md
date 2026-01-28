Rewrite README.md

Mở Terminal
```
cd initial/src
python -m pip install antlr4-python3-runtime
python run.py gen
```
Nếu có lỗi tải file này: https://www.antlr.org/download/antlr-4.13.2-complete.jar (có thể để đâu cũng được)(nhập đường dẫn file vào biến ANTLR_JAR vào Terminal)
VD: (Thường nằm trong Downloads)
```
$env:ANTLR_JAR = "C:\antlr\antlr-4.13.2-complete.jar"
```

```
python run.py gen
python run.py test LexerSuite
python run.py test ParserSuite
```
Chạy test cho có thôi


Copy từng bài vào file src/main/bkit/parser/BKIT.g4 và chạy lại lệnh 
```
python run.py gen
```
Sau đó nộp toàn bộ file trong thư mục target (trừ __pycache__) và file BKIT.g4

## Bài 1
grammar BKIT;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

// Quy tắc Parser (Đơn giản để build thành công)
program: tokens+ EOF;
tokens: ID | ERROR_CHAR;

// --- LEXER RULES ---

// 1. Pascal Identifier: Bắt đầu bằng chữ thường, theo sau là chữ hoặc số
ID: [a-z][a-z0-9]*;

// 2. Bỏ qua khoảng trắng
WS: [ \t\r\n]+ -> skip;

// 3. Ký tự lỗi: Sử dụng đúng class ErrorToken từ lexererr
ERROR_CHAR: . { raise ErrorToken(self.text) };

## Bài 2
grammar BKIT;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

// Quy tắc Parser
program: tokens+ EOF;
tokens: REAL | ERROR_CHAR; // CHỈ giữ lại REAL và ERROR_CHAR

// --- LEXER RULES ---

// 1. Pascal Real Number
// Case 1: Có dấu chấm (phải có số 2 bên), có thể có phần mũ e
// Case 2: Không có dấu chấm nhưng bắt buộc có phần mũ e
REAL: [0-9]+ '.' [0-9]+ ('e' '-'? [0-9]+)? 
    | [0-9]+ 'e' '-'? [0-9]+ ;

// 2. Khoảng trắng
WS: [ \t\r\n]+ -> skip;

// 3. Ký tự lỗi
// Khi không có quy tắc ID, các chữ cái như 'e', 'abc' sẽ bị bắt ở đây
ERROR_CHAR: . { raise ErrorToken(self.text) };

## Bài 3
grammar BKIT;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

// Quy tắc Parser
program: tokens+ EOF;
tokens: STRING | ERROR_CHAR; // Chỉ giữ lại STRING và ERROR_CHAR cho bài này

// --- LEXER RULES ---

// Pascal String: 
// 1. Bắt đầu bằng dấu nháy đơn '
// 2. Nội dung bên trong: có thể là bất kỳ ký tự nào KHÔNG PHẢI nháy đơn (~['])
//    HOẶC là cặp nháy đơn back-to-back ('')
// 3. Kết thúc bằng dấu nháy đơn '
STRING: '\'' ( ~['\r\n] | '\'\'' )* '\'' ;

// Khoảng trắng
WS: [ \t\r\n]+ -> skip;

// Ký tự lỗi
ERROR_CHAR: . { raise ErrorToken(self.text) };

## Bài 4
grammar BKIT;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

// Quy tắc Parser
program: tokens+ EOF;
tokens: IPV4 | ERROR_CHAR; // Chỉ giữ lại IPV4 và ERROR_CHAR cho bài này

// --- LEXER RULES ---

// Định nghĩa một nhóm số từ 0-255
// 1. '25' [0-5]        -> 250 tới 255
// 2. '2' [0-4] [0-9]   -> 200 tới 249
// 3. '1' [0-9] [0-9]   -> 100 tới 199
// 4. [1-9] [0-9]?      -> 1 tới 99 (không có số 0 ở đầu)
// 5. '0'               -> Đúng số 0 duy nhất
fragment BYTE: '25' [0-5] 
             | '2' [0-4] [0-9] 
             | '1' [0-9] [0-9] 
             | [1-9] [0-9]? 
             | '0';

// IPv4 gồm đúng 4 nhóm BYTE ngăn cách bởi dấu chấm
IPV4: BYTE '.' BYTE '.' BYTE '.' BYTE;

// Khoảng trắng
WS: [ \t\r\n]+ -> skip;

// Ký tự lỗi
ERROR_CHAR: . { raise ErrorToken(self.text) };

## Bài 5
grammar BKIT;

@lexer::header {
from lexererr import *
}

options {
    language = Python3;
}

// Quy tắc Parser
program: tokens+ EOF;
tokens: PHP_INT | ERROR_CHAR; // Chỉ giữ lại PHP_INT và ERROR_CHAR cho bài này

// --- LEXER RULES ---

// PHP Decimal Integer:
// 1. Số 0 duy nhất: '0'
// 2. Hoặc bắt đầu bằng số từ 1-9, theo sau là các chữ số hoặc dấu gạch dưới nằm giữa số
// Hành động: self.text.replace('_', '') để xóa dấu gạch dưới trước khi trả về
PHP_INT: ( '0' | [1-9] [0-9]* ('_' [0-9]+)* ) 
         { self.text = self.text.replace('_', '') };

// Khoảng trắng
WS: [ \t\r\n]+ -> skip;

// Ký tự lỗi
ERROR_CHAR: . { raise ErrorToken(self.text) };

## Bài 6
Đi làm BTL PPL