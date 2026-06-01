# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5241
- Title: RTCP Revitalization Act
- Congress: 119
- Bill type: HR
- Bill number: 5241
- Origin chamber: House
- Introduced date: 2025-09-09
- Update date: 2026-05-16T08:08:02Z
- Update date including text: 2026-05-16T08:08:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-09: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-09-09: Introduced in House

## Actions

- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Introduced in House
- 2025-09-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-09",
    "latestAction": {
      "actionDate": "2025-09-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5241",
    "number": "5241",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "RTCP Revitalization Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:02Z",
    "updateDateIncludingText": "2026-05-16T08:08:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-09",
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
      "actionDate": "2025-09-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-09",
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
          "date": "2025-09-09T14:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T19:55:01Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AK"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MP"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AS"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "GU"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "PR"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5241ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5241\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 9, 2025 Ms. Tokuda (for herself, Mr. Begich , Ms. King-Hinds , Mrs. Radewagen , Mr. Moylan , Mr. Hern\u00e1ndez , and Ms. Plaskett ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food, Conservation, and Energy Act of 2008 to provide mandatory funding from the Commodity Credit Corporation for reimbursement payments to geographically disadvantaged farmers and ranchers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the RTCP Revitalization Act .\n#### 2. Commodity Credit Corporation funding for geographically disadvantaged farmers and ranchers\nSection 1621 of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 8792 ) is amended\u2014\n**(1)**\nin subsection (b), by striking Subject to the availability of funds under subsection (d), the Secretary and inserting The Secretary ;\n**(2)**\nin subsection (c)(3), by striking subparagraph (B) and inserting the following:\n(B) Payment limitations The Secretary may not impose a limitation on the amount of payments received by a geographically disadvantaged farmer or rancher under this section for any fiscal year in which the amount made available for payments under this section is equal to or greater than the amount that may be provided in accordance with this section with respect to applications received by the Secretary for that fiscal year. ; and\n**(3)**\nin subsection (d), by striking the subsection designation and heading and all that follows through There are and inserting the following:\n(d) Funding (1) Mandatory funding Of the funds of the Commodity Credit Corporation, the Secretary shall use to carry out this section\u2014 (A) $10,000,000 for fiscal year 2026; (B) $11,000,000 for fiscal year 2027; (C) $12,000,000 for fiscal year 2028; (D) $13,000,000 for fiscal year 2029; (E) $14,000,000 for fiscal year 2030; and (F) $15,000,000 for fiscal year 2031 and each fiscal year thereafter. (2) Authorization of appropriations There are .",
      "versionDate": "2025-09-09",
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
        "actionDate": "2025-05-14",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1758",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "RTCP Revitalization Act",
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
        "updateDate": "2025-09-17T19:33:10Z"
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
      "date": "2025-09-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5241ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RTCP Revitalization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-17T11:23:14Z"
    },
    {
      "title": "RTCP Revitalization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food, Conservation, and Energy Act of 2008 to provide mandatory funding from the Commodity Credit Corporation for reimbursement payments to geographically disadvantaged farmers and ranchers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-17T11:18:15Z"
    }
  ]
}
```
