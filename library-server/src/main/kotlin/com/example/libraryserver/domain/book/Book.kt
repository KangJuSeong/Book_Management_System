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
    location: String
): AuditEntity() {
    @Column(name = "name")
    var name: String = name

    @Column(name = "author")
    var author: String = author

    @Column(name = "isbn")
    var isbn: String = isbn


    @Column(name = "location")
    var location: String = location

    override fun toString(): String =
        "${this.name}, ${this.author}, ${this.isbn}, ${this.location}"
}