# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4239?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4239
- Title: Plug Offshore Wells Act
- Congress: 119
- Bill type: S
- Bill number: 4239
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-05-01T19:22:59Z
- Update date including text: 2026-05-01T19:22:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4239",
    "number": "4239",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Plug Offshore Wells Act",
    "type": "S",
    "updateDate": "2026-05-01T19:22:59Z",
    "updateDateIncludingText": "2026-05-01T19:22:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T18:53:33Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4239is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4239\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Welch (for himself, Mr. Merkley , Mr. Wyden , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require the Secretary of the Interior to annually submit to Congress, and make publicly available on a website, a report on decommissioning offshore oil and gas wells, platforms, and pipelines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Plug Offshore Wells Act .\n#### 2. Annual report on decommissioning offshore oil and gas wells, platforms, and pipelines\n##### (a) Definitions\nIn this Act:\n**(1) Decommissioning**\nThe term decommissioning has the meaning given the term in section 250.1700 of title 30, Code of Federal Regulations (or a successor regulation).\n**(2) Secretary**\nThe term Secretary means the Secretary of the Interior.\n##### (b) Annual report\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to Congress and make publicly available on the website of the Department of the Interior a report that describes, with respect to the preceding calendar year\u2014\n**(1)**\nthe number of applications for decommissioning an offshore oil and gas well, platform, or pipeline that were required to be submitted pursuant to subpart Q of part 250 of title 30, Code of Federal Regulations (or successor regulations);\n**(2)**\nthe number of applications described in paragraph (1) that were received by the Secretary;\n**(3)**\nthe number of offshore oil and gas wells, platforms, and pipelines for which decommissioning did not occur by the date required pursuant to subpart Q of part 250 of title 30, Code of Federal Regulations (or successor regulations);\n**(4)**\nthe number of offshore oil and gas wells and platforms approved for decommissioning in place pursuant to section 250.1750 of title 30, Code of Federal Regulations (or a successor regulation);\n**(5)**\nthe length of any offshore oil and gas pipelines that\u2014\n**(A)**\nwere decommissioned in place pursuant to section 250.1750 of title 30, Code of Federal Regulations (or a successor regulation); and\n**(B)**\nwere removed pursuant to\u2014\n**(i)**\nsection 250.1752 of title 30, Code of Federal Regulations (or a successor regulation); and\n**(ii)**\nsection 250.1754 of title 30, Code of Federal Regulations (or a successor regulation); and\n**(6)**\nthe status of enforcement actions, including notices of incident of noncompliance, orders, citations, civil penalties, and disqualifications from future offshore operations, by the Bureau of Safety and Environmental Enforcement with respect to decommissioning offshore oil and gas wells, platforms, and pipelines.",
      "versionDate": "2026-03-26",
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
      "number": "8099",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Plug Offshore Wells Act",
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
        "name": "Environmental Protection",
        "updateDate": "2026-05-01T19:22:59Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4239is.xml"
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
      "title": "Plug Offshore Wells Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Plug Offshore Wells Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Interior to annually submit to Congress, and make publicly available on a website, a report on decommissioning offshore oil and gas wells, platforms, and pipelines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:34Z"
    }
  ]
}
```
