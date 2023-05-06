package com.example.libraryserver.api

import com.example.libraryserver.domain.book.BookDto
import com.example.libraryserver.domain.book.BookResDto
import com.example.libraryserver.service.BookService
import com.example.libraryserver.util.DataResponse
import com.example.libraryserver.util.MsgResponse
import com.example.libraryserver.util.Response
import org.springframework.http.HttpStatus
import org.springframework.web.bind.annotation.*


@RestController
@RequestMapping("/book")
class BookController(
    private val bookService: BookService
) {

    @GetMapping("/list")
    fun findAll(): Response<*> = DataResponse(HttpStatus.OK, "도서 목록 가져오기", bookService.findAll())

    @GetMapping("/search")
    fun search(@RequestParam keyword: String): Response<*> {
        val books: List<BookResDto> = bookService.search("%${keyword}%")
        return DataResponse(HttpStatus.OK, "도서 검색 결과 가져오기", books)
    }

    @GetMapping("/{id}")
    fun info(@PathVariable id: String): Response<*> {
        val book: BookResDto = bookService.info(id.toInt())?:
        return MsgResponse(HttpStatus.BAD_REQUEST, "도서 정보 조회 실패")
        return DataResponse(HttpStatus.OK, "도서 정보 조회 성공", book)
    }

    @PostMapping("")
    fun create(@RequestBody bookDto: BookDto): Response<*> {
        return DataResponse(HttpStatus.OK, "도서 등록 성공", bookService.create(bookDto))
    }

    @DeleteMapping("{id}")
    fun delete(@PathVariable id: String): Response<*> {
        bookService.delete(id.toLong())
        return MsgResponse(HttpStatus.OK, "도서 삭제 성공")
    }
}