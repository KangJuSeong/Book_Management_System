package com.example.libraryserver.service

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.book.BookRepository
import com.example.libraryserver.domain.rental.*
import com.example.libraryserver.domain.user.Role
import com.example.libraryserver.domain.user.User
import com.example.libraryserver.domain.user.UserRepository
import mu.KotlinLogging
import org.springframework.stereotype.Service
import java.util.*


@Service
class RentalService(
    private val rentalRepository: RentalRepository,
    private val userRepository: UserRepository,
    private val bookRepository: BookRepository
) {
    fun findAll(id: Int): List<RentalResDto>? {
        val user: User = userRepository.getReferenceById(id.toLong())
        return when(userRepository.findById(id).role) {
            Role.MANAGER -> rentalRepository.findJoinAll().map {it.toResDto()}
            else -> rentalRepository.findJoinAll(id.toLong()).map { it.toResDto() }
        }
    }

    fun findById(id: Int): RentalResDto? = rentalRepository.findJoinById(id).toResDto()

    fun create(rentalReqDto: RentalReqDto): Boolean {
        val book: Book = bookRepository.findById(rentalReqDto.bookId)!!
        val user: User = userRepository.getReferenceById(rentalReqDto.userId.toLong())
        return if (book.isRental) {
            false
        } else {
            book.isRental = true
            bookRepository.save(book)
            rentalRepository.save(
                RentalDto(
                    book = book,
                    user = user,
                    rental = true
                ).toEntity()
            )
            true
        }
    }
}