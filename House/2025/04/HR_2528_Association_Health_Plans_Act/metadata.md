# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2528
- Title: Association Health Plans Act
- Congress: 119
- Bill type: HR
- Bill number: 2528
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2026-05-28T19:05:26Z
- Update date including text: 2026-05-28T19:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-06-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 21 - 15.
- 2025-12-15 - Calendars: Placed on the Union Calendar, Calendar No. 357.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-409.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-409.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-06-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-06-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 21 - 15.
- 2025-12-15 - Calendars: Placed on the Union Calendar, Calendar No. 357.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-409.
- 2025-12-15 - Committee: Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-409.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2528",
    "number": "2528",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Association Health Plans Act",
    "type": "HR",
    "updateDate": "2026-05-28T19:05:26Z",
    "updateDateIncludingText": "2026-05-28T19:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-12-15",
      "calendarNumber": {
        "calendar": "U00357"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 357.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-409.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-12-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Education and Workforce. H. Rept. 119-409.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 21 - 15.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2025-12-15T18:10:16Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-25T13:10:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-01T14:00:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "GA"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MO"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OK"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "CA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WI"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "PA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MI"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "UT"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NC"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "PA"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "AR"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "NE"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "AZ"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NJ"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TX"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "MN"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "AZ"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "IN"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "NJ"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AZ"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "AZ"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "GA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "KY"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "FL"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "WI"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "AZ"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2528ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2528\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Walberg (for himself, Mr. Allen , Mr. Onder , Mr. Crenshaw , Mrs. Bice , Mr. Kiley of California , Mr. Grothman , Mr. Mackenzie , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to clarify the treatment of certain association health plans as employers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Association Health Plans Act .\n#### 2. Treatment of group or association of employers\n##### (a) In general\nSection 3(5) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(5) ) is amended\u2014\n**(1)**\nby striking The term and inserting (A) The term ; and\n**(2)**\nby adding at the end the following:\n(B) For purposes of subparagraph (A), a group or association of employers shall be treated as an employer , regardless of whether the employers composing such group or association are in the same industry, trade, or profession, if such group or association\u2014 (i) (I) has established and maintains an employee welfare benefit plan that is a group health plan (as defined in section 733(a)(1)); (II) provides coverage under such plan to at least 51 employees after all of the employees employed by all of the employer members of such group or association have been aggregated and counted together as described in subparagraph (D); (III) has been actively in existence for at least 2 years; (IV) has been formed and maintained in good faith for purposes other than providing medical care (as defined in section 733(a)(2)) through the purchase of insurance or otherwise; (V) does not condition membership in the group or association on any health status-related factor (as described in section 702(a)(1)) relating to any individual; (VI) makes coverage under such plan available to all employer members of such group or association regardless of any health status-related factor (as described in section 702(a)(1)) relating to such employer members; (VII) does not provide coverage under such plan to any individual other than an employee of an employer member of such group or association; (VIII) has established a governing board with by-laws or other similar indications of formality to manage and operate such plan in both form and substance, of which at least 75 percent of the board members shall be made up of employer members of such group or association participating in the plan that are duly elected by each participating employer member casting 1 vote during a scheduled election; (IX) is not a health insurance issuer (as defined in section 733(b)(2)), and is not owned or controlled by such a health insurance issuer or by a subsidiary or affiliate of such a health insurance issuer, other than to the extent such a health insurance issuer may participate in the group or association as a member; (ii) is structured in good faith with any set of criteria to qualify for such treatment in any advisory opinion issued prior to the date of enactment of the Association Health Plans Act ; or (iii) meets any other set of criteria to qualify for such treatment that the Secretary by regulation may provide. (C) (i) For purposes of subparagraph (B), a self-employed individual shall be treated as\u2014 (I) an employer who may become a member of a group or association of employers; (II) an employee who may participate in an employee welfare benefit plan established and maintained by such group or association; and (III) a participant of such plan subject to the eligibility determination and monitoring requirements set forth in clause (iii). (ii) For purposes of this subparagraph, the term self-employed individual means an individual who\u2014 (I) does not have any common law employees; (II) has a bona fide ownership right in a trade or business, regardless of whether such trade or business is incorporated or unincorporated; (III) earns wages (as defined in section 3121(a) of the Internal Revenue Code of 1986) or self-employment income (as defined in section 1402(b) of such Code) from such trade or business; and (IV) works at least 10 hours a week or 40 hours per month providing personal services to such trade or business. (iii) The board of a group or association of employers shall\u2014 (I) initially determine whether an individual meets the requirements under clause (ii) to be considered to a self-employed individual for the purposes of being treated as an\u2014 (aa) employer member of such group or association (in accordance with clause (i)(I)); and (bb) employee who may participate in the employee welfare benefit plan established and maintained by such group or association (in accordance with clause (i)(II)); (II) through reasonable monitoring procedures, periodically determine whether the individual continues to meet such requirements; and (III) if the board determines that an individual no longer meets such requirements, not make such plan coverage available to such individual (or dependents thereof) for any plan year following the plan year during which the board makes such determination. If, subsequent to a determination that an individual no longer meets such requirements, such individual furnishes evidence of satisfying such requirements, such individual (and dependents thereof) shall be eligible to receive plan coverage. (D) For purposes of subparagraph (B), all of the employees (including self-employed individuals) employed by all of the employer members (including self-employed individuals) of a group or association of employers shall be\u2014 (i) treated as participants in a single plan multiple employer welfare arrangement; and (ii) aggregated and counted together for purposes of any regulation of an employee welfare benefit plan established and maintained by such group or association. .\n##### (b) Determination of employer or joint employer status\nThe provision of employee welfare benefit plan coverage by a group or association of employers shall not be construed as evidence for establishing an employer or joint employer relationship under any Federal or State law.\n#### 3. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers\nPart 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1181 , et seq.) is amended by adding at the end the following:\n736. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers (a) Premium rates for a group or association of employers (1) (A) In the case of an employee welfare benefit plan established and maintained by a group or association of employers described in section 3(5)(B), such plan may, to the extent not prohibited under State law\u2014 (i) establish base premium rates formed on an actuarially sound, modified community rating methodology that considers the pooling of all plan participant claims; and (ii) utilize the specific risk profile of each employer member of such group or association to determine contribution rates for each such employer member\u2019s share of a premium by actuarially adjusting above or below the established base premium rates. (B) For purposes of paragraph (1), the term employer member means\u2014 (i) an employer who is a member of such group or association of employers and employs at least 1 common law employee; or (ii) a group made up solely of self-employed individuals, within which all of the self-employed individual members of such group or association are aggregated together as a single employer member group, provided the group includes at least 20 self-employed individual members. (2) In the event a group or association is made up solely of self-employed individuals (and no employers with at least 1 common law employee are members of such group or association), the employee welfare benefit plan established by such group or association shall\u2014 (A) treat all self-employed individuals who are members of such group or association as a single risk pool; (B) pool all plan participant claims; and (C) charge each plan participant the same premium rate. (b) Discrimination and pre-Existing condition protections An employee welfare benefit plan established and maintained by a group or association of employers described in section 3(5)(B) shall be prohibited from\u2014 (1) establishing any rule for eligibility (including continued eligibility) of any individual (including an employee of an employer member or a self-employed individual, or a dependent of such employee or self-employed individual) to enroll for benefits under the terms of the plan that discriminates based on any health status-related factor that relates to such individual (consistent with the rules under section 702(a)(1)); (2) requiring an individual (including an employee of an employer member or a self-employed individual, or a dependent of such employee or self-employed individual), as a condition of enrollment or continued enrollment under the plan, to pay a premium or contribution that is greater than the premium or contribution for a similarly situated individual enrolled in the plan based on any health status-related factor that relates to such individual (consistent with the rules under section 702(b)(1)); and (3) denying coverage under such plan on the basis of a pre-existing condition (consistent with the rules under section 2704 of the Public Health Service Act). .\n#### 4. Rule of construction\nNothing in this Act shall be construed to exempt a group health plan which is an employee welfare benefit plan offered through a group or association of employers from the requirements of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 (29 U.S.C. 1181 et. seq.), including the provisions of part A of title XXVII of the Public Health Service Act as incorporated by reference into this Act through section 715.",
      "versionDate": "2025-04-01",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2528rh.xml",
      "text": "IB\nUnion Calendar No. 357\n119th CONGRESS\n1st Session\nH. R. 2528\n[Report No. 119\u2013409]\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Walberg (for himself, Mr. Allen , Mr. Onder , Mr. Crenshaw , Mrs. Bice , Mr. Kiley of California , Mr. Grothman , Mr. Mackenzie , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Education and Workforce\nDecember 15, 2025 Additional sponsors: Mr. Owens , Mr. Harris of North Carolina , Mr. Thompson of Pennsylvania , Mr. Hill of Arkansas , Mr. Smith of Nebraska , Mr. Biggs of Arizona , Mr. Cuellar , Mr. Van Drew , Mr. Weber of Texas , Mrs. Fischbach , Mr. Hunt , Mr. Goldman of Texas , Mr. Gosar , Mr. Messmer , Mr. Smith of New Jersey , Mr. Ciscomani , Mr. Hamadeh of Arizona , Mr. Bishop , Mr. Meuser , Mr. Barr , Mr. Dunn of Florida , Mr. Calvert , Mr. Fitzgerald , and Mr. Schweikert\nDecember 15, 2025 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on April 1, 2025\nA BILL\nTo amend the Employee Retirement Income Security Act of 1974 to clarify the treatment of certain association health plans as employers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Association Health Plans Act .\n#### 2. Treatment of group or association of employers\n##### (a) In general\nSection 3(5) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(5) ) is amended\u2014\n**(1)**\nby striking The term and inserting (A) The term ; and\n**(2)**\nby adding at the end the following:\n(B) For purposes of subparagraph (A), a group or association of employers shall be treated as an employer solely for purposes of sponsoring a group health plan, regardless of whether the employers composing such group or association are in the same industry, trade, or profession, if such group or association\u2014 (i) (I) has established and maintains an employee welfare benefit plan that is a group health plan (as defined in section 733(a)(1)); (II) provides coverage under such plan to at least 51 employees after all of the employees employed by all of the employer members of such group or association have been aggregated and counted together as described in subparagraph (D); (III) has been actively in existence for at least 2 years; (IV) has been formed and maintained in good faith for purposes other than providing medical care (as defined in section 733(a)(2)) through the purchase of insurance or otherwise; (V) does not condition membership in the group or association on any health status-related factor (as described in section 702(a)(1)) relating to any individual; (VI) makes coverage under such plan available to all employer members of such group or association regardless of any health status-related factor (as described in section 702(a)(1)) relating to such employer members; (VII) does not provide coverage under such plan to any individual other than an employee of an employer member of such group or association; (VIII) has established a governing board with by-laws or other similar indications of formality to manage and operate such plan in both form and substance, of which at least 75 percent of the board members shall be made up of employer members of such group or association participating in the plan that are duly elected by each participating employer member casting 1 vote during a scheduled election; and (IX) is not a health insurance issuer (as defined in section 733(b)(2)), and is not owned or controlled by such a health insurance issuer or by a subsidiary or affiliate of such a health insurance issuer, other than to the extent such a health insurance issuer may participate in the group or association as a member; (ii) is structured in good faith with any set of criteria to qualify for such treatment in any advisory opinion issued prior to the date of enactment of the Association Health Plans Act ; or (iii) meets any other set of criteria to qualify for such treatment that the Secretary by regulation may provide. (C) (i) For purposes of subparagraph (B), a self-employed individual shall be treated as\u2014 (I) an employer who may become a member of a group or association of employers; (II) an employee who may participate in an employee welfare benefit plan established and maintained by such group or association; and (III) a participant of such plan subject to the eligibility determination and monitoring requirements set forth in clause (iii). (ii) For purposes of this subparagraph, the term self-employed individual means an individual who\u2014 (I) does not have any common law employees; (II) has a bona fide ownership right in a trade or business, regardless of whether such trade or business is incorporated or unincorporated; (III) earns wages (as defined in section 3121(a) of the Internal Revenue Code of 1986) or self-employment income (as defined in section 1402(b) of such Code) from such trade or business; and (IV) works at least 10 hours a week or 40 hours per month providing personal services to such trade or business. (iii) The board of a group or association of employers shall\u2014 (I) initially determine whether an individual meets the requirements under clause (ii) to be considered to a self-employed individual for the purposes of being treated as an\u2014 (aa) employer member of such group or association (in accordance with clause (i)(I)); and (bb) employee who may participate in the employee welfare benefit plan established and maintained by such group or association (in accordance with clause (i)(II)); (II) through reasonable monitoring procedures, periodically determine whether the individual continues to meet such requirements; and (III) if the board determines that an individual no longer meets such requirements, not make such plan coverage available to such individual (or dependents thereof) for any plan year following the plan year during which the board makes such determination. If, subsequent to a determination that an individual no longer meets such requirements, such individual furnishes evidence of satisfying such requirements, such individual (and dependents thereof) shall be eligible to receive plan coverage. (D) For purposes of subparagraph (B), all of the employees (including self-employed individuals) employed by all of the employer members (including self-employed individuals) of a group or association of employers shall be\u2014 (i) treated as participants in a single plan multiple employer welfare arrangement; and (ii) aggregated and counted together for purposes of any regulation of an employee welfare benefit plan established and maintained by such group or association. .\n##### (b) Determination of employer or joint employer status\nThe provision of employee welfare benefit plan coverage by a group or association of employers shall not be construed as evidence for establishing an employer or joint employer relationship under any Federal or State law.\n#### 3. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers\n##### (a) In general\nPart 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1181 , et seq.) is amended by adding at the end the following:\n736. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers (a) Premium rates for a group or association of employers (1) (A) In the case of an employee welfare benefit plan established and maintained by a group or association of employers described in section 3(5)(B), such plan may, to the extent not prohibited under State law\u2014 (i) establish base premium rates formed on an actuarially sound, modified community rating methodology that considers the pooling of all plan participant claims; and (ii) utilize the specific risk profile of each employer member of such group or association to determine contribution rates for each such employer member\u2019s share of a premium by actuarially adjusting above or below the established base premium rates. (B) For purposes of paragraph (1), the term employer member means\u2014 (i) an employer who is a member of such group or association of employers and employs at least 1 common law employee; or (ii) a group made up solely of self-employed individuals, within which all of the self-employed individual members of such group or association are aggregated together as a single employer member group, provided the group includes at least 20 self-employed individual members. (2) In the event a group or association is made up solely of self-employed individuals (and no employers with at least 1 common law employee are members of such group or association), the employee welfare benefit plan established by such group or association shall\u2014 (A) treat all self-employed individuals who are members of such group or association as a single risk pool; (B) pool all plan participant claims; and (C) charge each plan participant the same premium rate. (b) Discrimination and pre-Existing condition protections An employee welfare benefit plan established and maintained by a group or association of employers described in section 3(5)(B) shall be prohibited from\u2014 (1) establishing any rule for eligibility (including continued eligibility) of any individual (including an employee of an employer member or a self-employed individual, or a dependent of such employee or self-employed individual) to enroll for benefits under the terms of the plan that discriminates based on any health status-related factor that relates to such individual (consistent with the rules under section 702(a)(1)); (2) requiring an individual (including an employee of an employer member or a self-employed individual, or a dependent of such employee or self-employed individual), as a condition of enrollment or continued enrollment under the plan, to pay a premium or contribution that is greater than the premium or contribution for a similarly situated individual enrolled in the plan based on any health status-related factor that relates to such individual (consistent with the rules under section 702(b)(1)); and (3) denying coverage under such plan on the basis of a pre-existing condition (consistent with the rules under section 2704 of the Public Health Service Act). .\n##### (b) Clerical amendment\nThe table of contents in section 1 of such Act is amended by inserting after the item relating to section 734 the following new items:\nSec. 735. Standardized reporting format. Sec. 736. Rules applicable to employee welfare benefit plans established and maintained by a group or association of employers. .\n#### 4. Rule of construction\nNothing in this Act shall be construed to exempt a group health plan which is an employee welfare benefit plan offered through a group or association of employers from the requirements of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 (29 U.S.C. 1181 et. seq.), including the provisions of part A of title XXVII of the Public Health Service Act as incorporated by reference into the Employee Retirement Income Security Act of 1974 through section 715 of such Act.",
      "versionDate": "2025-12-15",
      "versionType": "Reported in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-21",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1847",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Association Health Plans Act",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-06-27T17:22:05Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-06-27T17:22:05Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-06-27T17:22:05Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-06-27T17:22:05Z"
          },
          {
            "name": "Labor-management relations",
            "updateDate": "2025-06-27T17:22:05Z"
          },
          {
            "name": "Self-employed",
            "updateDate": "2025-06-27T17:22:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-04-06T14:25:18Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2528ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2528rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Association Health Plans Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-12-16T06:38:14Z"
    },
    {
      "title": "Association Health Plans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Association Health Plans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Employee Retirement Income Security Act of 1974 to clarify the treatment of certain association health plans as employers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:27Z"
    }
  ]
}
```
