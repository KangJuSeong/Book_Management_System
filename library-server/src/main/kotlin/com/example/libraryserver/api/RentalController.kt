package com.example.libraryserver.api

import com.example.libraryserver.service.RentalService
import com.example.libraryserver.util.DataResponse
import com.example.libraryserver.util.Response
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.PathVariable
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController


@RestController
@RequestMapping("/rental")
class RentalController(
    private val rentalService: RentalService
) {

    @GetMapping("/list/{userId}")
    fun findAll(@PathVariable userId: String): Response<*> =
        DataResponse(HttpStatus.OK, "대여 정보 목록 가져오기", rentalService.findAll(userId.toInt()))
}