package com.example.libraryserver.service

import com.example.libraryserver.domain.user.*
import org.springframework.stereotype.Service
import java.util.NoSuchElementException


@Service
class UserService(
    private val userRepository: UserRepository
) {
    fun login(data: LoginDto): UserResDto? {
        return userRepository.findByEmailAndPassword(data.email, data.password)?.toResDto()
    }

    fun signup(data: UserDto): UserResDto? {
        userRepository.findByEmail(data.email)?: return userRepository.save(data.toEntity()).toResDto()
        return null
    }

    fun info(id: Int): UserResDto = userRepository.findById(id).toResDto()

    fun reversOrderUsers(): List<UserDto> = userRepository.reversOrderUsers().map {it.toDto()}
}