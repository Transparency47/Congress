# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8099?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8099
- Title: Plug Offshore Wells Act
- Congress: 119
- Bill type: HR
- Bill number: 8099
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-30T19:46:45Z
- Update date including text: 2026-04-30T19:46:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Natural Resources.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8099",
    "number": "8099",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "D000635",
        "district": "3",
        "firstName": "Maxine",
        "fullName": "Rep. Dexter, Maxine [D-OR-3]",
        "lastName": "Dexter",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Plug Offshore Wells Act",
    "type": "HR",
    "updateDate": "2026-04-30T19:46:45Z",
    "updateDateIncludingText": "2026-04-30T19:46:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8099ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8099\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Ms. Dexter (for herself, Ms. Bonamici , Mr. Huffman , Mr. Min , Mr. Kennedy of New York , Ms. Brownley , Ms. Norton , Mr. Mullin , and Mr. Levin ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo require the Secretary of the Interior to annually submit to Congress, and make publicly available on a website, a report on decommissioning offshore oil and gas wells, platforms, and pipelines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Plug Offshore Wells Act .\n#### 2. Annual report on decommissioning offshore oil and gas wells, platforms, and pipelines\n##### (a) Definitions\nIn this Act:\n**(1) Decommissioning**\nThe term decommissioning has the meaning given the term in section 250.1700 of title 30, Code of Federal Regulations (or a successor regulation).\n**(2) Secretary**\nThe term Secretary means the Secretary of the Interior.\n##### (b) Annual report\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to Congress and make publicly available on the website of the Department of the Interior a report that describes, with respect to the preceding calendar year\u2014\n**(1)**\nthe number of applications for decommissioning an offshore oil and gas well, platform, or pipeline that were required to be submitted pursuant to subpart Q of part 250 of title 30, Code of Federal Regulations (or successor regulations);\n**(2)**\nthe number of applications described in paragraph (1) that were received by the Secretary;\n**(3)**\nthe number of offshore oil and gas wells, platforms, and pipelines for which decommissioning did not occur by the date required pursuant to subpart Q of part 250 of title 30, Code of Federal Regulations (or successor regulations);\n**(4)**\nthe number of offshore oil and gas wells and platforms approved for decommissioning in place pursuant to section 250.1750 of title 30, Code of Federal Regulations (or a successor regulation);\n**(5)**\nthe length of any offshore oil and gas pipelines that\u2014\n**(A)**\nwere decommissioned in place pursuant to section 250.1750 of title 30, Code of Federal Regulations (or a successor regulation); and\n**(B)**\nwere removed pursuant to\u2014\n**(i)**\nsection 250.1752 of title 30, Code of Federal Regulations (or a successor regulation); and\n**(ii)**\nsection 250.1754 of title 30, Code of Federal Regulations (or a successor regulation); and\n**(6)**\nthe status of enforcement actions, including notices of incidents of noncompliance, orders, citations, civil penalties, and disqualifications from future offshore operations, by the Bureau of Safety and Environmental Enforcement with respect to decommissioning offshore oil and gas wells, platforms, and pipelines.",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Energy and Natural Resources."
      },
      "number": "4239",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Plug Offshore Wells Act",
      "type": "S"
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
        "updateDate": "2026-04-30T19:46:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8099ih.xml"
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
      "title": "Plug Offshore Wells Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Plug Offshore Wells Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Interior to annually submit to Congress, and make publicly available on a website, a report on decommissioning offshore oil and gas wells, platforms, and pipelines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:33:33Z"
    }
  ]
}
```
