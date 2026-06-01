# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3259
- Title: RECAPTURE Act
- Congress: 119
- Bill type: S
- Bill number: 3259
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-04-14T11:03:26Z
- Update date including text: 2026-04-14T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3259",
    "number": "3259",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
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
    "title": "RECAPTURE Act",
    "type": "S",
    "updateDate": "2026-04-14T11:03:26Z",
    "updateDateIncludingText": "2026-04-14T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
            "date": "2025-11-20T19:12:32Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-20T19:12:32Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "TX"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "UT"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-06",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3259is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3259\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Ms. Ernst (for herself and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend the Infrastructure Investment and Jobs Act to require remaining funds under the Broadband Equity, Access, and Deployment Program to be used for deficit reduction.\n#### 1. Short title\nThis Act may be cited as the Recovering Excess Communications Appropriations while Protecting Telecommunications Upgrades, Reinvestment, and Expansion Act or the RECAPTURE Act .\n#### 2. Use of remaining BEAD funds for deficit reduction\n##### (a) In general\nSection 60102(e)(4) of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702(e)(4) ) is amended\u2014\n**(1)**\nin subparagraph (D)(ii)(III), by striking , shall make available to the eligible entity the remainder of the grant funds allocated to the eligible entity under subsection (c); and inserting the following:\n, shall, with respect to the remainder of the grant funds allocated to the eligible entity under subsection (c)\u2014 (aa) make available to the eligible entity the portion of those remaining funds that have been designated for a specific purpose in the final proposal; and (bb) deposit in the general fund of the Treasury, for the sole purpose of deficit reduction, the portion of those remaining funds that have not been designated for a specific purpose in the final proposal; ; and\n**(2)**\nin subparagraph (E)(ii)(III), by striking , shall make available to the eligible entity the remainder of the grant funds allocated to the eligible entity under subsection (c); and inserting the following:\n, shall, with respect to the remainder of the grant funds allocated to the eligible entity under subsection (c)\u2014 (aa) make available to the eligible entity the portion of those remaining funds that have been designated for a specific purpose in the final proposal; and (bb) deposit in the general fund of the Treasury, for the sole purpose of deficit reduction, the portion of those remaining funds that have not been designated for a specific purpose in the final proposal; .\n##### (b) Technical and conforming amendments\nSection 60102 of the Infrastructure Investment and Jobs Act ( 47 U.S.C. 1702 ) is amended\u2014\n**(1)**\nin subsection (c)(5)(C)\u2014\n**(A)**\nby striking clause (ii);\n**(B)**\nby striking Reallocation to other eligible entities .\u2014 and all that follows through The Assistant Secretary and inserting Reallocation to other eligible entities due to application failures .\u2014The Assistant Secretary ;\n**(C)**\nby redesignating subclauses (I) and (II) as clauses (i) and (ii), respectively, and adjusting the margins accordingly; and\n**(D)**\nin clause (ii), as so redesignated, by striking subclause (I) of this clause and inserting clause (i) of this subparagraph ; and\n**(2)**\nin subsection (e)(4)(A)(i), in the matter preceding subclause (I), by striking approvals and inserting approves .",
      "versionDate": "2025-11-20",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-19T16:38:24Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3259is.xml"
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
      "title": "RECAPTURE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RECAPTURE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recovering Excess Communications Appropriations while Protecting Telecommunications Upgrades, Reinvestment, and Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Infrastructure Investment and Jobs Act to require remaining funds under the Broadband Equity, Access, and Deployment Program to be used for deficit reduction.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T06:33:37Z"
    }
  ]
}
```
