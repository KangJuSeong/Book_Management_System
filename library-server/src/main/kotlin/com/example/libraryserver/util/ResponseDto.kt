package com.example.libraryserver.util


open class Response<T>(
    val status: T,
    val msg: String,
)
class SuccessResponse<T>(status: T, msg: String, data: T): Response<T>(status, msg) {
    var data: T = data
}

class FailResponse<T>(status: T, msg: String): Response<T>(status, msg){
}