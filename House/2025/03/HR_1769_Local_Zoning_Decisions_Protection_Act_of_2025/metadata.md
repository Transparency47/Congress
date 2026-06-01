# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1769?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1769
- Title: Local Zoning Decisions Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1769
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-05-15T08:07:56Z
- Update date including text: 2026-05-15T08:07:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1769",
    "number": "1769",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "G000565",
        "district": "9",
        "firstName": "Paul",
        "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
        "lastName": "Gosar",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Local Zoning Decisions Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:56Z",
    "updateDateIncludingText": "2026-05-15T08:07:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "WI"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "TX"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TN"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1769ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1769\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Gosar introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo nullify certain regulations and notices of the Department of Housing and Urban Development, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Local Zoning Decisions Protection Act of 2025 .\n#### 2. Nullification of rules and notices\n##### (a) Proposed rule\nThe proposed rule of the Department of Housing and Urban Development entitled Affirmatively Furthering Fair Housing , published in the Federal Register on February 9, 2023 (88 Fed. Reg. 8516; Docket No. FR\u20136250\u2013P\u201301), and any successor rule that is substantially similar to such proposed rule shall have no force or effect.\n##### (b) Interim final rule\nThe interim final rule of the Department of Housing and Urban Development entitled Restoring Affirmatively Furthering Fair Housing Definitions and Certifications , published in the Federal Register on June 10, 2021 (86 Fed. Reg. 30779; Docket No. FR\u20136249\u2013I\u201301), and any successor rule that is substantially similar to such interim final rule shall have no force or effect.\n##### (c) Final rule\nThe final rule of the Department of Housing and Urban Development entitled Affirmatively Furthering Fair Housing , published in the Federal Register on July 16, 2015 (80 Fed. Reg. 42272; Docket No. FR\u20135173\u2013F\u201304), and any successor rule that is substantially similar to such final rule shall have no force or effect.\n##### (d) Notice\nThe notice of the Department of Housing and Urban Development relating to the Affirmatively Furthering Fair Housing Assessment Tool, published in the Federal Register on December 31, 2015 (80 Fed. Reg. 81840; Docket No. FR\u20135173\u2013N\u201307), and any successor notice or rule substantially similar to such notice shall have no force or effect.\n#### 3. Prohibition on use of Federal funds\nNotwithstanding any other provision of law, no Federal funds may be used to design, build, maintain, utilize, or provide access to a Federal database of geospatial information on community racial disparities or disparities in access to affordable housing.\n#### 4. Federalism consultation and report\n##### (a) In general\nThe Secretary of Housing and Urban Development shall jointly consult with State officials, local government officials, and officials of public housing agencies to develop recommendations, consistent with applicable rulings of the Supreme Court of the United States, to further the purposes and policies of the Fair Housing Act.\n##### (b) Consultation requirements\nIn developing the recommendations required under subsection (a), the Secretary shall\u2014\n**(1)**\nprovide State officials, local government officials, and officials of public housing agencies with notice and an opportunity to participate in the consultation process required under subsection (a);\n**(2)**\nseek to consult with State officials, local government officials, and officials of public housing agencies that represent a broad cross-section of regional, economic, and geographic perspectives in the United States;\n**(3)**\nemphasize the importance of collaboration with and among the State officials, local government officials, and officials of public housing agencies;\n**(4)**\nallow for meaningful and timely input by State officials, local government officials, and officials of public housing agencies;\n**(5)**\npromote transparency in the consultation process required under subsection (a); and\n**(6)**\nexplore with State officials, local government officials, and officials of public housing agencies whether Federal objectives under the Fair Housing Act can be attained by means other than through new regulations.\n##### (c) Reports\n**(1) In general**\nNot later than 12 months after the date of the enactment of this Act, the Secretary shall publish in the Federal Register a draft report describing the recommendations developed pursuant to subsection (a).\n**(2) Consensus requirement**\nThe Secretary may include a recommendation in the draft report only if consensus has been reached with regard to the recommendation among the Secretary, the State officials, local government officials, and officials of public housing agencies consulted pursuant to subsection (a).\n**(3) Failure to reach consensus**\nIf the Secretary, State officials, local government officials, and officials of public housing agencies consulted under subsection (a) fail to reach consensus on a regulatory proposal, the draft report shall identify that consensus was not reached and shall describe\u2014\n**(A)**\nthe areas and issues with regard to which consensus was reached;\n**(B)**\nthe areas and issues of continuing disagreement that resulted in the failure to reach consensus; and\n**(C)**\nthe reasons for the continuing disagreements.\n**(4) Public review and comment period**\nThe Secretary shall make the draft report available for public review and comment for a period of not fewer than 180 days.\n**(5) Final report**\nThe Secretary shall, in consultation with the State officials, local government officials, and officials of public housing agencies, address any comments received pursuant to paragraph (4) and shall prepare a final report describing the final results of the consultation process under subsection (a).\n##### (d) Submission of final report\nNot later than 12 months after the date of enactment of this Act, the Secretary shall make publicly available online the final report prepared pursuant to subsection (c)(5).\n##### (e) Definitions\nIn this Act, the following definitions apply:\n**(1) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(2) Local government official**\nThe term local government official means an elected or professional official of a local government or an official of a regional or national organization representing local governments or officials.\n**(3) State official**\nThe term State official means an elected or professional official of a State government or an official of a regional or national organization representing State governments or officials.\n**(4) Public housing agency**\nThe term public housing agency has the meaning given such term in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).",
      "versionDate": "2025-03-03",
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
        "actionDate": "2025-02-26",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1609",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Local Zoning Decisions Protection Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-27",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1174",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Local Zoning Decisions Protection Act of 2025",
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
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Department of Housing and Urban Development",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Housing discrimination",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Housing supply and affordability",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2026-04-15T18:30:18Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-04-15T18:30:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-19T13:20:45Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1769ih.xml"
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
      "title": "Local Zoning Decisions Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Local Zoning Decisions Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To nullify certain regulations and notices of the Department of Housing and Urban Development, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T03:03:21Z"
    }
  ]
}
```
