# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7882?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7882
- Title: To provide for the leasing of certain deposits of minerals located within the City of Carlsbad, New Mexico.
- Congress: 119
- Bill type: HR
- Bill number: 7882
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-04-01T16:23:16Z
- Update date including text: 2026-04-01T16:23:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-03-18 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-03-25 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7882",
    "number": "7882",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001212",
        "district": "8",
        "firstName": "Pete",
        "fullName": "Rep. Stauber, Pete [R-MN-8]",
        "lastName": "Stauber",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "To provide for the leasing of certain deposits of minerals located within the City of Carlsbad, New Mexico.",
    "type": "HR",
    "updateDate": "2026-04-01T16:23:16Z",
    "updateDateIncludingText": "2026-04-01T16:23:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-25T14:15:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-18T15:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7882ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7882\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Stauber introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo provide for the leasing of certain deposits of minerals located within the City of Carlsbad, New Mexico.\n#### 1. Leasing of certain deposits of minerals located within City of Carlsbad, New Mexico\n##### (a) In general\nNotwithstanding the exclusion in the first section of the Mineral Leasing Act ( 30 U.S.C. 181 ) or the first sentence of section 3 of the Mineral Leasing Act for Acquired Lands ( 30 U.S.C. 352 ) with respect to incorporated cities, towns, and villages, and subject to written consent provided by the City of Carlsbad, New Mexico, to the Secretary of the Interior, the Secretary may lease deposits of the minerals described in such section and such sentence that are located on covered land in accordance with the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ) or Mineral Leasing Act for Acquired Lands ( 30 U.S.C. 351 et seq. ), as applicable, and any other applicable Federal mineral leasing law.\n##### (b) Definitions\nIn this section:\n**(1) Acquired land**\nThe term acquired land has the meaning given the term acquired lands in section 2 of the Mineral Leasing Act for Acquired Lands ( 30 U.S.C. 351 ).\n**(2) Covered land**\nThe term covered land means land that\u2014\n**(A)**\nis\u2014\n**(i)**\nowned by the United States within the meaning of the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ); or\n**(ii)**\nacquired land; and\n**(B)**\nlocated within the City of Carlsbad, New Mexico.",
      "versionDate": "2026-03-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Mining",
            "updateDate": "2026-04-01T16:23:16Z"
          },
          {
            "name": "New Mexico",
            "updateDate": "2026-04-01T16:22:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2026-03-11T14:26:28Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7882ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the leasing of certain deposits of minerals located within the City of Carlsbad, New Mexico.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T08:18:33Z"
    },
    {
      "title": "To provide for the leasing of certain deposits of minerals located within the City of Carlsbad, New Mexico.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T08:05:32Z"
    }
  ]
}
```
