# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/724?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/724
- Title: CBO Show Your Work Act
- Congress: 119
- Bill type: HR
- Bill number: 724
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-12-03T09:06:32Z
- Update date including text: 2025-12-03T09:06:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/724",
    "number": "724",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "CBO Show Your Work Act",
    "type": "HR",
    "updateDate": "2025-12-03T09:06:32Z",
    "updateDateIncludingText": "2025-12-03T09:06:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "KY"
    },
    {
      "bioguideId": "C001039",
      "district": "3",
      "firstName": "Kat",
      "fullName": "Rep. Cammack, Kat [R-FL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Cammack",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MN"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WY"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "LA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "SC"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "AL"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "PA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NY"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NJ"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "GA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "IL"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TX"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "SC"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "NC"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "VA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ND"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "VA"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "SC"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "FL"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "TN"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "KY"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "CO"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AK"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr724ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 724\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Davidson (for himself, Mr. Barr , Mrs. Cammack , Mr. Finstad , Mr. Scott Franklin of Florida , Ms. Hageman , Mr. Higgins of Louisiana , Mr. Mills , Mr. Nehls , Mr. Norman , Mr. Ogles , Mr. Palmer , Mr. Perry , Mr. Rouzer , Mr. Austin Scott of Georgia , Ms. Tenney , Mr. Weber of Texas , Mr. Allen , Mr. Van Drew , Mr. Clyde , Ms. Greene of Georgia , Mr. Gill of Texas , Mrs. Miller of Illinois , Mr. Fallon , Mr. Wilson of South Carolina , Mr. Harris of North Carolina , Mr. McGuire , Ms. Fedorchak , Mr. Cline , Mr. Fry , Mr. Bilirakis , Mr. Rose , and Mr. Massie ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo require the Congressional Budget Office to make publicly available the fiscal and mathematical models, data, and other details of computations used in cost analysis and scoring.\n#### 1. Short title\nThis Act may be cited as the CBO Show Your Work Act .\n#### 2. Publication of Congressional Budget Office models\n##### (a) In general\nSection 402 of the Congressional Budget Act of 1974 ( 2 U.S.C. 653 ) is amended\u2014\n**(1)**\nby striking The Director and inserting the following:\n(a) In general The Director ; and\n**(2)**\nby adding at the end the following:\n(b) Publication of models and data The Director of the Congressional Budget Office shall make available to Members of Congress and make publicly available on the website of the Congressional Budget Office\u2014 (1) each fiscal model, policy model, and data preparation routine used by the Congressional Budget Office in estimating the costs and other fiscal, social, or economic effects of legislation, including estimates prepared under subsection (a); (2) any update of a model or routine described in paragraph (1); (3) subject to paragraph (4), for each estimate of the costs and other fiscal effects of legislation, including estimates prepared under subsection (a), the data, programs, models, assumptions, and other details of the computations used by the Congressional Budget Office in preparing the estimate, in a manner sufficient to permit replication by individuals not employed by the Congressional Budget Office; and (4) for any data that is required not to be disclosed by the Congressional Budget Office\u2014 (A) a complete list of all data variables for such data; (B) descriptive statistics for all data variables for such data (including averages, standard deviations, number of observations, and correlations to other variables), to the extent that the descriptive statistics do not violate the rule against disclosure; (C) a reference to the statute requiring that the data not be disclosed; and (D) information regarding how to contact the individual or entity who has unrestricted access to the data. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply on and after the date that is 6 months after the date of enactment of this Act.",
      "versionDate": "2025-01-24",
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
        "actionDate": "2025-06-17",
        "text": "Read twice and referred to the Committee on the Budget."
      },
      "number": "2090",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Budget Reform Act of 2025",
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
            "name": "Budget process",
            "updateDate": "2025-03-26T19:56:51Z"
          },
          {
            "name": "Congressional Budget Office (CBO)",
            "updateDate": "2025-03-26T19:56:51Z"
          },
          {
            "name": "Congressional agencies",
            "updateDate": "2025-03-26T19:56:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-26T19:56:51Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2025-03-26T19:56:51Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-26T19:56:51Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-03-26T19:56:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-02-27T13:52:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr724",
          "measure-number": "724",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr724v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>CBO Show Your Work Act </b></p> <p>This bill requires the Congressional Budget Office (CBO) to make available to Congress and the public each fiscal model, policy model, and data preparation routine that the CBO uses to estimate the costs and other fiscal, social, or economic effects of legislation. </p> <p>For each estimate of the costs and other fiscal effects of legislation, the CBO must also disclose, in a manner sufficient to permit replication by individuals not employed by the CBO, the data, programs, models, assumptions, and other details of the computations used to prepare the estimate. </p> <p>For data that may not be disclosed, the CBO must make available to Congress and the public</p> <ul> <li> a complete list of all data variables for the data; </li> <li> descriptive statistics for all data variables for the data, to the extent that the descriptive statistics do not violate the rule against disclosure; </li> <li> a reference to the statute requiring that the data not be disclosed; and </li> <li> contact information for the individual or entity who has unrestricted access to the data. </li> </ul>"
        },
        "title": "CBO Show Your Work Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr724.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><b>CBO Show Your Work Act </b></p> <p>This bill requires the Congressional Budget Office (CBO) to make available to Congress and the public each fiscal model, policy model, and data preparation routine that the CBO uses to estimate the costs and other fiscal, social, or economic effects of legislation. </p> <p>For each estimate of the costs and other fiscal effects of legislation, the CBO must also disclose, in a manner sufficient to permit replication by individuals not employed by the CBO, the data, programs, models, assumptions, and other details of the computations used to prepare the estimate. </p> <p>For data that may not be disclosed, the CBO must make available to Congress and the public</p> <ul> <li> a complete list of all data variables for the data; </li> <li> descriptive statistics for all data variables for the data, to the extent that the descriptive statistics do not violate the rule against disclosure; </li> <li> a reference to the statute requiring that the data not be disclosed; and </li> <li> contact information for the individual or entity who has unrestricted access to the data. </li> </ul>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr724"
    },
    "title": "CBO Show Your Work Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p><b>CBO Show Your Work Act </b></p> <p>This bill requires the Congressional Budget Office (CBO) to make available to Congress and the public each fiscal model, policy model, and data preparation routine that the CBO uses to estimate the costs and other fiscal, social, or economic effects of legislation. </p> <p>For each estimate of the costs and other fiscal effects of legislation, the CBO must also disclose, in a manner sufficient to permit replication by individuals not employed by the CBO, the data, programs, models, assumptions, and other details of the computations used to prepare the estimate. </p> <p>For data that may not be disclosed, the CBO must make available to Congress and the public</p> <ul> <li> a complete list of all data variables for the data; </li> <li> descriptive statistics for all data variables for the data, to the extent that the descriptive statistics do not violate the rule against disclosure; </li> <li> a reference to the statute requiring that the data not be disclosed; and </li> <li> contact information for the individual or entity who has unrestricted access to the data. </li> </ul>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr724"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr724ih.xml"
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
      "title": "CBO Show Your Work Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T08:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CBO Show Your Work Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T08:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Congressional Budget Office to make publicly available the fiscal and mathematical models, data, and other details of computations used in cost analysis and scoring.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T08:03:49Z"
    }
  ]
}
```
