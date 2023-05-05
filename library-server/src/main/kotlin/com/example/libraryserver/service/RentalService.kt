package com.example.libraryserver.service

import com.example.libraryserver.domain.rental.RentalRepository
import com.example.libraryserver.domain.rental.RentalResDto
import com.example.libraryserver.domain.user.Role
import com.example.libraryserver.domain.user.UserResDto
import org.springframework.stereotype.Service


@Service
class RentalService(
    private val rentalRepository: RentalRepository,
    private val userService: UserService
) {
    fun findAll(id: Int): List<RentalResDto>? {
        return when(userService.info(id).role) {
            Role.MANAGER -> rentalRepository.findJoinAll().map {it.toResDto()}
            else -> rentalRepository.findJoinAll(id).map { it.toResDto() }
        }
    }
}