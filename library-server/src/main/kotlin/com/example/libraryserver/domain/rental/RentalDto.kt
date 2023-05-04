package com.example.libraryserver.domain.rental

import com.example.libraryserver.domain.book.Book
import com.example.libraryserver.domain.user.User

data class RentalDto(
    var book: Book,
    var user: User,
    var rental: Boolean
) {
    fun toEntity(): Rental =
        Rental(
            book = this.book,
            user = this.user,
            rental = this.rental
        )
}