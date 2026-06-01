# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1195?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1195
- Title: Protect Medicaid Act
- Congress: 119
- Bill type: HR
- Bill number: 1195
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-12-05T21:56:45Z
- Update date including text: 2025-12-05T21:56:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1195",
    "number": "1195",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Protect Medicaid Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:56:45Z",
    "updateDateIncludingText": "2025-12-05T21:56:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
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
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:00:45Z",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "NY"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "WV"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OH"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "KY"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WY"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "IA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "TX"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "UT"
    },
    {
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1195ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1195\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Hudson (for himself and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to prohibit Federal Medicaid funding for the administrative costs of providing health benefits to individuals who are unauthorized immigrants.\n#### 1. Short title\nThis Act may be cited as the Protect Medicaid Act .\n#### 2. Prohibiting Federal Medicaid funding for the administrative costs of providing health benefits to individuals who are unauthorized immigrants\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ; and\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amounts expended for the administration of a State program associated with providing health benefits to noncitizens who are not lawfully admitted permanent residents and are ineligible for medical assistance under this title on the basis of not having a satisfactory immigration status (as defined in section 1137(d)(1)(B)(iii)) (except that such prohibition shall not be construed as prohibiting payment under the preceding provisions of this section for costs attributable to the establishment or operation of a system designed to ensure compliance with such prohibition). .\n#### 3. Inspector General report\nNot later than 180 days after the date of enactment of this Act, the Inspector General of the Department of Health and Human Services shall submit to Congress a report that includes the following information with respect to States that provide health benefits to noncitizens who are not lawfully admitted permanent residents and are ineligible on the basis of immigration status for medical assistance under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ):\n**(1)**\nHow such States separate amounts expended on the administrative costs related to the State's Medicaid program and amounts expended on administrative costs related to providing health benefits to such noncitizens.\n**(2)**\nThe types of procedures, protocols, or systems that such States employ to ensure that they are in full compliance with prohibitions on the use of Federal funding to provide health benefits to such noncitizens and how effective they are at ensuring compliance.\n**(3)**\nA description of States' methods of financing State programs that provide health benefits to such noncitizens who are ineligible for medical assistance due to not having a satisfactory immigration status, including through the increased use of provider taxes and intergovernmental transfers to finance the non-Federal share of expenditures under the State Medicaid program for medical assistance provided to individuals who are not so ineligible.\n**(4)**\nAn analysis of\u2014\n**(A)**\nthe extent to which such noncitizens are provided covered outpatient drugs purchased under\u2014\n**(i)**\nthe Medicaid Drug Rebate Program under section 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ); or\n**(ii)**\nthe drug discount program under section 340B of the Public Health Service Act ( 42 U.S.C. 256b ); and\n**(B)**\nthe effect that the provision to such noncitizens of covered outpatient drugs purchased under the programs described in subparagraph (A) has on the average manufacturer price (as defined in section 1927(k)(1) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(1) )) of such drugs, including whether the average manufacturer price for such drugs would be lower if no drugs purchased under such programs were provided to such noncitizens.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "523",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Medicaid Act",
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
            "name": "Health programs administration and funding",
            "updateDate": "2025-05-02T14:50:32Z"
          },
          {
            "name": "Immigrant health and welfare",
            "updateDate": "2025-05-02T14:50:38Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-05-02T14:50:43Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-05-02T14:50:53Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-05-02T14:50:25Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-05-02T14:50:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T14:23:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1195",
          "measure-number": "1195",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-03-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1195v00",
            "update-date": "2025-03-20"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Protect Medicaid Act</b></p> <p>This bill prohibits federal payment under Medicaid for the administrative costs of providing health benefits to noncitizens who are ineligible for Medicaid based on their immigration status. The Department of Health and Human Services must report on specified information regarding states that provide health benefits to such individuals.</p>"
        },
        "title": "Protect Medicaid Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1195.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Protect Medicaid Act</b></p> <p>This bill prohibits federal payment under Medicaid for the administrative costs of providing health benefits to noncitizens who are ineligible for Medicaid based on their immigration status. The Department of Health and Human Services must report on specified information regarding states that provide health benefits to such individuals.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119hr1195"
    },
    "title": "Protect Medicaid Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Protect Medicaid Act</b></p> <p>This bill prohibits federal payment under Medicaid for the administrative costs of providing health benefits to noncitizens who are ineligible for Medicaid based on their immigration status. The Department of Health and Human Services must report on specified information regarding states that provide health benefits to such individuals.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119hr1195"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1195ih.xml"
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
      "title": "Protect Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:57:53Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to prohibit Federal Medicaid funding for the administrative costs of providing health benefits to individuals who are unauthorized immigrants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T05:18:39Z"
    }
  ]
}
```
