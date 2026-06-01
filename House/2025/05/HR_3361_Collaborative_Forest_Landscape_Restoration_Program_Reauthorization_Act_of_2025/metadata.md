# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3361?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3361
- Title: Collaborative Forest Landscape Restoration Program Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3361
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2025-12-05T21:37:11Z
- Update date including text: 2025-12-05T21:37:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-13: Introduced in House

## Actions

- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3361",
    "number": "3361",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Collaborative Forest Landscape Restoration Program Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:37:11Z",
    "updateDateIncludingText": "2025-12-05T21:37:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
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
      "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-13",
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
          "date": "2025-05-13T16:07:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-13T16:07:00Z",
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "MT"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "OR"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3361ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3361\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Neguse (for himself, Mr. Zinke , Ms. Salinas , and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Agriculture , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Omnibus Public Land Management Act of 2009 to reauthorize the Collaborative Forest Landscape Restoration Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Collaborative Forest Landscape Restoration Program Reauthorization Act of 2025 .\n#### 2. Collaborative Forest Landscape Restoration Program reauthorization\nSection 4003 of the Omnibus Public Land Management Act of 2009 ( 16 U.S.C. 7303 ) is amended\u2014\n**(1)**\nin subsection (b)(3)\u2014\n**(A)**\nin subparagraph (D), by striking species; and inserting species or pathogens; ;\n**(B)**\nin subparagraph (G), by striking and at the end;\n**(C)**\nin subparagraph (H), by adding and after the semicolon at the end; and\n**(D)**\nby adding at the end the following:\n(I) address standardized monitoring questions and indicators; ;\n**(2)**\nin subsection (c)(3)(A)\u2014\n**(A)**\nin clause (i), by striking and at the end;\n**(B)**\nin clause (ii), by adding and at the end; and\n**(C)**\nby adding at the end the following:\n(iii) include a Federal Government staffing plan for providing support to collaboratives established pursuant to subsection (b)(2); ;\n**(3)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (E), by striking and at the end;\n**(ii)**\nin subparagraph (F), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following:\n(G) proposals that seek to use innovative implementation mechanisms, including conservation finance agreements, good neighbor agreements entered into under section 8206 of the Agricultural Act of 2014 ( 16 U.S.C. 2113a ), and similar implementation mechanisms; (H) proposals that seek to reduce the risk of uncharacteristic wildfire or increase ecological restoration activities\u2014 (i) within areas across land ownerships, including State, Tribal, and private land; and (ii) within the wildland-urban interface (as defined in section 101 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6511 )); and (I) proposals that seek to enhance watershed health and drinking water sources. ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking 10 and inserting 20 ; and\n**(ii)**\nin subparagraph (B), by striking 2 and inserting 4 ;\n**(4)**\nin subsection (e)(3), by inserting conflict resolution or collaborative governance, before and woody ; and\n**(5)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (4)(B)(ii), by striking $4,000,000 and inserting $8,000,000 ; and\n**(B)**\nin paragraph (6), by striking 2023 and inserting 2034 .",
      "versionDate": "2025-05-13",
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
        "actionDate": "2025-05-07",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1662",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Collaborative Forest Landscape Restoration Program Reauthorization Act of 2025",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-06-11T14:00:00Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3361ih.xml"
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
      "title": "Collaborative Forest Landscape Restoration Program Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Collaborative Forest Landscape Restoration Program Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Public Land Management Act of 2009 to reauthorize the Collaborative Forest Landscape Restoration Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:22Z"
    }
  ]
}
```
