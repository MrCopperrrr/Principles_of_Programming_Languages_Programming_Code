# Hướng dẫn Bài tập BKOOL

## Thiết lập môi trường

1.  **Mở Terminal tại thư mục gốc của dự án.**
2.  **Di chuyển vào thư mục `src`:**
    ```powershell
    cd src
    ```
3.  **Cài đặt runtime ANTLR4 cho Python (nếu chưa có):**
    ```powershell
    python -m pip install antlr4-python3-runtime
    ```
4.  **Cấu hình biến môi trường `ANTLR_JAR`:**
    Tải file [antlr-4.13.2-complete.jar](https://www.antlr.org/download/antlr-4.13.2-complete.jar) và trỏ biến môi trường đến đường dẫn của nó.
    VD (trên Windows PowerShell):
    ```powershell
    $env:ANTLR_JAR = "C:\Users\Admin\Downloads\Compressed\Syntax Programming Code\src\antlr-4.13.2-complete.jar"
    ```

## Các lệnh cơ bản

*   **Tạo mã nguồn từ file grammar:**
    ```powershell
    python run.py gen
    ```
*   **Chạy test case:**
    ```powershell
    python run.py test LexerSuite
    python run.py test ParserSuite
    ```

## Quy trình làm bài
1.  Copy nội dung bài tập vào file `src/main/bkool/parser/BKOOL.g4`.
2.  Chạy lệnh `python run.py gen`.
3.  Nộp toàn bộ file trong thư mục `target/main/bkool/parser` và file `BKOOL.g4`.

---

## Bài 1: Khai báo Program, Variable và Function
```antlr
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardecl | funcdecl)+ EOF;

vardecl: 'vardecl';

funcdecl: 'funcdecl';

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```

## Bài 2: Khai báo Biến và Hàm (Variable & Function Declarations)

### Mã ANTLR (BKOOL.g4):
```antlr
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF;

decl: vardecl | funcdecl;

vardecl: type_name id_list ';';

funcdecl: type_name ID '(' param_list? ')' body;

param_list: param (';' param)*;

param: type_name id_list;

id_list: ID (',' ID)*;

type_name: 'int' | 'float';

body: 'body';

ID: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```

---

## Bài 3: Khai báo Biến và Hàm (Variable & Function Declarations)
```antlr
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF;

decl: vardecl | funcdecl;

vardecl: type_name id_list ';';

funcdecl: type_name ID '(' param_list? ')' body;

param_list: param (';' param)*;

param: type_name id_list;

id_list: ID (',' ID)*;

type_name: 'int' | 'float';

body: '{' (vardecl | statement)* '}';

statement: assignment | call | return_stmt;

assignment: ID '=' expr ';';

call: ID '(' exp_list? ')' ';';

return_stmt: 'return' expr ';';

exp_list: expr (',' expr)*;

expr: 'expr';

ID: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```

## Bài 4: Khai báo Biểu thức (Full Expressions)

### Mã ANTLR (BKOOL.g4):
```antlr
grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: decl+ EOF;

decl: vardecl | funcdecl;

vardecl: type_name id_list ';';

funcdecl: type_name ID '(' param_list? ')' body;

param_list: param (';' param)*;

param: type_name id_list;

id_list: ID (',' ID)*;

type_name: 'int' | 'float';

body: '{' (vardecl | statement)* '}';

statement: assignment | call | return_stmt;

assignment: ID '=' expr ';';

call: ID '(' exp_list? ')' ';';

return_stmt: 'return' expr ';';

exp_list: expr (',' expr)*;

// Expressions
expr: expr1 '+' expr | expr1; // Right associative
expr1: expr2 '-' expr2 | expr2; // Non-associative
expr2: expr2 ('*' | '/') expr3 | expr3; // Left associative
expr3: ID '(' exp_list? ')' | ID | INTLIT | FLOATLIT | '(' expr ')';

// Lexer
INTLIT: [0-9]+;
FLOATLIT: [0-9]+ '.' [0-9]+;
ID: [a-zA-Z]+;

WS: [ \t\r\n]+ -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};
```