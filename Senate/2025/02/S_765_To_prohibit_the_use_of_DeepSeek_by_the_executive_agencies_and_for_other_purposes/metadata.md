# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/765?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/765
- Title: No DeepSeek on Government Devices Act
- Congress: 119
- Bill type: S
- Bill number: 765
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T21:46:21Z
- Update date including text: 2025-12-05T21:46:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/765",
    "number": "765",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "No DeepSeek on Government Devices Act",
    "type": "S",
    "updateDate": "2025-12-05T21:46:21Z",
    "updateDateIncludingText": "2025-12-05T21:46:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-27T16:20:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s765is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 765\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Ms. Rosen (for herself, Mr. Husted , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit the use of DeepSeek by the executive agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No DeepSeek on Government Devices Act .\n#### 2. Prohibition on the use of DeepSeek\n##### (a) Definitions\nIn this section:\n**(1) Covered application**\nThe term covered application means the DeepSeek application or any successor application or service developed or provided by High Flyer or an entity owned by High Flyer.\n**(2) Executive agency**\nThe term executive agency has the meaning given that term in section 133 of title 41, United States Code.\n**(3) Information technology**\nThe term information technology has the meaning given that term in section 11101 of title 40, United States Code.\n##### (b) Prohibition on the use of DeepSeek\n**(1) In general**\nNot later than 60 days after the date of enactment of this Act, the Director of the Office of Management and Budget, in consultation with the Administrator of General Services, the Director of the Cybersecurity and Infrastructure Security Agency, the Director of National Intelligence, and the Secretary of Defense, and consistent with the information security requirements under subchapter II of chapter 35 of title 44, United States Code, shall develop standards and guidelines for executive agencies that require the removal of any covered application from information technology.\n**(2) National security and research exceptions**\nThe standards and guidelines developed under paragraph (1) shall include\u2014\n**(A)**\nexceptions for law enforcement activities, national security interests and activities, and security researchers; and\n**(B)**\nfor any authorized use of a covered application under an exception, requirements for executive agencies to develop and document risk mitigation actions for such use.",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-07",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1121",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No DeepSeek on Government Devices Act",
      "type": "HR"
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
            "name": "Computer security and identity theft",
            "updateDate": "2025-06-09T17:52:03Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-09T17:52:03Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-09T17:52:03Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-09T17:52:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-12T14:53:53Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s765is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "No DeepSeek on Government Devices Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No DeepSeek on Government Devices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the use of DeepSeek by the executive agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:51Z"
    }
  ]
}
```
