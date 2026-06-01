# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2404?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2404
- Title: A bill to subject emergency legislation enacted by the District of Columbia Council to expedited congressional disapproval procedures.
- Congress: 119
- Bill type: S
- Bill number: 2404
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-05-19T10:56:42Z
- Update date including text: 2026-05-19T10:56:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2404",
    "number": "2404",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to subject emergency legislation enacted by the District of Columbia Council to expedited congressional disapproval procedures.",
    "type": "S",
    "updateDate": "2026-05-19T10:56:42Z",
    "updateDateIncludingText": "2026-05-19T10:56:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
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
            "date": "2025-07-23T18:17:00Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-23T18:17:00Z",
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
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2404is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2404\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo subject emergency legislation enacted by the District of Columbia Council to expedited congressional disapproval procedures.\n#### 1. Congressional disapproval of emergency District of Columbia legislation\nThe District of Columbia Home Rule Act is amended\u2014\n**(1)**\nin section 412(a) (sec. 1\u2013204.12(a), D.C. Official Code), in the fifth sentence, by inserting after ninety days the following: , unless a joint resolution of disapproval is enacted under section 604 before the expiration of that period ; and\n**(2)**\nin section 602(c) (sec. 1\u2013206.02(c), D.C. Official Code)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the first sentence, by striking any act which the Council determines, according to section 412(a), should take effect immediately because of emergency circumstances, ; and\n**(ii)**\nin the second sentence, by striking paragraph (2) and inserting paragraphs (2) and (3) ;\n**(B)**\nby redesignating paragraph (3) as paragraph (4); and\n**(C)**\nby inserting after paragraph (2) the following:\n(3) (A) In the case of any such Act transmitted by the Chairman which the Council determines according to section 412(a) should take effect immediately because of emergency circumstances, the Act shall take effect immediately upon enactment. (B) The Chairman of the Council shall transmit an Act described in subparagraph (A) to\u2014 (i) the Speaker of the House of Representatives not later than 3 session days (with respect to the House of Representatives) after the date of enactment of the Act; and (ii) the President of the Senate not later than 3 session days (with respect to the Senate) after the date of enactment of the Act. .",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4670",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To subject emergency legislation enacted by the District of Columbia Council to expedited congressional disapproval procedures.",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-12T20:14:43Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2404is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to subject emergency legislation enacted by the District of Columbia Council to expedited congressional disapproval procedures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:32Z"
    },
    {
      "title": "A bill to subject emergency legislation enacted by the District of Columbia Council to expedited congressional disapproval procedures.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T10:56:18Z"
    }
  ]
}
```
