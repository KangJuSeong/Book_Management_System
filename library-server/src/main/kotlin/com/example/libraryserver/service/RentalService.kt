package com.example.libraryserver.service

import com.example.libraryserver.domain.rental.Rental
import com.example.libraryserver.domain.rental.RentalRepository

class RentalService(
    private val rentalRepository: RentalRepository
) {
    fun findAll(): MutableList<Rental> = rentalRepository.findAll()
}