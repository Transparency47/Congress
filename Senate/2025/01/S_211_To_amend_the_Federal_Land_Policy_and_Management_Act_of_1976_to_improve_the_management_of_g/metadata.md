# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/211?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/211
- Title: Resiliency for Ranching and Natural Conservation Health Act
- Congress: 119
- Bill type: S
- Bill number: 211
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S336-337)
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S336-337)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/211",
    "number": "211",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Resiliency for Ranching and Natural Conservation Health Act",
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
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S336-337)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T18:20:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "SD"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "MT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "ID"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s211is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 211\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Barrasso (for himself, Mr. Risch , Mr. Rounds , Ms. Lummis , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Federal Land Policy and Management Act of 1976 to improve the management of grazing permits and leases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Resiliency for Ranching and Natural Conservation Health Act .\n#### 2. Temporary use of vacant grazing allotments for holders of grazing permits or leases during extreme natural events and disasters\nTitle IV of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1751 et seq. ) is amended by adding at the end the following:\n405. Vacant grazing allotments made available to holders of grazing permits or leases during extreme natural events and disasters (a) Definition of secretary concerned In this section, the term Secretary concerned means\u2014 (1) the Secretary of Agriculture, with respect to National Forest System land; and (2) the Secretary, with respect to public lands. (b) Allotments (1) In general The Secretary concerned may make available to the holder of a grazing permit or lease issued by either Secretary concerned the temporary use of a vacant grazing allotment if\u2014 (A) 1 or more grazing allotments covered by the grazing permit or lease of the holder of the grazing permit or lease are temporarily unusable, as determined by the Secretary concerned, because of unforeseen natural events or disasters (including an extreme weather event, drought, wildfire, infestation, or blight); and (B) the Secretary concerned determines that the vacant grazing allotment is appropriate for temporary grazing use. (2) Terms and conditions In establishing the terms and conditions in a permit or lease for the temporary use of a vacant grazing allotment made available pursuant to this subsection, the Secretary concerned\u2014 (A) shall take into consideration the terms and conditions of the most recent permit or lease that was applicable to the vacant grazing allotment; (B) if there are no terms or conditions available for consideration under subparagraph (A), may assign temporary terms or conditions, after considering ecological conditions of, or terms on, adjacent grazing allotments; (C) shall base the terms and conditions on local ecological conditions, as determined by the applicable official; (D) shall take into consideration other factors, including any prior agency agreement that resolved or sought to resolve a management conflict, including a conflict related to State management of wildlife; and (E) may authorize the placement and use of temporary rangeland improvements (including portable corrals, fencing, aboveground pipelines, and water troughs) on the vacant grazing allotment to accommodate the temporary use. (3) Coordination To the maximum extent practicable, the Secretaries concerned shall coordinate to make available to holders of grazing permits or leases the use of vacant grazing allotments, regardless of agency jurisdiction over vacant grazing allotments, pursuant to paragraphs (1) and (2). (4) Effect The temporary use of a vacant grazing allotment under this subsection shall not\u2014 (A) preclude or otherwise alter other ongoing or future actions or assessments evaluating the potential of the vacant grazing allotment to be used or otherwise assigned; or (B) alter\u2014 (i) the terms and conditions of the original grazing permit or lease of the holder of the grazing permit or lease; (ii) the preference or ability of the holder of the grazing permit or lease to return to the original allotment once access to, or the use of, the original allotment is restored; or (iii) the animal unit months in future authorizations, or conditions of a permit, of the holder of the grazing permit or lease. (c) Duration The Secretary concerned shall determine the duration of the temporary use of a vacant grazing allotment made available pursuant to subsection (b), after considering\u2014 (1) the condition of the vacant grazing allotment; and (2) the period of time necessary for the original allotment of the holder of the grazing permit or lease to return to use. (d) Guidelines (1) In general Not later than 1 year after the date of enactment of this section, the Secretary concerned shall establish guidelines to expeditiously, efficiently, and effectively carry out activities authorized under this section. (2) Considerations In establishing the guidelines under paragraph (1), the Secretary concerned may consider\u2014 (A) criteria for determining whether the vacant grazing allotment is suitable for temporary grazing use; (B) eligibility criteria for the holders of grazing permits or leases; (C) prioritizing holders of grazing permits or leases in close proximity to a vacant grazing allotment; (D) any class or change in class of livestock on the temporary use of a vacant grazing allotment, with consideration given to local ecological conditions, disease, wildlife conflicts, and other factors based on localized conditions; (E) processes for coordinating with allotments adjoining or within the vicinity of a vacant grazing allotment; and (F) any other processes intended to expedite procedures for making vacant grazing allotments available during emergent circumstances. (e) Periodic evaluations The Secretary concerned shall periodically evaluate land health conditions of vacant grazing allotments to facilitate the efficient implementation of this section. .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-07-17",
        "text": "Referred to the Committee on Natural Resources, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4513",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Resiliency for Ranching and Natural Conservation Health Act",
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
            "name": "Agricultural conservation and pollution",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Ecology",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Hunting and fishing",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Outdoor recreation",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-09-05T17:53:02Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2025-09-05T17:53:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-01T20:12:18Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s211is.xml"
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
      "title": "Resiliency for Ranching and Natural Conservation Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Resiliency for Ranching and Natural Conservation Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Land Policy and Management Act of 1976 to improve the management of grazing permits and leases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:26Z"
    }
  ]
}
```
