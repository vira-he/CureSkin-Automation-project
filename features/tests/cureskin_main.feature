# Created by vera at 7/12/23
Feature: Test for Main page feature

  Scenario: User can access Search by Product page
    Given Open main page
    When Click on Shop by product button
    When Click Sunscreen
    When Open the first product in search
    Then Verify the fist product in Sunscreen