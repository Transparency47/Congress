# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6633
- Title: High-Capacity Grid Act
- Congress: 119
- Bill type: HR
- Bill number: 6633
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-21T09:05:24Z
- Update date including text: 2026-01-21T09:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6633",
    "number": "6633",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "F000482",
        "district": "",
        "firstName": "Julie",
        "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
        "lastName": "Fedorchak",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "High-Capacity Grid Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:24Z",
    "updateDateIncludingText": "2026-01-21T09:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:02:30Z",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "AZ"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6633ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6633\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mrs. Fedorchak introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish a best-available transmission conductor standard for certain transmission projects under the Federal Power Act and to provide for presumptions regarding cost recovery for such conductors.\n#### 1. Short title\nThis Act may be cited as the High-Capacity Grid Act .\n#### 2. Best-available transmission conductor standard\nSection 205 of the Federal Power Act ( 16 U.S.C. 824d ) is amended by adding at the end the following:\n(h) Best-Available transmission conductor standard (1) Definitions In this subsection: (A) Best-available transmission conductor The term best-available transmission conductor means a transmission conductor that, as determined by the Commission by rule under paragraph (5)\u2014 (i) provides the greatest feasible and commercially available energy-carrying capacity at a given voltage level; (ii) provides the highest feasible and commercially available electrical efficiency at that voltage level; and (iii) mitigates thermal sag at the maximum rated transmission-carrying capacity of the facility. (B) Covered project The term covered project means\u2014 (i) the construction of a new transmission facility subject to the jurisdiction of the Commission under section 201(b); and (ii) any modification, upgrade, replacement, or reconductoring of an existing transmission line subject to such jurisdiction. (2) Presumption of prudence for best-available transmission conductors In any filing seeking to recover the cost of a transmission conductor for a covered project, and in any proceeding to determine whether such cost may be recovered through rates, the Commission shall presume that the use of a best-available transmission conductor is a prudent practice and that the associated costs are just and reasonable. (3) Presumption against recovery of costs for non-best-available conductors In any filing seeking to recover the cost of a transmission conductor for a covered project, and in any proceeding to determine whether such cost may be recovered through rates, the Commission shall presume that the use of a transmission conductor that is not a best-available transmission conductor is not prudent and that the associated costs are not just and reasonable. (4) Applicability The requirements of this subsection apply only to public utilities and only with respect to covered projects that are subject to the jurisdiction of the Commission under section 201(b). (5) Rulemaking Not later than 180 days after the date of enactment of this subsection, the Commission shall promulgate regulations to implement this subsection. In promulgating such regulations, the Commission shall\u2014 (A) establish a methodology for determining whether a transmission conductor is a best-available transmission conductor for purposes of this subsection; (B) ensure that such methodology is consistent with the criteria set forth in paragraph (1)(A); and (C) provide for periodic review and updating of the methodology to reflect improvements in technology, materials, and system performance. .",
      "versionDate": "2025-12-11",
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
        "name": "Energy",
        "updateDate": "2026-01-07T18:54:41Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6633ih.xml"
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
      "title": "High-Capacity Grid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "High-Capacity Grid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a best-available transmission conductor standard for certain transmission projects under the Federal Power Act and to provide for presumptions regarding cost recovery for such conductors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T05:48:18Z"
    }
  ]
}
```
