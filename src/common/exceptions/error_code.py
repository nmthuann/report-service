from enum import Enum

class ErrorType(Enum):
    NOT_FOUND = 'Not Found!'
    PERMISSION_DENIED = 'Permission Denied!'
    # Add more error types here
    NO_SUCCESS = 'Thực hiện tác vụ không thành công.'


class ErrorInput(Enum):
    INPUT_INVALID = 'Nhập thông tin không hợp lệ.'
    NAME_INVALID = 'Tên không được chứa số hoặc khoảng trắng.'
    INPUT_WRONG_FORMAT = 'Nhập thông tin sai định dạng.'
    NOT_FULL_FIELD = 'Vui lòng không bỏ trống.'
    FIELD_MISSING = 'bạn nhập thiếu '
    PHONE_NUMBER_ERROR = 'Số điện thoại phải có đúng 10 chữ số.'
    EMAIL_ERROR = 'Nhập Email chưa đúng.'
    PASSWORD_ERROR = 'Mật khẩu phải đủ 8 kí tự.'
    NUMBER_ERROR = 'Vui lòng không nhập số.'
    STRING_ERROR = 'Vui lòng không nhập text.'
    MAX_ERROR = 'Không nhập quá '
    MIN_ERROR = 'Phải nhập đủ '
    NOT_SELECT_FIELD = 'Vui lòng chọn '
    PRICE_INVALID = 'Unit price must be less than price'
    EMAIL_EXSIT = 'Email đã tồn tại.'
    AuthExceptionMessages = 'AuthExceptionMessages.'
    EMAIL_NOT_FOUND = 'Không tìm thấy email.'

class SystemError (Enum):
    INTERNAL_SERVER_ERROR = 'Internal server error.'
    CONNECT_ERROR = 'Kết nối thất bại.'

class MiddlewareError(Enum):
    TOKEN_MISSING = 'Bạn thiếu token.'
    TOKEN_INVALID = 'Token của bạn hết hạn khoặc không hợp lệ.'

class HttpError(Enum):
    BAD_REQUEST = 'bad request'
    PERMISSION_DENIED = "Permission denied"