package com.example.libraryserver.domain.book

data class BookDto(
    val name: String,
    val author: String,
    val isbn: String,
    val isRental: Boolean,
    val location: String
) {
    fun toEntity(): Book =
        Book(
            name = this.name,
            author = this.author,
            isbn = this.isbn,
            isRental = this.isRental,
            location = this.location
        )
}

data class BookResDto(
    val id: Long,
    val name: String,
    val author: String,
    val isbn: String,
    val isRental: Boolean,
    val location: String
)