# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3211?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3211
- Title: Recognizing the Role of Direct Support Professionals Act
- Congress: 119
- Bill type: S
- Bill number: 3211
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3211",
    "number": "3211",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Recognizing the Role of Direct Support Professionals Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:19Z",
    "updateDateIncludingText": "2026-03-20T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
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
        "item": [
          {
            "date": "2025-11-19T20:09:20Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-19T20:09:20Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ME"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AK"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-11-19",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MD"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "DE"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "DE"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3211is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3211\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Ms. Hassan (for herself, Ms. Collins , Ms. Murkowski , Mrs. Gillibrand , Mr. King , Mrs. Shaheen , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the Office of Management and Budget to consider revising the Standard Occupational Classification system to establish a separate code for direct support professionals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Recognizing the Role of Direct Support Professionals Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nDirect support professionals play a critical role in the care provided to individuals with intellectual and developmental disabilities by providing a wide range of supportive services on a day-to-day basis to promote independence, including\u2014\n**(A)**\nenhancing independence and community inclusion of these individuals, including through travel and recreation, visiting friends and family, shopping, or socializing;\n**(B)**\ncoaching and supporting individuals in communicating needs, achieving self-expression, pursuing personal goals, living independently, and participating actively in employment or voluntary roles in the community;\n**(C)**\nproviding assistance with activities of independent daily living (such as feeding, bathing, toileting, and ambulation) and with tasks such as meal preparation, shopping, light housekeeping, laundry, and home management; or\n**(D)**\nsupporting individuals at home, work, school, or any other community setting.\n**(2)**\nThrough the support of direct support professionals, individuals are able to lead self-directed lives within their own communities.\n**(3)**\nProviders of home- and community-based services are experiencing difficulty hiring and retaining direct support professionals, with a national turnover rate of 39 percent, as identified in a 2023 study by the National Core Indicators.\n**(4)**\nHigh turnover rates can lead to instability for individuals receiving services, and this may result in individuals not receiving enough personalized care to help them reach their goals for independent living.\n**(5)**\nA discrete occupational category for direct support professionals will help States and the Federal Government\u2014\n**(A)**\nbetter interpret the shortage in the labor market of direct support professionals; and\n**(B)**\ncollect data on the high turnover rate of direct support professionals.\n**(6)**\nThe Standard Occupational Classification system is designed and maintained solely for statistical purposes, and is used by Federal statistical agencies to classify workers and jobs into occupational categories for the purpose of collecting, calculating, analyzing, or disseminating data.\n**(7)**\nOccupations in the Standard Occupational Classification system are classified based on work performed and, in some cases, on the skills, education, or training needed to perform the work.\n**(8)**\nEstablishing a discrete occupational category for direct support professionals will\u2014\n**(A)**\ncorrect an inaccurate representation in the Standard Occupational Classification system;\n**(B)**\nrecognize these professionals for the critical and often overlooked work that they perform for the disabled community, which work is different than the work of a home health aide or a personal care aide; and\n**(C)**\nbetter align the Standard Occupational Classification system with related classification systems.\n#### 3. Revision of standard occupational classification system\nThe Director of the Office of Management and Budget shall, as part of the first revision of the Standard Occupational Classification system occurring after the date of enactment of this Act, consider revising the Standard Occupational Classification system to establish a separate code for direct support professionals as a healthcare support occupation.\n#### 4. Report to Congress\nIf, after carrying out section 3, the Director of the Office of Management and Budget decides not to establish a separate code for direct support professionals in the Standard Occupational Classification system, the Director shall, by not later than 30 days after the first revision of the Standard Occupational Classification system occurring after the date of enactment of this Act, submit a report to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Education and Workforce of the House of Representatives explaining the Office of Management and Budget\u2019s decision.\n#### 5. No new funds\nNo additional funds are authorized to be appropriated to carry out this Act.",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-11-19",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6137",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the Role of Direct Support Professionals Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-12-19T17:01:36Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3211is.xml"
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
      "title": "Recognizing the Role of Direct Support Professionals Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recognizing the Role of Direct Support Professionals Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Office of Management and Budget to consider revising the Standard Occupational Classification system to establish a separate code for direct support professionals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:18Z"
    }
  ]
}
```
