# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/573?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/573
- Title: A resolution expressing the need for the United States continued leadership on matters of religious freedom.
- Congress: 119
- Bill type: SRES
- Bill number: 573
- Origin chamber: Senate
- Introduced date: 2025-12-18
- Update date: 2026-03-05T13:04:51Z
- Update date including text: 2026-03-05T13:04:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-18: Introduced in Senate
- 2025-12-18 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S8926-8927)
- 2025-12-18 - IntroReferral: Submitted in Senate
- Latest action: 2025-12-18: Submitted in Senate

## Actions

- 2025-12-18 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S8926-8927)
- 2025-12-18 - IntroReferral: Submitted in Senate

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-18",
    "latestAction": {
      "actionDate": "2025-12-18",
      "text": "Submitted in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/573",
    "number": "573",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A resolution expressing the need for the United States continued leadership on matters of religious freedom.",
    "type": "SRES",
    "updateDate": "2026-03-05T13:04:51Z",
    "updateDateIncludingText": "2026-03-05T13:04:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S8926-8927)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10025",
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in Senate",
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
            "date": "2025-12-19T02:09:59Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-19T02:09:59Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NC"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "PA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "ID"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "WY"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "IN"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "AL"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "UT"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "MS"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "MO"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "NE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres573is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 573\nIN THE SENATE OF THE UNITED STATES\nDecember 18, 2025 Mr. Risch submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the need for the United States continued leadership on matters of religious freedom.\nThat the Senate\u2014\n**(1)**\nreaffirms the United States leadership around the world to promote, protect, and expand the inalienable and internationally recognized right to freedom of religion;\n**(2)**\nencourages the Secretary of State\u2014\n**(A)**\nto continue to engage on matters of religious freedom;\n**(B)**\nto use all available tools and resources to discourage foreign governments from continuing patterns of violations; and\n**(C)**\nto continue to engage on matters of religious freedom with friendly nations to prevent further erosion of religious freedom;\n**(3)**\nreaffirms the importance of the offices of the Ambassador-at-Large for International Religious Freedom and the Special Envoy to Monitor and Combat Antisemitism;\n**(4)**\nsupports the offices of the Ambassador-at-Large for International Religious Freedom and the Special Envoy to Monitor and Combat Antisemitism to work together to ensure that no faith or believer is left behind; and\n**(5)**\ncommits the United States to always support those seeking freedom from authoritarian repression against our shared and inalienable rights.",
      "versionDate": "2025-12-18",
      "versionType": "IS"
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
        "name": "International Affairs",
        "updateDate": "2026-01-06T20:04:03Z"
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
      "date": "2025-12-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres573is.xml"
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
      "title": "A resolution expressing the need for the United States continued leadership on matters of religious freedom.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T11:56:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A resolution expressing the need for the United States continued leadership on matters of religious freedom.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T11:56:24Z"
    }
  ]
}
```
