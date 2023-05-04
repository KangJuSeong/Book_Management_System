package com.example.libraryserver.domain.rental

import org.springframework.data.jpa.repository.JpaRepository

interface RentalRepository: JpaRepository<Rental, Long> {
}