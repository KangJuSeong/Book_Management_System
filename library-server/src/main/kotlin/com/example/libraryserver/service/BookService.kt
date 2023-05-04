package com.example.libraryserver.service

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.book.BookRepository
import org.springframework.stereotype.Service


@Service
class BookService(
    private val bookRepository: BookRepository
) {
    fun findAll(): MutableList<Book> = bookRepository.findAll()
}