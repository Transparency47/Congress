# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1167?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1167
- Title: Expressing support for the designation of the month of April 2026 as "Parkinson's Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 1167
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-05-08T18:12:40Z
- Update date including text: 2026-05-08T18:12:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-14 - IntroReferral: Submitted in House
- Latest action: 2026-04-14: Submitted in House

## Actions

- 2026-04-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-04-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1167",
    "number": "1167",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Expressing support for the designation of the month of April 2026 as \"Parkinson's Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-05-08T18:12:40Z",
    "updateDateIncludingText": "2026-05-08T18:12:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-04-14T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1167ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1167\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Bell (for himself and Mr. Bilirakis ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of the month of April 2026 as Parkinson\u2019s Awareness Month .\nThat the House of Representatives\u2014\n**(1)**\nexpresses support for the designation of Parkinson\u2019s Awareness Month ;\n**(2)**\nsupports the goals and ideals of Parkinson\u2019s Awareness Month;\n**(3)**\ncontinues to support research to find better treatments and a cure for Parkinson\u2019s disease;\n**(4)**\nrecognizes the individuals living with Parkinson\u2019s disease who participate in vital clinical trials to advance the knowledge of the disease; and\n**(5)**\ncommends the dedication of organizations, volunteers, researchers, and millions of individuals across the United States working to improve the quality of life of people living with Parkinson\u2019s disease and their families.",
      "versionDate": "2026-04-14",
      "versionType": "IH"
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
        "actionDate": "2026-04-28",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S2076-2077; text: CR S2085-2086)"
      },
      "number": "696",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of the month of April 2026 as \"Parkinson's Awareness Month\".",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-24",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "345",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for designation of the month of April 2025 as \"Parkinsons Awareness Month\".",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-30",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S2719)"
      },
      "number": "194",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of the month of April 2025 as \"Parkinson's Awareness Month\".",
      "type": "SRES"
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
            "updateDate": "2026-05-01T18:10:47Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2026-05-01T18:10:47Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2026-05-01T18:10:47Z"
          },
          {
            "name": "Research administration and funding",
            "updateDate": "2026-05-01T18:10:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-04-20T19:18:50Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1167ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for the designation of the month of April 2026 as \"Parkinson's Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-15T08:18:31Z"
    },
    {
      "title": "Expressing support for the designation of the month of April 2026 as \"Parkinson's Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T08:05:53Z"
    }
  ]
}
```
