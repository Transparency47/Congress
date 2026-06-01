# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8588?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8588
- Title: Housing FIRST Act
- Congress: 119
- Bill type: HR
- Bill number: 8588
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-20T20:19:08Z
- Update date including text: 2026-05-20T20:19:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8588",
    "number": "8588",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Housing FIRST Act",
    "type": "HR",
    "updateDate": "2026-05-20T20:19:08Z",
    "updateDateIncludingText": "2026-05-20T20:19:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
        "item": {
          "date": "2026-04-29T13:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MI"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NY"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "LA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NJ"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "MN"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8588ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8588\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Ms. Pressley (for herself, Ms. Tlaib , Mr. McGovern , Ms. Ocasio-Cortez , Ms. Simon , Mrs. Ramirez , Ms. Schakowsky , Mr. Johnson of Georgia , Mr. Frost , Ms. Lee of Pennsylvania , Ms. Williams of Georgia , Mrs. McIver , Ms. Clarke of New York , Mr. Carter of Louisiana , Ms. Kelly of Illinois , Ms. Kamlager-Dove , Mrs. Watson Coleman , Ms. Omar , Mr. Casar , and Mr. Gomez ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Fair Credit Reporting Act to prohibit consumer reporting agencies that furnish consumer reports for tenant screening purposes from providing certain information, to establish duties of users of consumer reports for housing purposes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing for Formerly Incarcerated Reentry and Stable Tenancy Act or the Housing FIRST Act .\n#### 2. Definition of tenant screening purposes\n##### (a) Definition of tenant screening purposes\nSection 603(h) of the Fair Credit Reporting Act ( 15 U.S.C. 1681a(h) ) is amended\u2014\n**(1)**\nby inserting Employment Purposes and Tenant Screening Purposes.\u2014 before The term ;\n**(2)**\nby striking The term and inserting the following:\n(1) Employment purposes The term ; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) Tenant screening purposes The term tenant screening purposes when used in connection with a consumer report means a report used for the purpose of evaluating a consumer for rental housing or retention as a renter or tenant. .\n##### (b) Conforming amendments\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ) is amended\u2014\n**(1)**\nin section 603\u2014\n**(A)**\nin subsection (d)(1)(B), by inserting or tenant screening purposes after employment purposes ; and\n**(B)**\nin subsection (k)\u2014\n**(i)**\nin clause (iii), by striking and at the end;\n**(ii)**\nin clause (iv)(II), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(v) a denial of housing or any other decision related to the provision of rental housing that adversely affects any current or prospective tenant or renter. ;\n**(2)**\nin section 604(a)(3)(B), by inserting or tenant screening purposes after employment purposes ;\n**(3)**\nin section 605A(i)(4)(I), by striking employment, tenant, or background screening purposes and inserting employment purposes, tenant screening purposes, or background screening purposes ;\n**(4)**\nin section 606(d)(2)\u2014\n**(A)**\nby inserting or tenant screening purposes after employment purposes ;\n**(B)**\nby striking of the consumer and inserting of the consumer, or by a housing provider or a prospective housing provider (as applicable) ; and\n**(C)**\nby inserting or fair housing after equal employment opportunity ;\n**(5)**\nin section 609(a)(3)(A)(i), by inserting or tenant screening purposes after employment purposes ; and\n**(6)**\nin section 613\u2014\n**(A)**\nin the section heading, by inserting or tenant screening purposes after employment purposes ; and\n**(B)**\nin subsection (a)\u2014\n**(i)**\nin the matter preceding paragraph (1), by inserting or tenant screening purposes after employment purposes ; and\n**(ii)**\nby inserting or rental housing, as applicable, after obtain employment each place it appears.\n#### 3. Prohibition on information included in consumer reports furnished for tenant screening purposes\nThe Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ) is amended by inserting after section 605C the following new section:\n605D. Consumer reports for tenant screening purposes A consumer reporting agency that furnishes a consumer report for tenant screening purposes shall not include any information relating to the following: (1) A record for an arrest. (2) Any juvenile adjudication or conviction, including convictions or adjudications in which a juvenile was tried as an adult. (3) Non-criminal citations by State or local law enforcement agencies. (4) Any criminal case resolved through successful completion of diversion, deferred adjudication, deferred entry of judgment, drug court, or a similar judicial program established under State law. (5) A conviction for which\u2014 (A) the consumer was sentenced and for which the consumer has completed the sentence; or (B) the consumer is on probation or parole. (6) An offense or offenses related to fees or back payments associated with court costs or incarceration. (7) A record of a conviction or arrest that has been expunged, sealed, vacated, set aside, or subject to similar relief, or any conviction for which a consumer has been pardoned or granted clemency. .\n#### 4. Conditions for furnishing and using consumer reports for tenant screening purposes\nSection 604(b) of the Fair Credit Reporting Act ( 15 U.S.C. 1681b(b) ) is amended\u2014\n**(1)**\nin the subsection heading, by inserting or tenant screening purposes after employment purposes ;\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting or tenant screening purposes after employment purposes ; and\n**(B)**\nin subparagraph (A)(ii), by inserting or fair housing after equal employment opportunity ;\n**(3)**\nin paragraph (2)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by inserting or tenant screening purposes after employment purposes ; and\n**(B)**\nin clause (i), by inserting or tenant screening purposes after employment purposes ; and\n**(4)**\nin paragraph (3)(A), by inserting or tenant screening purposes after employment purposes .\n#### 5. Clarification for sources of information\nSection 609(a)(2) of the Fair Credit Reporting Act ( 15 U.S.C. 1681g(a)(2) ) is amended by inserting (including any entity from whom the consumer reporting agency received such information) after the information .\n#### 6. Duties of users of consumer reports for housing purposes\nSection 615 of the Fair Credit Reporting Act ( 15 U.S.C. 1681m ) is amended by adding at the end the following new subsection:\n(i) Duties of users for tenant screening purposes If a person who has procured a consumer report of a consumer for tenant screening purposes or takes any adverse action, including denial of rental housing, against such consumer based wholly or in part on the report, the person\u2014 (1) shall provide to the consumer to whom the report relates a notice containing the information described in subsection (a) within 3 days after such adverse action; and (2) shall provide the specific reasons for such adverse action, including the information contained in the consumer report that resulted in the adverse action. .\n#### 7. Prohibition on State regulation of time limits for information excluded from consumer reports\nSection 625(b)(1)(E) of the Fair Credit Reporting Act ( 15 U.S.C. 1681t(b)(1)(E) ) is amended\u2014\n**(1)**\nby inserting the time after which after relating to ; and\n**(2)**\nby inserting becomes obsolete after consumer reports .\n#### 8. Additional exclusion of information from consumer reports\nSection 605(a)(5) of the Fair Credit Reporting Act ( 15 U.S.C. 1681c(a)(5) ) is amended by striking , other than records of convictions of crimes .\n#### 9. Technical amendment\nSection 615(h)(8) of the Fair Credit Reporting Act ( 15 U.S.C. 1681m(h)(8) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking this section and inserting this subsection ; and\n**(2)**\nin subparagraph (B), by striking This section and inserting This subsection .",
      "versionDate": "2026-04-29",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-20T20:19:08Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8588ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Housing FIRST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing FIRST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing for Formerly Incarcerated Reentry and Stable Tenancy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Credit Reporting Act to prohibit consumer reporting agencies that furnish consumer reports for tenant screening purposes from providing certain information, to establish duties of users of consumer reports for housing purposes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:35Z"
    }
  ]
}
```
