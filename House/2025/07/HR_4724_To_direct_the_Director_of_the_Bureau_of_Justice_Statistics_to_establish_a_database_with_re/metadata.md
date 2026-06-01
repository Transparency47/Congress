# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4724
- Title: Corporate Crime Database Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4724
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-13T08:05:59Z
- Update date including text: 2026-05-13T08:05:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-23 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4724",
    "number": "4724",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary Gay",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Corporate Crime Database Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:05:59Z",
    "updateDateIncludingText": "2026-05-13T08:05:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:08:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-23T14:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "DC"
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
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
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
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4724ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4724\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Scanlon (for herself, Ms. Norton , Mr. Johnson of Georgia , Ms. Tlaib , Ms. Jayapal , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Director of the Bureau of Justice Statistics to establish a database with respect to corporate offenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Corporate Crime Database Act of 2025 .\n#### 2. Corporate crime database at the Bureau of Justice Statistics\n##### (a) In general\nPart C of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10131 et seq. ) is amended by adding at the end the following:\n305. Corporate crime database (a) Definitions In this section: (1) Business entity The term business entity means a corporation, association, partnership, limited liability company, limited liability partnership, or other legal entity. (2) Corporate offense The term corporate offense means\u2014 (A) a violation or alleged violation of Federal law committed by\u2014 (i) a business entity; or (ii) an individual employed by a business entity within the conduct of the individual's occupational role; and (B) any other violation determined by the Director to be a corporate offense. (3) Director The term Director means the Director of the Bureau. (4) Enforcement action The term enforcement action includes any concluded administrative, civil, or criminal enforcement action or any declination, settlement, deferred prosecution agreement, or non-prosecution agreement entered into by a Federal agency to enforce a law or regulation. (5) Federal agency The term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code. (b) Establishment Beginning not later than 1 year after the date of enactment of the Corporate Crime Database Act of 2025 , the Director shall\u2014 (1) collect, aggregate, and analyze information regarding enforcement actions taken with respect to corporate offenses; and (2) publish on the internet website of the Bureau a database of the enforcement actions described in paragraph (1). (c) Information included The database established under subsection (b) shall include the following information on an enforcement action with respect to corporate offenses: (1) Each business entity or individual identified by the enforcement action. (2) The employer of an individual identified under paragraph (1), as determined relevant by the Director. (3) The parent company of a business entity identified under paragraph (1) or the parent company of any employer identified under paragraph (2), as determined relevant by the Director. (4) The type of offense or alleged offense committed by the business entity or individual. (5) Any relevant statute or regulation violated by the business entity or individual. (6) Each Federal agency bringing the enforcement action. (7) The outcome of the enforcement action, if any, including all documentation relevant to the outcome. (8) An unique identifier for each business entity, individual, employer, or parent company identified by the enforcement action. (9) Any additional information the Director determines necessary to carry out the purposes of this section. (d) Information collection by Director (1) In general Not later than 180 days after the date of enactment of the Corporate Crime Database Act of 2025 , the Director shall establish guidance for the collection of information from each Federal agency that carries out an enforcement action with respect to corporate offenses, including identification of each Federal agency that shall submit information to the Director and the manner in which, time at which, and frequency with which the information shall be submitted. (2) Cooperation by Federal agencies Each Federal agency identified in the guidance established under paragraph (1) shall submit to the Director the information specified by the Director, in accordance with that guidance. (3) Timing of information included To the extent to which information is available, the database established under subsection (b) shall include the information described in subsection (c) on each enforcement action with respect to corporate offenses taken by a Federal agency before, on, or after the date of enactment of the Corporate Crime Database Act of 2025 . (e) Publication details (1) In general Not later than 1 year after the date of enactment of the Corporate Crime Database Act of 2025 , the Director shall publish on the internet website of the Bureau the database established under subsection (b) in a format that is searchable, downloadable, and accessible to the public. (2) Update of information The Director shall update the information included in the database established under subsection (b) each time the information is collected under subsection (d). (f) Report required Not later than 1 year after the publication of the database established under subsection (b), and annually thereafter, the Director shall submit to Congress a report including\u2014 (1) a description of the data collected and analyzed under this section related to corporate offenses, including an analysis of recidivism, offenses and alleged offenses, and enforcement actions; (2) an estimate of the impact of corporate offenses on victims and the public; and (3) recommendations, developed in consultation with the Attorney General, for legislative or administrative actions to improve the ability of Federal agencies to monitor, respond to, and deter instances of corporate offenses. .\n##### (b) Chief Data Officer Council\nSection 3520A(b) of title 44, United States Code, is amended\u2014\n**(1)**\nin paragraph (4), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(6) identify ways in which a Federal agency (as defined in section 305 of title I of the Omnibus Crime Control and Safe Streets Act of 1968) that carries out an enforcement action (as defined in that section) with respect to a corporate offense (as defined in that section) can improve the collection, digitalization, tabulation, sharing, and publishing of information under that section, and the standardization of those processes, in order to carry out that section. .",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-03-16",
        "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S1057)"
      },
      "number": "4104",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Corporate Crime Database Act of 2026",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-12T14:18:09Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4724ih.xml"
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
      "title": "Corporate Crime Database Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Corporate Crime Database Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the Bureau of Justice Statistics to establish a database with respect to corporate offenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:20Z"
    }
  ]
}
```
