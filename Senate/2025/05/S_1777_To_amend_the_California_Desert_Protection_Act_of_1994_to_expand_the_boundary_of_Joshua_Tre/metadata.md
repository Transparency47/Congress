# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1777?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1777
- Title: Joshua Tree National Park Expansion Act
- Congress: 119
- Bill type: S
- Bill number: 1777
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: S2953)
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: S2953)
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1777",
    "number": "1777",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Joshua Tree National Park Expansion Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (Sponsor introductory remarks on measure: S2953)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T17:01:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:07Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1777is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1777\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Padilla introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the California Desert Protection Act of 1994 to expand the boundary of Joshua Tree National Park, to redesignate the Cottonwood Visitor Center at Joshua Tree National Park as the Dianne Feinstein Visitor Center , and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Joshua Tree National Park Expansion Act .\n#### 2. Expansion of Joshua Tree National Park\n##### (a) Boundary adjustment\nSection 402 of the California Desert Protection Act of 1994 ( 16 U.S.C. 410aaa\u201322 ) is amended, in the first sentence, by inserting after October 1991 or prior, the following: and including the approximately 20,149 acres of land generally depicted on the map entitled Joshua Tree National Park Proposed Boundary Addition , numbered 156/193,676, and dated June 2024 .\n##### (b) Transfer of administrative jurisdiction\nAdministrative jurisdiction over the land described in the amendment made by subsection (a) is transferred from the Bureau of Land Management to the National Park Service.\n##### (c) Land acquisition\n**(1) In general**\nSubject to paragraph (2), the Secretary of the Interior may acquire land and interests in land within the boundary of the Joshua Tree National Park by\u2014\n**(A)**\ndonation;\n**(B)**\npurchase from a willing seller;\n**(C)**\nexchange; or\n**(D)**\ntransfer.\n**(2) Limitation**\nAny land or interest land within the boundary of the Joshua Tree National Park that is owned by the State of California or a political subdivision of the State of California may only be acquired by the Secretary of the Interior by donation or exchange.\n#### 3. Technical correction\nSection 1433(a) of the John D. Dingell, Jr. Conservation, Management, and Recreation Act ( Public Law 116\u20139 ; 133 Stat. 700) is amended by striking 156/149,375 each place it appears and inserting 156/149,375A .\n#### 4. Redesignation of the Cottonwood Visitor Center at Joshua Tree National Park as the Dianne Feinstein Visitor Center\n##### (a) Redesignation\nThe Cottonwood Visitor Center at Joshua Tree National Park, or any successor to that visitor center, shall be known and designated as the Dianne Feinstein Visitor Center .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the visitor center referred to in subsection (a) shall be deemed to be a reference to the Dianne Feinstein Visitor Center .",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-05-14",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "3414",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Joshua Tree National Park Expansion Act",
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
            "name": "California",
            "updateDate": "2025-12-12T20:49:09Z"
          },
          {
            "name": "Land transfers",
            "updateDate": "2025-12-12T20:49:09Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-12T20:49:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-18T15:12:37Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1777is.xml"
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
      "title": "Joshua Tree National Park Expansion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Joshua Tree National Park Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the California Desert Protection Act of 1994 to expand the boundary of Joshua Tree National Park, to redesignate the Cottonwood Visitor Center at Joshua Tree National Park as the \"Dianne Feinstein Visitor Center\", and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:23Z"
    }
  ]
}
```
