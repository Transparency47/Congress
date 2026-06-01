# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7282?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7282
- Title: FRAMER Act
- Congress: 119
- Bill type: HR
- Bill number: 7282
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-02-24T09:06:02Z
- Update date including text: 2026-02-24T09:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7282",
    "number": "7282",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001137",
        "district": "5",
        "firstName": "Jeff",
        "fullName": "Rep. Crank, Jeff [R-CO-5]",
        "lastName": "Crank",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "FRAMER Act",
    "type": "HR",
    "updateDate": "2026-02-24T09:06:02Z",
    "updateDateIncludingText": "2026-02-24T09:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:33:35Z",
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
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "CO"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7282ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7282\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Crank introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo incentivize States not to enact costly, burdensome, and unreasonable energy code housing policies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freeing Residential Affordable Markets from Excess Regulation Act or the FRAMER Act .\n#### 2. Energy Codes in Opportunity Zones\n##### (a) In general\nSection 104 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5304 ) is amended by adding at the end the following:\n(n) Energy Codes in Opportunity Zones (1) In general To be eligible to receive amounts under this title on or after the date that is 90 days after the date of the enactment of this subsection, a State shall provide to each person who built a covered dwelling unit in an opportunity zone that is located in the jurisdiction of such entity, not later than 30 days after such dwelling unit has been inspected and certified for occupancy, a payment in the amount equal to the difference, determined by the Secretary of Housing and Urban Development, between\u2014 (A) the cost of implementing the energy housing code of the State with respect to such covered dwelling unit, including costs associated with labor, supplies, wages of employees, inspection costs, or any other cost realized by the person who built a covered dwelling unit; and (B) the cost of implementing the Department of Housing and Urban Development\u2019s Minimum Energy Standard with respect to such covered dwelling unit, regardless of whether such covered dwelling is subject to such standard. (2) Exception Paragraph (1) shall not apply if the energy housing code of the State has a lower cost than the Department of Housing and Urban Development\u2019s Minimum Energy Standard. (3) Disclosure requirement A person who built a covered dwelling unit in an opportunity zone and who has received or may in the future receive a reimbursement for building costs incurred shall provide to the person who first buys the covered dwelling unit, using a procedure and form established by the Secretary, a disclosure document that, based on information reasonably available at the time such disclosure is made,\u2014 (A) identifies the difference between the cost of implementing the energy housing code of the State with respect to such covered dwelling unit and the cost of implementing the Department of Housing and Urban Development\u2019s Minimum Energy Standard with respect to such covered dwelling unit; (B) identifies any amount that such person who built a covered dwelling unit has received or expects to receive from the a State under this section and any portion of such amount that was used by such person to reduce the price of the covered dwelling unit. (4) Definitions In this subsection: (A) Covered dwelling unit The term covered dwelling unit means a residential building such as term is defined in section 6832 of title 42, Code of Federal Regulations. (B) Opportunity zone The term opportunity zone has the meaning given the term in section 1400Z\u20132 of title 26, United States Code. .\n##### (b) Report\nThe Comptroller General of the United States shall, each year until the date described in subsection (c), submit a report to the Congress that, to the degree practicable\u2014\n**(1)**\nlists the States that were required under Section 104(n) of the Housing and Community Development Act of 1974 to provide payments to persons who built dwelling units;\n**(2)**\nthe amount of each such payment, broken out by metropolitan city, urban county, State, unit of general local government, and insular area;\n**(3)**\nthe total amount of all such payments, broken out by metropolitan city, urban county, State, unit of general local government, and insular area; and\n**(4)**\nthe amount of the difference between the State codes and Department of Housing and Urban Development\u2019s Minimum Energy Standard by metropolitan city, urban county, State, unit of general local government, and insular area.\n##### (c) Sunset\nSection 104(n) of the Housing and Community Development Act of 1974, as added by this section, shall be repealed on the date that is 7 years after the date of the enactment of this section.",
      "versionDate": "2026-01-30",
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
        "updateDate": "2026-02-20T17:49:20Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7282ih.xml"
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
      "title": "FRAMER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FRAMER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freeing Residential Affordable Markets from Excess Regulation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To incentivize States not to enact costly, burdensome, and unreasonable energy code housing policies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:30Z"
    }
  ]
}
```
