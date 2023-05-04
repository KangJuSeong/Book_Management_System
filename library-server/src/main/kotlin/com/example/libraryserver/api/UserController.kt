package com.example.libraryserver.api

import com.example.libraryserver.domain.user.LoginDto
import com.example.libraryserver.domain.user.UserDto
import com.example.libraryserver.service.UserService
import com.example.libraryserver.util.FailResponse
import com.example.libraryserver.util.Response
import com.example.libraryserver.util.SuccessResponse
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RestController


@RestController
class UserController(
    private val userService: UserService
) {
    @PostMapping("/login")
    fun login(@RequestBody data: LoginDto): Response<*> {
        val user: UserDto = userService.login(data.email, data.password) ?: return FailResponse(HttpStatus.BAD_REQUEST, "Login Fail")
        return SuccessResponse(HttpStatus.OK, "success", user)
    }
}