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