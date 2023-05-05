package com.example.libraryserver.util


open class Response<T>(
    val status: T,
    val msg: String,
)
class DataResponse<T>(status: T, msg: String, data: T): Response<T>(status, msg) {
    var data: T = data
}

class MsgResponse<T>(status: T, msg: String): Response<T>(status, msg){
}