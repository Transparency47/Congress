# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1843?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1843
- Title: To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications.
- Congress: 119
- Bill type: HR
- Bill number: 1843
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-05T17:34:06Z
- Update date including text: 2026-02-05T17:34:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1843",
    "number": "1843",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications.",
    "type": "HR",
    "updateDate": "2026-02-05T17:34:06Z",
    "updateDateIncludingText": "2026-02-05T17:34:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:00:50Z",
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
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1843ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1843\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Dunn of Florida (for himself and Mr. Mullin ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications.\n#### 1. Increasing transparency in generic drug applications\n##### (a) In general\nSection 505(j)(3) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(3) ) is amended by adding at the end the following:\n(H) (i) Upon request (in controlled correspondence or an analogous process) by a person that has submitted or intends to submit an abbreviated application under this subsection for a drug that is required by regulation to contain one or more of the same inactive ingredients in the same concentrations as the listed drug referred to, or for which the Secretary determines there is a scientific justification for an approach that is in vitro in whole or in part to be used to demonstrate bioequivalence for a drug if such a drug contains one or more of the same inactive ingredients in the same concentrations as the listed drug, the Secretary shall inform the person whether such drug is qualitatively and quantitatively the same as the listed drug. The Secretary may also provide such information to such a person on the Secretary\u2019s own initiative during the review of an abbreviated application under this subsection for such drug. (ii) Notwithstanding section 301(j), if the Secretary determines that such drug is not qualitatively or quantitatively the same as the listed drug, the Secretary shall identify and disclose to the person\u2014 (I) the ingredient or ingredients that cause such drug not to be qualitatively or quantitatively the same as the listed drug; and (II) for any ingredient for which there is an identified quantitative deviation, the amount of such deviation. (iii) If the Secretary determines that such drug is qualitatively and quantitatively the same as the listed drug, the Secretary shall not change or rescind such determination after the submission of an abbreviated application for such drug under this subsection unless\u2014 (I) the formulation of the listed drug has been changed and the Secretary has determined that the prior listed drug formulation was withdrawn for reasons of safety or effectiveness; or (II) the Secretary makes a written determination that the prior determination must be changed because an error has been identified. (iv) If the Secretary makes a written determination described in clause (iii)(II), the Secretary shall provide notice and a copy of the written determination to the person making the request under clause (i). (v) The disclosures required by this subparagraph are disclosures authorized by law, including for purposes of section 1905 of title 18, United States Code. .\n##### (b) Guidance\n**(1) In general**\nNot later than one year after the date of enactment of this Act, the Secretary of Health and Human Services shall issue draft guidance, or update guidance, describing how the Secretary will determine whether a drug is qualitatively and quantitatively the same as the listed drug (as such terms are used in section 505(j)(3)(H) of the Federal Food, Drug, and Cosmetic Act, as added by subsection (a)), including with respect to assessing pH adjusters.\n**(2) Process**\nIn issuing guidance under this subsection, the Secretary of Health and Human Services shall\u2014\n**(A)**\npublish draft guidance;\n**(B)**\nprovide a period of at least 60 days for comment on the draft guidance; and\n**(C)**\nafter considering any comments received and not later than one year after the close of the comment period on the draft guidance, publish final guidance.\n##### (c) Applicability\nSection 505(j)(3)(H) of the Federal Food, Drug, and Cosmetic Act, as added by subsection (a), applies beginning on the date of enactment of this Act, irrespective of the date on which the guidance required by subsection (b) is finalized.",
      "versionDate": "2025-03-05",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1302",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Increasing Transparency in Generic Drug Applications Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
        "name": "Health",
        "updateDate": "2025-03-21T17:32:00Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1843",
          "measure-number": "1843",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1843v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Food and Drug Administration (FDA) to inform generic drug applicants, upon request or during review, whether the drug is qualitatively and quantitatively the same as the listed brand-name drug (and if not, the reasons why). The FDA must also update or publish guidance on how it makes such determinations.</p>"
        },
        "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1843.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Food and Drug Administration (FDA) to inform generic drug applicants, upon request or during review, whether the drug is qualitatively and quantitatively the same as the listed brand-name drug (and if not, the reasons why). The FDA must also update or publish guidance on how it makes such determinations.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1843"
    },
    "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications."
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Food and Drug Administration (FDA) to inform generic drug applicants, upon request or during review, whether the drug is qualitatively and quantitatively the same as the listed brand-name drug (and if not, the reasons why). The FDA must also update or publish guidance on how it makes such determinations.</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1843"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1843ih.xml"
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
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:34Z"
    },
    {
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T09:06:42Z"
    }
  ]
}
```
