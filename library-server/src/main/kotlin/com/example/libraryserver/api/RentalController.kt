package com.example.libraryserver.api

import com.example.libraryserver.domain.rental.RentalReqDto
import com.example.libraryserver.domain.rental.RentalResDto
import com.example.libraryserver.service.RentalService
import com.example.libraryserver.util.DataResponse
import com.example.libraryserver.util.MsgResponse
import com.example.libraryserver.util.Response
import mu.KotlinLogging
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*


@RestController
@RequestMapping("/rental")
class RentalController(
    private val rentalService: RentalService
) {
    private val log = KotlinLogging.logger {  }
    @GetMapping("/list/{userId}")
    fun findAll(@PathVariable userId: String): Response<*> =
        DataResponse(HttpStatus.OK, "대여 정보 목록 가져오기", rentalService.findAll(userId.toInt()))

    @GetMapping("/{id}")
    fun findById(@PathVariable id: String): Response<*> {
        val rental: RentalResDto = rentalService.findById(id.toInt())?:
        return MsgResponse(HttpStatus.BAD_REQUEST, "대여 정보 가져오기 실패")
        return DataResponse(HttpStatus.OK, "대여 정보 가져오기", rental)
    }

    @PostMapping("")
    fun create(@RequestBody rentalReqDto: RentalReqDto): Response<*> {
        rentalService.create(rentalReqDto).apply {
            return if (this) {
                MsgResponse(HttpStatus.OK, "대여 성공")
            } else {
                MsgResponse(HttpStatus.BAD_REQUEST, "대여 실패")
            }
        }
    }

    @PutMapping("/{id}")
    fun update(@PathVariable id: String): Response<*> {
        return if (rentalService.update(id.toInt())) {
            MsgResponse(HttpStatus.OK, "반납 성공")
        } else {
            MsgResponse(HttpStatus.BAD_REQUEST, "반납 실패")
        }
    }

    @GetMapping("/search")
    fun search(@RequestParam keyword: String): Response<*> =
        DataResponse(HttpStatus.OK, "대여 검색 성공", rentalService.search("%$keyword%"))
}