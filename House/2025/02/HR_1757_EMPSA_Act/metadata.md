# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1757?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1757
- Title: EMPSA Act
- Congress: 119
- Bill type: HR
- Bill number: 1757
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-05-12T08:05:56Z
- Update date including text: 2026-05-12T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1757",
    "number": "1757",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "EMPSA Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:05:56Z",
    "updateDateIncludingText": "2026-05-12T08:05:56Z"
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
          "date": "2025-02-27T14:13:40Z",
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
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NV"
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
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "ME"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "KS"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "PA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
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
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NH"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1757ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1757\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Valadao (for himself and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVI of the Social Security Act to provide that the supplemental security income benefits of adults with intellectual or developmental disabilities shall not be reduced by reason of marriage.\n#### 1. Short title\nThis Act may be cited as the Eliminating the Marriage Penalty in SSI Act or the EMPSA Act .\n#### 2. Supplemental security income benefits\n##### (a) Eligibility for benefits\nSection 1611(a) of the Social Security Act ( 42 U.S.C. 1382(a) ) is amended by adding at the end the following:\n(4) Notwithstanding paragraphs (1) and (2) of this subsection, each individual who has attained 18 years of age, who is diagnosed with an intellectual or developmental disability, whose income, other than income excluded pursuant to section 1612(b), is at not more than the rate in effect for purposes of paragraph (1)(A) of this subsection, and whose resources, other than resources excluded pursuant to section 1613(a), are not more than the applicable amount in effect for purposes of paragraph (3)(B) of this subsection, shall be an eligible individual for purposes of this title. .\n##### (b) Amount of benefit\nSection 1611(b) of such Act ( 42 U.S.C. 1382(b) ) is amended by adding at the end the following:\n(3) Notwithstanding paragraphs (1) and (2) of this subsection, the benefit under this title for an individual described in subsection (a)(4) of this section, whether or not the individual has an eligible spouse, shall be payable at the rate in effect for purposes of such paragraph (1), reduced by the amount of income, not excluded pursuant to section 1612(b), of the individual. .\n##### (c) Income and resource deeming rules\nSection 1614(f) of such Act ( 42 U.S.C. 1382c(f) ) is amended by adding at the end the following:\n(5) Notwithstanding paragraph (1) of this subsection, for purposes of determining eligibility for, and the amount of, benefits for an individual described in section 1611(a)(4) who is married, the income and resources of the individual is deemed to not include any income or resources of the spouse. .",
      "versionDate": "2025-02-27",
      "versionType": "Introduced in House"
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
        "name": "Social Welfare",
        "updateDate": "2025-03-21T16:35:45Z"
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
          "measure-id": "id119hr1757",
          "measure-number": "1757",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1757v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Eliminating the Marriage Penalty in SSI Act or the EMPSA Act</b></p> <p>This bill excludes a spouse's income and resources when determining eligibility for Supplemental Security Income (SSI), and disregards marital status when calculating the SSI benefit amount, for an adult who has a diagnosed intellectual or developmental disability. (SSI is a federal income supplement program designed to help aged, blind, and disabled individuals with limited income and resources meet basic needs.)</p>"
        },
        "title": "EMPSA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1757.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Eliminating the Marriage Penalty in SSI Act or the EMPSA Act</b></p> <p>This bill excludes a spouse's income and resources when determining eligibility for Supplemental Security Income (SSI), and disregards marital status when calculating the SSI benefit amount, for an adult who has a diagnosed intellectual or developmental disability. (SSI is a federal income supplement program designed to help aged, blind, and disabled individuals with limited income and resources meet basic needs.)</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1757"
    },
    "title": "EMPSA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Eliminating the Marriage Penalty in SSI Act or the EMPSA Act</b></p> <p>This bill excludes a spouse's income and resources when determining eligibility for Supplemental Security Income (SSI), and disregards marital status when calculating the SSI benefit amount, for an adult who has a diagnosed intellectual or developmental disability. (SSI is a federal income supplement program designed to help aged, blind, and disabled individuals with limited income and resources meet basic needs.)</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119hr1757"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1757ih.xml"
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
      "title": "EMPSA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EMPSA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eliminating the Marriage Penalty in SSI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVI of the Social Security Act to provide that the supplemental security income benefits of adults with intellectual or developmental disabilities shall not be reduced by reason of marriage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:38Z"
    }
  ]
}
```
