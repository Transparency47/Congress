# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3438?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3438
- Title: HIRRE Prosecutors Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3438
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-02-25T12:03:23Z
- Update date including text: 2026-02-25T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3438",
    "number": "3438",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "HIRRE Prosecutors Act of 2025",
    "type": "S",
    "updateDate": "2026-02-25T12:03:23Z",
    "updateDateIncludingText": "2026-02-25T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
        "item": [
          {
            "date": "2025-12-11T18:00:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-11T18:00:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AK"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "MN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3438is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3438\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Coons (for himself and Ms. Murkowski ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Attorney General to establish a single grant program to make grants to hire prosecutors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Helping Improve Recruitment and Retention Efforts for Prosecutors Act of 2025 or as the HIRRE Prosecutors Act of 2025 .\n#### 2. Authority to make grants for prosecutors\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall establish a program (in this Act referred to as the Program ) to assist a State, territory, unit of local government, or tribal government in hiring prosecutors.\n##### (b) Grant authority\nIn carrying out the Program, the Attorney General may award a grant on a competitive basis in accordance with this section.\n##### (c) Eligible recipients\nThe Attorney General may award a grant under the Program each year to a prosecutor's office of a State, territory, unit of local government, or tribal government that submits an application pursuant to subsection (d).\n##### (d) Application\nTo be eligible for a grant under the Program, an eligible recipient shall submit to the Attorney General an application in such form, at such time, and containing such information as the Attorney General determines to be appropriate.\n##### (e) Eligible projects\nGrant funds awarded under the Program may only be used to hire, retain, and train prosecutors or support staff for a prosecutor's office of a State, territory, unit of local government, or tribal government.\n##### (f) Use of components\nThe Attorney General may use any component of the Department of Justice in carrying out this section.\n##### (g) Preferential consideration of applications for certain grants\nIn awarding grants under this section, the Attorney General may give preferential consideration to an application\u2014\n**(1)**\nto hire and train new prosecutors or support staff for a prosecutor's office of a State, territory, unit of local government, or tribal government;\n**(2)**\nto rehire prosecutors who have been laid off as a result of State, territory, unit of local government, or tribal government budget reductions; and\n**(3)**\nfrom a jurisdiction representing a tribal, remote, or rural area, as defined in section 40002(a) of the Violence Against Women Act of 1994 ( 34 U.S.C. 12291(a) ).\n##### (h) Federal share\n**(1) Federal share**\nThe Federal share of the cost of a project assisted with a grant under the Program shall not exceed 75 percent.\n**(2) Waiver**\nThe Attorney General may waive the 25 percent matching requirement under paragraph (1) upon making a determination that a waiver is equitable in view of the financial circumstances affecting the ability of the eligible recipient to meet that requirement.\n**(3) Nonsupplanting requirement**\nFunds made available under the Program shall not be used to supplant State or local funds, or, in the case of Indian tribal governments, funds awarded by the Bureau of Indian Affairs, but shall be used to increase the amount of funds that would, in the absence of Federal funds received under the Program, be made available from State or local sources, or in the case of Indian tribal governments, from funds supplied by the Bureau of Indian Affairs.\n**(4) Non-Federal costs**\n**(A) In general**\nA State or unit of local or tribal government may use assets received through the assets forfeiture equitable sharing program.\n**(B) Indian tribal governments**\nFunds appropriated by Congress for the activities of any agency of an Indian tribal government or the Bureau of Indian Affairs performing prosecutorial functions on any Indian lands may be used to provide the non-Federal share of the cost of programs or projects funded under this section.\n##### (i) Performance evaluation\n**(1) Monitoring components**\nEach project funded by a grant under the Program shall contain a monitoring component, including the systematic identification and collection of data about activities, accomplishments, and programs undertaken pursuant to the Program.\n**(2) Evaluation components**\nThe Attorney General shall evaluate each project funded by a grant under the Program, individually or as part of a national evaluation.\n**(3) Periodic review and reports**\nThe Attorney General may require a project funded under the Program to submit to the Attorney General the results of the monitoring component and evaluation under paragraphs (1) and (2), respectively, as well as any other information as the Attorney General deems necessary.\n**(4) Revocation or suspension of funding**\nIf the Attorney General determines, as a result of evaluation under this subsection, or otherwise, that a grant under the Program is not in substantial compliance with the terms and requirements of the Program, the Attorney General may revoke or suspend funding of that grant, in whole or in part.\n##### (j) General regulatory authority\nThe Attorney General may promulgate regulations and guidelines to carry out this section.\n##### (k) Authorization of appropriations\nThere are authorized to be appropriated to carry out the Program $10,000,000 for each of the fiscal years 2026 through 2030.",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6666",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "HIRRE Prosecutors Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-08T15:07:48Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3438is.xml"
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
      "title": "HIRRE Prosecutors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HIRRE Prosecutors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping Improve Recruitment and Retention Efforts for Prosecutors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Attorney General to establish a single grant program to make grants to hire prosecutors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:29Z"
    }
  ]
}
```
