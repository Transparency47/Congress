# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/827?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/827
- Title: Supporting Rural Veterans Access to Healthcare Services Act
- Congress: 119
- Bill type: S
- Bill number: 827
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2026-03-19T11:03:26Z
- Update date including text: 2026-03-19T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- 2025-07-30 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/827",
    "number": "827",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001096",
        "district": "",
        "firstName": "Kevin",
        "fullName": "Sen. Cramer, Kevin [R-ND]",
        "lastName": "Cramer",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Supporting Rural Veterans Access to Healthcare Services Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:26Z",
    "updateDateIncludingText": "2026-03-19T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-04",
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
            "date": "2025-07-30T20:00:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-21T20:00:22Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:22Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-04T15:53:21Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-04",
      "state": "ME"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AK"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "SD"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s827is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 827\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Cramer (for himself, Mr. King , and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo extend and modify the transportation grant program of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supporting Rural Veterans Access to Healthcare Services Act .\n#### 2. Extension and modification of transportation grant program of Department of Veterans Affairs\nSection 307 of the Caregivers and Veterans Omnibus Health Services Act of 2010 ( Public Law 111\u2013163 ; 38 U.S.C. 1710 note) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2), by adding at the end the following new subparagraphs:\n(C) Tribal organizations. (D) Native Hawaiian organizations. ;\n**(B)**\nin paragraph (3), by striking State veterans service agency or veterans service organization awarded and inserting recipient of ; and\n**(C)**\nby amending paragraph (4) to read as follows:\n(4) Maximum amount (A) In general Except as provided in subparagraph (B), the amount of a grant under this section may not exceed $50,000. (B) Additional amount In the case of a county that has more than five communities that are off the road system, the amount of a grant awarded with respect to that county under this section may be increased by an amount not to exceed 50 percent of the amount specified in subparagraph (A). ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby redesignating paragraph (2) as paragraph (4); and\n**(B)**\nby inserting after paragraph (1) the following new paragraphs:\n(2) Native Hawaiian organization The term Native Hawaiian organization has the meaning given that term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ). (3) Tribal organization The term Tribal organization has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ). ; and\n**(3)**\nin subsection (d), by striking $3,000,000 for each of fiscal years 2010 through 2022 and inserting such sums as may be necessary for each of fiscal years 2025 through 2029 .",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in Senate"
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
            "name": "Alaska Natives and Hawaiians",
            "updateDate": "2025-06-03T15:59:05Z"
          },
          {
            "name": "Social work, volunteer service, charitable organizations",
            "updateDate": "2025-06-03T15:59:14Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-06-03T15:58:16Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-03T15:58:22Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-06-03T15:59:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-08T13:31:42Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s827is.xml"
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
      "title": "Supporting Rural Veterans Access to Healthcare Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Rural Veterans Access to Healthcare Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to extend and modify the transportation grant program of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:03:30Z"
    }
  ]
}
```
