# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1302
- Title: Increasing Transparency in Generic Drug Applications Act
- Congress: 119
- Bill type: S
- Bill number: 1302
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-02-05T17:34:10Z
- Update date including text: 2026-02-05T17:34:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1302",
    "number": "1302",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001076",
        "district": "",
        "firstName": "Maggie",
        "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
        "lastName": "Hassan",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Increasing Transparency in Generic Drug Applications Act",
    "type": "S",
    "updateDate": "2026-02-05T17:34:10Z",
    "updateDateIncludingText": "2026-02-05T17:34:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-04T00:15:31Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "KY"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CO"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "UT"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "OK"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1302is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1302\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Ms. Hassan (for herself, Mr. Paul , Mr. Hickenlooper , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for increased transparency in generic drug applications.\n#### 1. Short title\nThis Act may be cited as the Increasing Transparency in Generic Drug Applications Act .\n#### 2. Increasing transparency in generic drug applications\n##### (a) In general\nSection 505(j)(3) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 355(j)(3) ) is amended by adding at the end the following:\n(H) (i) Upon request (in controlled correspondence or an analogous process) by a person that has submitted or intends to submit an abbreviated application under this subsection for a drug that is required by regulation to contain one or more of the same inactive ingredients in the same concentrations as the listed drug referred to, or for which the Secretary determines there is a scientific justification for an approach that is in vitro, in whole or in part, to be used to demonstrate bioequivalence for a drug if such a drug contains one or more of the same inactive ingredients in the same concentrations as the listed drug referred to, the Secretary shall inform the person whether such drug is qualitatively and quantitatively the same as the listed drug. The Secretary may also provide such information to such a person on the Secretary\u2019s own initiative during the review of an abbreviated application under this subsection for such drug. (ii) Notwithstanding section 301(j), if the Secretary determines that such drug is not qualitatively or quantitatively the same as the listed drug, the Secretary shall identify and disclose to the person\u2014 (I) the ingredient or ingredients that cause such drug not to be qualitatively or quantitatively the same as the listed drug; and (II) for any ingredient for which there is an identified quantitative deviation, the amount of such deviation. (iii) If the Secretary determines that such drug is qualitatively and quantitatively the same as the listed drug, the Secretary shall not change or rescind such determination after the submission of an abbreviated application for such drug under this subsection unless\u2014 (I) the formulation of the listed drug has been changed and the Secretary has determined that the prior listed drug formulation was withdrawn for reasons of safety or effectiveness; or (II) the Secretary makes a written determination that the prior determination must be changed because an error has been identified. (iv) If the Secretary makes a written determination described in clause (iii)(II), the Secretary shall provide notice and a copy of the written determination to the person making the request under clause (i). (v) The disclosures authorized under clauses (i) and (ii) are disclosures authorized by law, including for purposes of section 1905 of title 18, United States Code. This subparagraph shall not otherwise be construed to authorize the disclosure of nonpublic qualitative or quantitative information about the ingredients in a listed drug, or to affect the status, if any, of such information as trade secret or confidential commercial information for purposes of section 301(j) of this Act, section 552 of title 5, United States Code, or section 1905 of title 18, United States Code. .\n##### (b) Guidance\n**(1) In general**\nNot later than one year after the date of enactment of this Act, the Secretary of Health and Human Services shall issue draft guidance, or update guidance, describing how the Secretary will determine whether a drug is qualitatively and quantitatively the same as the listed drug (as such terms are used in section 505(j)(3)(H) of the Federal Food, Drug, and Cosmetic Act, as added by subsection (a)), including with respect to assessing pH adjusters.\n**(2) Process**\nIn issuing guidance under this subsection, the Secretary of Health and Human Services shall\u2014\n**(A)**\npublish draft guidance;\n**(B)**\nprovide a period of at least 60 days for comment on the draft guidance; and\n**(C)**\nafter considering any comments received and not later than one year after the close of the comment period on the draft guidance, publish final guidance.\n##### (c) Applicability\nSection 505(j)(3)(H) of the Federal Food, Drug, and Cosmetic Act, as added by subsection (a), applies beginning on the date of enactment of this Act, irrespective of the date on which the guidance required by subsection (b) is finalized.",
      "versionDate": "2025-04-03",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1843",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to increase transparency in generic drug applications.",
      "type": "HR"
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
        "updateDate": "2025-05-05T12:45:32Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1302is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Increasing Transparency in Generic Drug Applications Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Increasing Transparency in Generic Drug Applications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for increased transparency in generic drug applications.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:28Z"
    }
  ]
}
```
