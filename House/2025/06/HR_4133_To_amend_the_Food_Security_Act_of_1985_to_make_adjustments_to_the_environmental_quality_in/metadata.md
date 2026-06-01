# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4133
- Title: EQIP Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4133
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-01-22T09:06:22Z
- Update date including text: 2026-01-22T09:06:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4133",
    "number": "4133",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001081",
        "district": "5",
        "firstName": "Jahana",
        "fullName": "Rep. Hayes, Jahana [D-CT-5]",
        "lastName": "Hayes",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "EQIP Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-22T09:06:22Z",
    "updateDateIncludingText": "2026-01-22T09:06:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-25",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
          "date": "2025-06-25T14:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "AL"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4133ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4133\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mrs. Hayes (for herself, Mr. Moulton , Mr. Huffman , and Mr. Figures ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to make adjustments to the environmental quality incentives program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the EQIP Improvement Act of 2025 .\n#### 2. Environmental Quality Incentives Program reforms\n##### (a) In general\nSection 1240B of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132 ) is amended\u2014\n**(1)**\nin subsection (d), by striking paragraph (2) and inserting the following:\n(2) Limitation on payments A payment to a producer for performing a practice may not exceed, as determined by the Secretary\u2014 (A) except as provided in subparagraphs (B) through (D), 75 percent of the costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training; (B) 40 percent of the costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training for\u2014 (i) an access road; (ii) an animal mortality facility; (iii) an aquaculture pond; (iv) clearing and snagging; (v) a dam; (vi) a dam using a diversion; (vii) a dike; (viii) a diversion; (ix) a fish raceway or tank; (x) an irrigation pipeline; (xi) an irrigation reservoir; (xii) land clearing; (xiii) land smoothing; (xiv) a livestock pipeline; (xv) obstruction removal; (xvi) a pond; (xvii) a pumping plant; (xviii) spoil spreading; (xix) a surface drain using a field ditch; (xx) a main or lateral surface drain; (xxi) a vertical drain; (xxii) a waste facility closure; (xxiii) a waste storage facility; (xxiv) waste transfer; or (xxv) a waste treatment lagoon; (C) 100 percent of income foregone by the producer; or (D) in the case of a practice that includes 1 or more elements described in subparagraphs (A) through (C)\u2014 (i) 75 percent of the costs incurred with respect to any elements described in subparagraph (A); (ii) 40 percent of the costs incurred with respect to any elements described in subparagraph (B); and (iii) 100 percent of the income forgone with respect to any elements described in subparagraph (C). ; and\n**(2)**\nin subsection (f), by striking the subsection designation and heading and all that follows through For each in paragraph (2)(B) and inserting the following:\n(f) Allocation of funding for wildlife habitat For each .\n##### (b) Limitation on payments\nSection 1240G of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20137 ) is amended by striking $450,000 and inserting $150,000 .\n##### (c) Report to Congress\nSection 1240B of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132 ) is amended by adding at the end the following:\n(k) Annual report to Congress Not less frequently than once each year, the Secretary shall submit to Congress a report describing\u2014 (1) the amount obligated under the program with respect to each category of practice, with information categorized by fiscal year and State; and (2) the amount obligated under the program in each State, with information categorized by fiscal year and the size of the operation of each producer. .",
      "versionDate": "2025-06-25",
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
        "actionDate": "2025-12-16",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3498",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "EQIP Improvement Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-11T17:44:22Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4133ih.xml"
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
      "title": "EQIP Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-11T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EQIP Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-11T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to make adjustments to the environmental quality incentives program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-11T06:48:21Z"
    }
  ]
}
```
