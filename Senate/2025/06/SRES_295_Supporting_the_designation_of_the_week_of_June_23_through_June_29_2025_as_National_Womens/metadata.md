# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/295?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/295
- Title: A resolution supporting the designation of the week of June 23 through June 29, 2025, as "National Women's Sports Week" to celebrate the anniversary of the enactment of title IX of the Education Amendments of 1972 and the growth of women's sports.
- Congress: 119
- Bill type: SRES
- Bill number: 295
- Origin chamber: Senate
- Introduced date: 2025-06-23
- Update date: 2025-12-06T06:59:00Z
- Update date including text: 2025-12-06T06:59:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in Senate
- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S3494)
- 2025-06-24 - Floor: Star Print ordered on the resolution.
- Latest action: 2025-06-23: Introduced in Senate

## Actions

- 2025-06-23 - IntroReferral: Introduced in Senate
- 2025-06-23 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S3494)
- 2025-06-24 - Floor: Star Print ordered on the resolution.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/295",
    "number": "295",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "A resolution supporting the designation of the week of June 23 through June 29, 2025, as \"National Women's Sports Week\" to celebrate the anniversary of the enactment of title IX of the Education Amendments of 1972 and the growth of women's sports.",
    "type": "SRES",
    "updateDate": "2025-12-06T06:59:00Z",
    "updateDateIncludingText": "2025-12-06T06:59:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the resolution.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S3494)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T22:00:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "ND"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "OK"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "AL"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "ID"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "ID"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "AL"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "MS"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "MO"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "WV"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "IN"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "MS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-06-30",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres295is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 295\nIN THE SENATE OF THE UNITED STATES\nJune 23, 2025 Ms. Ernst (for herself, Mr. Cramer , Mr. Lankford , Mr. Tuberville , Mr. Risch , Mr. Crapo , Mrs. Britt , Mrs. Hyde-Smith , and Mr. Hawley ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nSupporting the designation of the week of June 23 through June 29, 2025, as National Women\u2019s Sports Week to celebrate the anniversary of the enactment of title IX of the Education Amendments of 1972 and the growth of women\u2019s sports.\nThat the Senate supports\u2014\n**(1)**\nobserving National Women\u2019s Sports Week as the week of June 23 through June 29, 2025, to recognize\u2014\n**(A)**\nthe incredible expansion of opportunities for female athletes since the enactment of title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ); and\n**(B)**\nthe role of the provisions of law described in subparagraph (A) in guaranteeing equal athletic opportunities for members of both sexes; and\n**(2)**\nmarking the observance of National Women\u2019s Sports Week with\u2014\n**(A)**\nappropriate programs and activities that\u2014\n**(i)**\ncelebrate the contributions of individual female athletes in the United States;\n**(ii)**\nhonor the coaches and parents who support female athletes in the United States;\n**(iii)**\npromote equal access to athletic opportunities for members of both sexes; and\n**(iv)**\nsupport the commitment of the United States to supporting female athletes; and\n**(B)**\nlegislative efforts to protect single-sex sports.",
      "versionDate": "2025-06-12",
      "versionType": "IS"
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
        "actionDate": "2025-06-23",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "536",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the designation of the week including June 23, 2025, as \"National Women's Sports Week\" to celebrate the anniversary of the passage of title IX and the growth of women's sports.",
      "type": "HRES"
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
            "name": "Commemorative events and holidays",
            "updateDate": "2025-07-14T14:22:08Z"
          },
          {
            "name": "School athletics",
            "updateDate": "2025-07-14T14:22:14Z"
          },
          {
            "name": "Women's rights",
            "updateDate": "2025-07-14T14:21:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-07-09T15:19:59Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres295is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution supporting the designation of the week of June 23 through June 29, 2025, as \"National Women's Sports Week\" to celebrate the anniversary of the enactment of title IX of the Education Amendments of 1972 and the growth of women's sports.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:19Z"
    },
    {
      "title": "A resolution supporting the designation of the week of June 23 through June 29, 2025, as \"National Women's Sports Week\" to celebrate the anniversary of the enactment of title IX of the Education Amendments of 1972 and the growth of women's sports.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-24T10:56:19Z"
    }
  ]
}
```
