package com.example.libraryserver.domain.book

data class BookDto(
    var name: String,
    var author: String,
    var isbn: String,
    var location: String
) {
    fun toEntity(): Book =
        Book(
            name = this.name,
            author = this.author,
            isbn = this.isbn,
            location = this.location
        )
}