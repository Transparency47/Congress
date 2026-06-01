# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2221?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2221
- Title: SAWMILL Act
- Congress: 119
- Bill type: S
- Bill number: 2221
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2221",
    "number": "2221",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "SAWMILL Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-09",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-09",
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
            "date": "2025-07-09T18:12:49Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-09T18:12:49Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "MT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-29",
      "state": "ME"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2221is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2221\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Merkley (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo establish requirements under which the Secretary of Agriculture and the Secretary of the Interior shall carry out the Timber Production Expansion Guaranteed Loan Program.\n#### 1. Short title\nThis Act may be cited as the Supporting American Wood and Mill Infrastructure with Loans for Longevity Act or the SAWMILL Act .\n#### 2. Timber Production Expansion Guaranteed Loan Program\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means an individual or entity that owns or operates a sawmill or other wood-processing facility located in a rural area (as defined in section 343(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a) )) of the United States.\n**(2) Eligible Federal land**\nThe term eligible Federal land means any unit of Federal land, including Indian forest land or rangeland, that has been identified by the Secretary, in coordination with the Secretary of the Interior, as high or very high priority for ecological restoration involving vegetation removal under subsection (b).\n**(3) Program**\nThe term Program means the Timber Production Expansion Guaranteed Loan Program of the Department of Agriculture.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (b) Identification of eligible Federal land\nNot later than 1 year after the date of enactment of this Act, and not less frequently than once every 5 years thereafter, the Secretary, in coordination with the Secretary of the Interior, shall\u2014\n**(1)**\nreview Federal land under the jurisdiction of the Secretary or the Secretary of the Interior; and\n**(2)**\nidentify units of Federal land that, as determined by the Secretaries, are high or very high priority for ecological restoration involving vegetation removal.\n##### (c) Loan guarantees\n**(1) In general**\nThe Secretary, in coordination with the Secretary of the Interior, shall provide loan guarantees under the Program to eligible entities seeking to establish, reopen, retrofit, expand, or improve a sawmill or other wood-processing facility located within a 250-mile radius of, a unit of eligible Federal land, if the presence of a sawmill or other wood-processing facility would, or does, substantially decrease the cost of conducting ecological restoration projects involving vegetation removal on the eligible Federal land, as determined by the Secretary, in coordination with the Secretary of the Interior.\n**(2) Conditions**\nA loan guarantee under the Program shall be provided in accordance with such conditions as the Secretary determines to be necessary.\n**(3) Maximum amount**\nThe Secretary may provide a total of not more than $220,000,000 in loan guarantees under the Program.",
      "versionDate": "2025-07-09",
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
        "actionDate": "2025-11-21",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6277",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SAWMILL Act",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-31T22:18:47Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2221is.xml"
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
      "title": "SAWMILL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SAWMILL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting American Wood and Mill Infrastructure with Loans for Longevity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish requirements under which the Secretary of Agriculture and the Secretary of the Interior shall carry out the Timber Production Expansion Guaranteed Loan Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:48:31Z"
    }
  ]
}
```
