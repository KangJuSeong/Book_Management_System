package com.example.libraryserver.api

import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController


@RestController
class HealthController {

    @GetMapping("/health")
    fun health(): String = "Very Healthy"
}