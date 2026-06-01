# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1059?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1059
- Title: Jobs and Opportunities for Medicaid Act
- Congress: 119
- Bill type: HR
- Bill number: 1059
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-12-05T21:56:41Z
- Update date including text: 2025-12-05T21:56:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1059",
    "number": "1059",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Jobs and Opportunities for Medicaid Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:56:41Z",
    "updateDateIncludingText": "2025-12-05T21:56:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:05:30Z",
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
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1059ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1059\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Crenshaw introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to implement a minimum work requirement for able-bodied adults enrolled in State Medicaid programs.\n#### 1. Short title\nThis Act may be cited as the Jobs and Opportunities for Medicaid Act .\n#### 2. Work requirements for able-bodied adults\nSection 1902 of the Social Security Act ( 42 U.S.C. 1396a ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking and at the end of paragraph (86);\n**(B)**\nby striking the period at the end of paragraph (87) and inserting ; and ; and\n**(C)**\nby inserting after paragraph (87) the following new paragraph:\n(88) beginning January 1, 2026, not provide medical assistance with respect to a month to an able-bodied adult (as defined in subsection (uu)(2)) that has not met the work requirement described in subsection (uu)(1) for such month. ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Work requirement for able-Bodied adults (1) Work requirement described For purposes of subsection (a)(88), the work requirement described in this subsection with respect to an able-bodied adult and a month is that such adult satisfies at least one of the following with respect to such month: (A) The adult works 20 hours or more per week, based on a monthly average. (B) The adult volunteers for 20 hours or more per week, based on a monthly average. (2) Able-bodied adult defined In this subsection, the term able-bodied adult means any individual who is not\u2014 (A) under 18 years of age or over 65 years of age; (B) medically certified as physically or mentally unfit for employment; (C) pregnant; (D) the primary parent or caretaker of a dependent child under 6 years of age; (E) the primary parent or caretaker of a dependent child with a serious medical condition or disability, as determined by the State agency established or designated to administer or supervise the administration of the State plan; (F) receiving unemployment compensation under State or Federal law and, as applicable, complying with work requirements under such State or Federal law; or (G) participating in a drug addiction or alcoholic treatment and rehabilitation program (as defined in section 3(h) of the Food and Nutrition Act of 2008). .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "447",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Jobs and Opportunities for Medicaid Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Medicaid",
            "updateDate": "2025-04-14T14:29:58Z"
          },
          {
            "name": "Unemployment",
            "updateDate": "2025-04-14T14:29:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-10T15:08:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1059",
          "measure-number": "1059",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1059v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Jobs and Opportunities for Medicaid Act</b></p> <p>This bill establishes work requirements under Medicaid for able-bodied adults. </p> <p>Specifically, the bill requires individuals who are between the ages of 18 and 65 and who are not otherwise unable to work due to a medical condition, family situation, or other listed reason to work or volunteer at least 20 hours per week, based on a monthly average, in order to qualify for Medicaid.</p>"
        },
        "title": "Jobs and Opportunities for Medicaid Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1059.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Jobs and Opportunities for Medicaid Act</b></p> <p>This bill establishes work requirements under Medicaid for able-bodied adults. </p> <p>Specifically, the bill requires individuals who are between the ages of 18 and 65 and who are not otherwise unable to work due to a medical condition, family situation, or other listed reason to work or volunteer at least 20 hours per week, based on a monthly average, in order to qualify for Medicaid.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr1059"
    },
    "title": "Jobs and Opportunities for Medicaid Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Jobs and Opportunities for Medicaid Act</b></p> <p>This bill establishes work requirements under Medicaid for able-bodied adults. </p> <p>Specifically, the bill requires individuals who are between the ages of 18 and 65 and who are not otherwise unable to work due to a medical condition, family situation, or other listed reason to work or volunteer at least 20 hours per week, based on a monthly average, in order to qualify for Medicaid.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr1059"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1059ih.xml"
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
      "title": "Jobs and Opportunities for Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Jobs and Opportunities for Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to implement a minimum work requirement for able-bodied adults enrolled in State Medicaid programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:34Z"
    }
  ]
}
```
