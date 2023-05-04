package com.example.libraryserver.service

import com.example.libraryserver.domain.user.User
import com.example.libraryserver.domain.user.UserRepository
import org.springframework.stereotype.Service


@Service
class UserService(
    private val userRepository: UserRepository
) {
    fun findAll(): MutableList<User> = userRepository.findAll()
}