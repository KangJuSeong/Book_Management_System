package com.example.libraryserver.service

import com.example.libraryserver.domain.book.BookDto
import com.example.libraryserver.domain.book.BookRepository
import com.example.libraryserver.domain.book.BookResDto
import org.springframework.stereotype.Service


@Service
class BookService(
    private val bookRepository: BookRepository
) {
    fun findAll(): List<BookResDto> = bookRepository.findAll().map {it.toResDto()}

    fun search(keyword: String): List<BookResDto> = bookRepository.findBooks(keyword).map {it.toResDto()}

    fun info(id: Int): BookResDto? = bookRepository.findById(id)?.toResDto()

    fun create(bookDto: BookDto): BookResDto {
        return bookRepository.save(bookDto.toEntity()).toResDto()
    }

    fun delete(id: Long): Unit = bookRepository.deleteById(id)
}