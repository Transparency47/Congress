# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6345?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6345
- Title: Point-Access Housing Guidelines Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6345
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-03-19T08:07:11Z
- Update date including text: 2026-03-19T08:07:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6345",
    "number": "6345",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Point-Access Housing Guidelines Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-19T08:07:11Z",
    "updateDateIncludingText": "2026-03-19T08:07:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "NY"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-12-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6345ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6345\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Torres of New York (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development to establish Federal guidelines for point-access block buildings, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Point-Access Housing Guidelines Act of 2025 .\n#### 2. Federal guidelines for point-access block buildings\n##### (a) In general\nNot later than 18 months after the date of enactment of this section, the Secretary of Housing and Urban Development shall issue guidelines to provide States, territories, Tribes, and localities with model code language, best practices, and technical guidance that could be used to facilitate the permitting of point-access block residential buildings.\n##### (b) Contents\nWhen developing the guidelines under subsection (a), the Secretary shall consider\u2014\n**(1)**\nfire safety considerations, including sprinkler coverage, smoke detection, ventilation, and building egress performance;\n**(2)**\nconstruction costs and impacts on housing affordability, including the potential for increasing housing supply in high-cost jurisdictions;\n**(3)**\nflexibility for diverse consumer needs, including family sizes, unit configurations, and accessibility;\n**(4)**\nexamples from jurisdictions that have adopted or considered single-stair codes, including States, cities, and relevant international standards;\n**(5)**\nresearch and model language produced by organizations focused on point-access block building design and building-code reform;\n**(6)**\nconsultation with experts, including developers, architects, fire marshals, researchers, economists, housing authorities, and officials in States that have enacted or piloted single-stair reforms; and\n**(7)**\nalternative methods of compliance, incorporating options that utilize additional passive or active safety features.\n##### (c) Coordination with the International Code Council\nThe Secretary shall coordinate with the International Code Council to encourage the incorporation of provisions about point-access block buildings into the International Building Code.\n##### (d) Grants\nThe Secretary may award competitive grants to eligible entities to implement pilot projects that evaluate, demonstrate, or validate the safety, feasibility, or cost-effectiveness of point-access block residential buildings.\n##### (e) Rule of construction\nNothing in this section may be construed to preempt a State or local building code.\n##### (f) Definitions\nIn this section:\n**(1) Point-access block building**\nThe term point-access block building means a Group R\u20132 occupancy residential structure, as such term is defined by the International Building Code, in which a single internal stairway provides access and egress for all dwelling units in a building that is not greater than five stories in height.\n**(2) Eligible entities**\nThe term eligible entity means a State, unit of local government, Tribal government, public housing agency, nonprofit housing or community development organization, private developer or construction firm, qualified design or engineering firm, academic or research institution, or any partnership or consortium composed of 2 or more such entities.",
      "versionDate": "2025-12-01",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-12-12T16:14:38Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6345ih.xml"
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
      "title": "Point-Access Housing Guidelines Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Point-Access Housing Guidelines Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to establish Federal guidelines for point-access block buildings, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T07:18:27Z"
    }
  ]
}
```
