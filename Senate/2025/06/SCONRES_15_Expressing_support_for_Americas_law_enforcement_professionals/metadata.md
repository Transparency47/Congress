# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sconres/15?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/15
- Title: A concurrent resolution expressing support for America's law enforcement professionals.
- Congress: 119
- Bill type: SCONRES
- Bill number: 15
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-05-29T02:59:31Z
- Update date including text: 2026-05-29T02:59:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-06-18 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S3478; text: CR S3477)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:26 - Floor: Received in the House.
- 2025-06-23 15:29:07 - Floor: Held at the desk.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-06-18 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S3478; text: CR S3477)
- 2025-06-23 - Floor: Message on Senate action sent to the House.
- 2025-06-23 15:19:26 - Floor: Received in the House.
- 2025-06-23 15:29:07 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-concurrent-resolution/15",
    "number": "15",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A concurrent resolution expressing support for America's law enforcement professionals.",
    "type": "SCONRES",
    "updateDate": "2026-05-29T02:59:31Z",
    "updateDateIncludingText": "2026-05-29T02:59:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-06-23",
      "actionTime": "15:29:07",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-06-23",
      "actionTime": "15:19:26",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S3478; text: CR S3477)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "AL"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "WV"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "AK"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "UT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NM"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "PA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "TN"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "OK"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "NH"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "MT"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-18",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres15es.xml",
      "text": "119th CONGRESS\n1st Session\nS. CON. RES. 15\nIN THE SENATE OF THE UNITED STATES\nCONCURRENT RESOLUTION\nExpressing support for America\u2019s law enforcement professionals.\nThat Congress\u2014\n**(1)**\nhighly respects and values United States law enforcement professionals and greatly appreciates all that those officers do to protect and serve our communities;\n**(2)**\nremembers and honors those officers and their families who have experienced a death or injury in the line of duty;\n**(3)**\ncalls for increased measures to be taken to maximize the safety and well-being of officers, including more policing personnel, improved training and equipment, tough penalties for assaulting or killing a law enforcement professional, and increased mental health resources for officers; and\n**(4)**\ncalls on all levels of government to ensure that law enforcement professionals receive the support and resources needed to keep the United States safe.",
      "versionDate": "",
      "versionType": "ES"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres15ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. CON. RES. 15\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Cassidy (for himself, Mrs. Britt , Mr. Justice , Mr. Sullivan , Mr. Lee , Mr. Luj\u00e1n , Mr. Fetterman , Mr. Hagerty , Mr. Mullin , Ms. Hassan , Mr. Sheehy , and Mr. Moreno ) submitted the following concurrent resolution; which was considered and agreed to\nCONCURRENT RESOLUTION\nExpressing support for America\u2019s law enforcement professionals.\nThat Congress\u2014\n**(1)**\nhighly respects and values United States law enforcement professionals and greatly appreciates all that those officers do to protect and serve our communities;\n**(2)**\nremembers and honors those officers and their families who have experienced a death or injury in the line of duty;\n**(3)**\ncalls for increased measures to be taken to maximize the safety and well-being of officers, including more policing personnel, improved training and equipment, tough penalties for assaulting or killing a law enforcement professional, and increased mental health resources for officers; and\n**(4)**\ncalls on all levels of government to ensure that law enforcement professionals receive the support and resources needed to keep the United States safe.",
      "versionDate": "2025-06-18",
      "versionType": "ATS"
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "31",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for America's law enforcement professionals.",
      "type": "HCONRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-12",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "98",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for America's law enforcement professionals.",
      "type": "HCONRES"
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
            "name": "Congressional tributes",
            "updateDate": "2025-07-03T16:24:06Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-03T16:23:54Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-07-03T16:23:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-03T13:35:53Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres15es.xml"
        }
      ],
      "type": "ES"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sconres/BILLS-119sconres15ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A concurrent resolution expressing support for America's law enforcement professionals.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T10:56:27Z"
    },
    {
      "title": "A concurrent resolution expressing support for America's law enforcement professionals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T10:56:27Z"
    }
  ]
}
```
