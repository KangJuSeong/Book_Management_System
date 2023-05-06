package com.example.libraryserver.api

import com.example.libraryserver.domain.user.LoginDto
import com.example.libraryserver.domain.user.UserDto
import com.example.libraryserver.domain.user.UserResDto
import com.example.libraryserver.service.UserService
import com.example.libraryserver.util.DataResponse
import com.example.libraryserver.util.MsgResponse
import com.example.libraryserver.util.Response
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.PostMapping
import org.springframework.web.bind.annotation.RequestBody
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RequestParam
import org.springframework.web.bind.annotation.RestController


@RestController
@RequestMapping("/user")
class UserController(
    private val userService: UserService
) {
    @PostMapping("/login")
    fun login(@RequestBody data: LoginDto): Response<*> {
        val user: UserResDto = userService.login(data)?:
        return MsgResponse(HttpStatus.BAD_REQUEST, "로그인 실패")
        return DataResponse(HttpStatus.OK, "로그인 성공", user)
    }

    @PostMapping("/signup")
    fun signup(@RequestBody data: UserDto): Response<*> {
        val user: UserResDto = userService.signup(data)?:
        return MsgResponse(HttpStatus.BAD_REQUEST, "회원가입 실패")
        return DataResponse(HttpStatus.OK, "회원가입 성공", user)
    }

    @GetMapping("/{id}")
    fun info(@PathVariable("id") id: String): Response<*> =
        DataResponse(HttpStatus.OK, "회원 정보 가져오기", userService.info(id.toInt()))


    @GetMapping("/search")
    fun search(@RequestParam keyword: String): Response<*> =
        DataResponse(HttpStatus.OK, "회원 검색 성공", userService.search("%$keyword%"))
}
