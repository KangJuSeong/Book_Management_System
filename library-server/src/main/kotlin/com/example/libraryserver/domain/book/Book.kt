package com.example.libraryserver.domain.book

import com.example.libraryserver.domain.AuditEntity
import jakarta.persistence.Column
import jakarta.persistence.Entity
import jakarta.persistence.Table


@Entity
@Table(name = "Book")
class Book(
    name: String,
    author: String,
    isbn: String,
    isRental: Boolean,
    location: String
): AuditEntity() {
    @Column(name = "name")
    var name: String = name

    @Column(name = "author")
    var author: String = author

    @Column(name = "isbn")
    var isbn: String = isbn

    @Column(name = "is_rental")
    var isRental: Boolean = isRental

    @Column(name = "location")
    var location: String = location

    override fun toString(): String =
        "${this.name}, ${this.author}, ${this.isbn}, ${this.isRental} ${this.location}"

    fun toDto(): BookDto =
        BookDto(
            name = this.name,
            author = this.author,
            isbn = this.isbn,
            isRental = this.isRental,
            location = this.location
        )

    fun toResDto(): BookResDto =
        BookResDto(
            id = this.id!!,
            name = this.name,
            author = this.author,
            isbn = this.isbn,
            isRental = this.isRental,
            location = this.location
        )
}