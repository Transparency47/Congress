# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5523?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5523
- Title: Let Experienced Pilots Fly Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5523
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2025-12-17T16:30:55Z
- Update date including text: 2025-12-17T16:30:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-20 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-20 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5523",
    "number": "5523",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Let Experienced Pilots Fly Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-17T16:30:55Z",
    "updateDateIncludingText": "2025-12-17T16:30:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-20",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-20T21:47:42Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5523ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5523\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Nehls introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to raise the retirement age for pilots engaged in commercial aviation operations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Let Experienced Pilots Fly Act of 2025 .\n#### 2. Increased retirement age for pilots\nSection 44729 of title 49, United States Code, as amended by section 107 of division Q of the Consolidated Appropriations Act, 2023 ( Public Law 117\u2013328 ), is further amended to read as follows:\n44729. Age standards for pilots (a) In general A pilot may serve in multicrew covered operations until 67 years of age. (b) Covered operations defined In this section, the term covered operations means operations under part 121 of title 14, Code of Federal Regulations, unless the operation takes place in\u2014 (1) the territorial airspace of a foreign country where such operations are prohibited by the foreign country; or (2) international airspace where such operations are not in compliance with the Annexes to the Convention on International Civil Aviation. (c) Regulations On and after the date of enactment of the Let Experienced Pilots Fly Act of 2025 , subsections (d) and (e) of section 121.383 of title 14, Code of Federal Regulations, shall be deemed to have been amended to increase the age listed in such subsections to 67 years of age. (d) Applicability (1) Retroactivity A pilot who is over 65 years of age on the date of enactment of this bill may return to service in multicrew covered operations until 67 years of age. (2) Protection for compliance An action taken in conformance with this section, taken in conformance with a regulation issued to carry out this section, or taken prior to the date of enactment of the Let Experienced Pilots Fly Act of 2025 in conformance with subsection (d) or (e) of section 121.383 of title 14, Code of Federal Regulations (as in effect before such date), may not serve as a basis for liability or relief in a proceeding, brought under any employment law or regulation, before any court or agency of the United States or of any State or locality. (e) Amendments to labor agreements and benefit plans Any amendment to a labor agreement or benefit plan of an air carrier that is required to conform with the requirements of this section or a regulation issued to carry out this section, and is applicable to pilots represented for collective bargaining, shall be made by agreement of the air carrier and the designated bargaining representative of the pilots of the air carrier. (f) Medical standards and records (1) Medical examinations and standards Except as provided by paragraph (2), a person serving as a pilot for an air carrier engaged in covered operations shall not be subject to different medical standards, or different, greater, or more frequent medical examinations, on account of age unless the Administrator of the Federal Aviation Administration determines (based on data received or studies published after the date of enactment of the Let Experienced Pilots Fly Act of 2025 ) that different medical standards, or different, greater, or more frequent medical examinations, are needed to ensure an adequate level of safety in flight. (2) Duration of first-class medical certificate No person who has attained 60 years of age may serve as a pilot of an air carrier engaged in covered operations unless the person has a first-class medical certificate. Such a certificate shall expire on the last day of the 6-month period following the date of examination shown on the certificate. (g) Safety training Each air carrier engaged in covered operations shall continue to use pilot training and qualification programs approved by the Federal Aviation Administration. (h) Report Not later than 180 days after the date of enactment of this Act, the Administrator of the Federal Aviation Administration shall submit to the appropriate congressional committees a report on further increasing the age limitation described in subsection (a). .",
      "versionDate": "2025-09-19",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-17T16:30:55Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5523ih.xml"
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
      "title": "Let Experienced Pilots Fly Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Let Experienced Pilots Fly Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to raise the retirement age for pilots engaged in commercial aviation operations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:22Z"
    }
  ]
}
```
