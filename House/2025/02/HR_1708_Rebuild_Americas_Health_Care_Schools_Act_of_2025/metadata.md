# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1708?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1708
- Title: Rebuild America’s Health Care Schools Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1708
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-03-27T08:06:48Z
- Update date including text: 2026-03-27T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1708",
    "number": "1708",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Rebuild America\u2019s Health Care Schools Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-27T08:06:48Z",
    "updateDateIncludingText": "2026-03-27T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NC"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "VA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NE"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "DC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
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
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "DE"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "PA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1708ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1708\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. LaHood (for himself, Ms. Craig , and Mrs. Fischbach ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to adjust allowable direct and indirect costs for nursing and allied health education programs.\n#### 1. Short title\nThis Act may be cited as the Rebuild America\u2019s Health Care Schools Act of 2025 .\n#### 2. Adjusting allowable direct and indirect costs for nursing and allied health education programs\n##### (a) In general\nSection 1861(v)(1) of the Social Security Act ( 42 U.S.C. 1395x(v)(1) ) is amended by adding at the end the following new subparagraph:\n(X) (i) In determining such reasonable costs for nursing and allied health education furnished by a hospital, beginning with respect to cost reporting periods beginning on or after the date of the enactment of the Rebuild America\u2019s Health Care Schools Act of 2025 , the Secretary shall include as reasonable costs all direct and indirect costs incurred by a hospital participating in a nursing and allied health education program licensed by State law or accredited by a national or regional professional organization, including costs that\u2014 (I) were directly incurred by the hospital; (II) were allocated to the hospital by a related entity holding the applicable State license or accreditation by a national or regional professional organization; or (III) were associated with the training of a program participant at the hospital or at a related entity. (ii) For purposes of clause (i), the term related entity means, with respect to a hospital, any entity that is related by common ownership or control to\u2014 (I) the hospital itself; or (II) an entity\u2014 (aa) in which the hospital (or another entity that is a related entity with respect to the hospital) is the sole corporate member; (bb) that is the sole corporate member of the hospital; (cc) that is part of the same legal entity as the hospital; or (dd) that shares a board with the hospital. .\n##### (b) Allowing health systems and hospital-Based schools To provide clinical training and support\nNot later than 120 days after the date of the enactment of this section, the Secretary of Health and Human Services shall issue such rules as are necessary to carry out the amendments made by subsection (a).\n##### (c) Prohibiting recoupment of certain costs under Medicare\n**(1) In general**\nBeginning on the date of the enactment of this section, the Secretary of Health and Human Services may not recoup or reduce payments made to a hospital under part A of title XVIII of the Social Security Act ( 42 U.S.C. 1395c et seq. ) for costs related to an approved nursing or allied health education program that are included on the Medicare cost report for such hospital if such costs would be allowable after the amendments made by subsection (a) take effect.\n**(2) Refund of amounts recouped**\nIf, during the 6-year period ending on the date of the enactment of this section, the Secretary recouped or reduced payments made to a hospital under such part A for costs described in paragraph (1), the Secretary shall refund to the hospital the amount so recouped or reduced.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-03-14",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1087",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rebuild America\u2019s Health Care Schools Act of 2025",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-09-02T18:52:58Z"
          },
          {
            "name": "Department of Health and Human Services",
            "updateDate": "2025-09-02T18:53:02Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-09-02T18:52:43Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-09-02T18:52:16Z"
          },
          {
            "name": "Health personnel",
            "updateDate": "2025-09-02T18:52:20Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-09-02T18:53:06Z"
          },
          {
            "name": "Medical education",
            "updateDate": "2025-09-02T18:52:06Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-09-02T18:52:11Z"
          },
          {
            "name": "Nursing",
            "updateDate": "2025-09-02T18:52:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T14:52:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1708",
          "measure-number": "1708",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1708v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rebuild America\u2019s Health Care Schools Act of 2025</strong></p><p>This bill allows hospitals to receive reimbursement under Medicare for certain costs associated with training nursing and allied health students in settings other than the hospital itself.\u00a0</p><p>Currently, hospitals may receive reimbursement under Medicare for the reasonable costs associated with training nursing and allied health students if certain conditions are met; the criteria vary depending on whether the students are enrolled in an educational program that is operated by the hospital or another entity. If the students are part of a program that is operated by another entity, the training must occur at the hospital itself or in areas immediately surrounding the hospital in order to qualify for reimbursement (among other requirements). The bill allows hospitals to receive reimbursement for these costs if the training is conducted at an entity that is related to the hospital (i.e., common ownership or control).</p><p>The bill requires the Centers for Medicare & Medicaid Services (CMS) to update regulations to reflect these changes. Additionally, the CMS may not recoup or reduce payments to hospitals with respect to costs that are allowed under the bill and must refund any such recoupments or reductions that occurred during the six-year period prior to the bill's enactment.</p>"
        },
        "title": "Rebuild America\u2019s Health Care Schools Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1708.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rebuild America\u2019s Health Care Schools Act of 2025</strong></p><p>This bill allows hospitals to receive reimbursement under Medicare for certain costs associated with training nursing and allied health students in settings other than the hospital itself.\u00a0</p><p>Currently, hospitals may receive reimbursement under Medicare for the reasonable costs associated with training nursing and allied health students if certain conditions are met; the criteria vary depending on whether the students are enrolled in an educational program that is operated by the hospital or another entity. If the students are part of a program that is operated by another entity, the training must occur at the hospital itself or in areas immediately surrounding the hospital in order to qualify for reimbursement (among other requirements). The bill allows hospitals to receive reimbursement for these costs if the training is conducted at an entity that is related to the hospital (i.e., common ownership or control).</p><p>The bill requires the Centers for Medicare & Medicaid Services (CMS) to update regulations to reflect these changes. Additionally, the CMS may not recoup or reduce payments to hospitals with respect to costs that are allowed under the bill and must refund any such recoupments or reductions that occurred during the six-year period prior to the bill's enactment.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hr1708"
    },
    "title": "Rebuild America\u2019s Health Care Schools Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rebuild America\u2019s Health Care Schools Act of 2025</strong></p><p>This bill allows hospitals to receive reimbursement under Medicare for certain costs associated with training nursing and allied health students in settings other than the hospital itself.\u00a0</p><p>Currently, hospitals may receive reimbursement under Medicare for the reasonable costs associated with training nursing and allied health students if certain conditions are met; the criteria vary depending on whether the students are enrolled in an educational program that is operated by the hospital or another entity. If the students are part of a program that is operated by another entity, the training must occur at the hospital itself or in areas immediately surrounding the hospital in order to qualify for reimbursement (among other requirements). The bill allows hospitals to receive reimbursement for these costs if the training is conducted at an entity that is related to the hospital (i.e., common ownership or control).</p><p>The bill requires the Centers for Medicare & Medicaid Services (CMS) to update regulations to reflect these changes. Additionally, the CMS may not recoup or reduce payments to hospitals with respect to costs that are allowed under the bill and must refund any such recoupments or reductions that occurred during the six-year period prior to the bill's enactment.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hr1708"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1708ih.xml"
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
      "title": "Rebuild America\u2019s Health Care Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rebuild America\u2019s Health Care Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to adjust allowable direct and indirect costs for nursing and allied health education programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:44Z"
    }
  ]
}
```
