# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3743?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3743
- Title: A bill to direct the Secretary of the Interior to carry out a feasibility study on a selective water withdrawal system at Glen Canyon Dam, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 3743
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-04-15T01:32:18Z
- Update date including text: 2026-04-15T01:32:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2026-03-17 - Committee: Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3743",
    "number": "3743",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
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
    "title": "A bill to direct the Secretary of the Interior to carry out a feasibility study on a selective water withdrawal system at Glen Canyon Dam, and for other purposes.",
    "type": "S",
    "updateDate": "2026-04-15T01:32:18Z",
    "updateDateIncludingText": "2026-04-15T01:32:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Water and Power. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T21:49:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-03-17T14:00:32Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Water and Power Subcommittee",
          "systemCode": "sseg07"
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3743is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3743\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of the Interior to carry out a feasibility study on a selective water withdrawal system at Glen Canyon Dam, and for other purposes.\n#### 1. Glen Canyon Dam selective water withdrawal system feasibility study\n##### (a) In general\nThe Secretary of the Interior (acting through the Commissioner of Reclamation) (referred to in this section as the Secretary ), in consultation with the Secretary of Energy and Colorado River Storage Project power contractors, shall carry out a feasibility study (including all hydrological modeling) on a selective water withdrawal system at Glen Canyon Dam to optimize hydropower generation when releasing cold water from Glen Canyon Dam, while also preventing entrainment of invasive species, pursuant to the 2016 Long-Term Experimental and Management Plan Record of Decision and the 2024 Long-Term Experimental and Management Plan Supplemental Environmental Impact Statement and Record of Decision.\n##### (b) Feasibility determination\nIf the Secretary determines that a selective water withdrawal system alternative studied under subsection (a) is feasible under the reclamation laws, the Secretary may, if the Colorado River Storage Project power contractors concur with the alternative chosen, begin compliance with, and construction of, the chosen alternative.\n##### (c) Feasibility study deadline\nThe Secretary shall complete the feasibility study required under subsection (a) not later than 18 months after the date of enactment of this Act.\n##### (d) Funding\n**(1) In general**\nThe costs of the feasibility study under subsection (a) shall be paid for by the Secretary using appropriated funds.\n**(2) Treatment of funds**\nAny Federal funds made available to carry out this section shall be nonreimbursable and nonreturnable to the United States.\n**(3) Identification of funds**\nNot later than 90 days after the date of enactment of this Act, the Secretary, in consultation with the Secretary of Energy and Colorado River Storage Project power contractors, shall identify sources of available funds to carry out this section.\n##### (e) Effect\nNothing in this section affects the post-2026 Colorado River reservoir operations guidelines and strategies for Lake Powell and Lake Mead in effect before, on, or after the date of enactment of this Act.",
      "versionDate": "2026-01-29",
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
        "actionDate": "2026-03-26",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "8113",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To direct the Secretary of the Interior to carry out a feasibility study on a selective water withdrawal system at Glen Canyon Dam, and for other purposes.",
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
            "name": "Alternative and renewable resources",
            "updateDate": "2026-04-02T18:25:07Z"
          },
          {
            "name": "Arizona",
            "updateDate": "2026-04-02T18:24:48Z"
          },
          {
            "name": "Dams and canals",
            "updateDate": "2026-04-02T18:24:54Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-04-02T18:25:13Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-04-02T18:24:59Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-04-02T18:25:29Z"
          },
          {
            "name": "Water resources funding",
            "updateDate": "2026-04-02T18:25:36Z"
          },
          {
            "name": "Water storage",
            "updateDate": "2026-04-02T18:25:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Water Resources Development",
        "updateDate": "2026-02-23T21:53:07Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3743is.xml"
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
      "title": "A bill to direct the Secretary of the Interior to carry out a feasibility study on a selective water withdrawal system at Glen Canyon Dam, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:34Z"
    },
    {
      "title": "A bill to direct the Secretary of the Interior to carry out a feasibility study on a selective water withdrawal system at Glen Canyon Dam, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-30T11:56:18Z"
    }
  ]
}
```
