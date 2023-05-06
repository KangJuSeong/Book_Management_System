package com.example.libraryserver.domain.rental

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.user.User
import java.time.LocalDateTime

data class RentalDto(
    val book: Book,
    val user: User,
    val rental: Boolean
) {
    fun toEntity(): Rental =
        Rental(
            book = this.book,
            user = this.user,
            rental = this.rental
        )
}

data class RentalResDto(
    val id: Long,
    val book: Book,
    val user: User,
    val rental: Boolean,
    val createdAt: LocalDateTime
)

data class RentalReqDto(
    val bookId: Int,
    val userId: Int
)
