# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/324?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/324
- Title: PPP Shell Company Discovery Act
- Congress: 119
- Bill type: HR
- Bill number: 324
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-02-27T14:05:47Z
- Update date including text: 2025-02-27T14:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/324",
    "number": "324",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "T000480",
        "district": "4",
        "firstName": "William",
        "fullName": "Rep. Timmons, William R. [R-SC-4]",
        "lastName": "Timmons",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "PPP Shell Company Discovery Act",
    "type": "HR",
    "updateDate": "2025-02-27T14:05:47Z",
    "updateDateIncludingText": "2025-02-27T14:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Small Business Committee",
          "systemCode": "hssm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Small Business, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:40:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Small Business Committee",
      "systemCode": "hssm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:39:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr324ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 324\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Timmons introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Small Business , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the collection and sharing of information, including tax return information, for purposes of criminal investigations with respect to loans under the Paycheck Protection Program.\n#### 1. Short title\nThis Act may be cited as the PPP Shell Company Discovery Act .\n#### 2. Collection and sharing of information for criminal investigations with respect to loans under the Paycheck Protection Program\n##### (a) List of loan recipients\nThe Secretary of the Treasury or the Secretary\u2019s delegate (hereafter in this section referred to as the Secretary ), after consultation with the Administrator of the Small Business Administration, the Pandemic Response Accountability Committee, and such other persons as the Secretary determines appropriate, shall compile a list of the persons who received PPP loans. Such list shall include the name, mailing address, and taxpayer identifying number (within the meaning of section 6109 of the Internal Revenue Code of 1986) of, and aggregate amount of PPP loans received by, each such person. The Secretary shall make all information included on such list available to officers and employees of the Internal Revenue Service and the Department of Justice.\n##### (b) Creation of lists of loan recipients based on certain payroll tax information\n**(1) List of loan recipients with no FICA tax withholding**\nThe Commissioner of Internal Revenue shall create a list of PPP loan recipients (including the information described in subsection (a) with respect to each such recipient) which did not deduct and withhold any tax under section 3102 of the Internal Revenue Code of 1986 during calendar year 2019.\n**(2) List of loan recipients with large PPP loans relative to FICA wages**\nThe Commissioner of Internal Revenue shall create a list of PPP loan recipients (including the information described in subsection (a) with respect to each such recipient) with respect to whom the aggregate amount of PPP loans received by such person (as reported on the list described in subsection (a)) equals or exceeds the product of\u2014\n**(A)**\nthe greatest amount of wages (as defined in section 3121(a) of the Internal Revenue Code of 1986) for any calendar month during 2019 with respect to which tax was paid by such person under section 3111 of such Code, multiplied by\n**(B)**\n4.\n**(3) Notification of list completion**\nThe Commissioner of Internal Revenue shall notify the Attorney General and the Secretary of the Treasury when each list described in paragraphs (1) and (2) has been completed.\n**(4) Authority to disclose lists for use in criminal investigations**\nFor authority and procedure for disclosure of return information for use in criminal investigations, see section 6103(i)(1) of the Internal Revenue Code of 1986.\n##### (c) Definitions\nFor purposes of this section\u2014\n**(1) PPP loans**\nThe term PPP loan means a covered loan made under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ) that was forgiven under such paragraph (37) or section 7A of such Act ( 15 U.S.C. 636m ).\n**(2) PPP loan recipient**\nThe term PPP loan recipient means any person included on the list compiled by the Secretary under subsection (a).",
      "versionDate": "2025-01-09",
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
        "name": "Commerce",
        "updateDate": "2025-02-10T17:12:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr324",
          "measure-number": "324",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr324v00",
            "update-date": "2025-02-27"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>PPP Shell Company Discovery Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to compile a list of Paycheck Protection Program (PPP) loan recipients whose loans were forgiven under the program.</p><p>Additionally, the IRS must compile (1) a list of such loan recipients who did not withhold payroll taxes in 2019, and (2) a list of loan such recipients for which the aggregate amount of PPP loans exceeded four times the greatest amount of wages paid by the recipient during a calendar month in 2019.</p><p>The IRS must notify the Department of Justice when the lists are complete.</p>"
        },
        "title": "PPP Shell Company Discovery Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr324.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PPP Shell Company Discovery Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to compile a list of Paycheck Protection Program (PPP) loan recipients whose loans were forgiven under the program.</p><p>Additionally, the IRS must compile (1) a list of such loan recipients who did not withhold payroll taxes in 2019, and (2) a list of loan such recipients for which the aggregate amount of PPP loans exceeded four times the greatest amount of wages paid by the recipient during a calendar month in 2019.</p><p>The IRS must notify the Department of Justice when the lists are complete.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr324"
    },
    "title": "PPP Shell Company Discovery Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PPP Shell Company Discovery Act</strong></p><p>This bill requires the Internal Revenue Service (IRS) to compile a list of Paycheck Protection Program (PPP) loan recipients whose loans were forgiven under the program.</p><p>Additionally, the IRS must compile (1) a list of such loan recipients who did not withhold payroll taxes in 2019, and (2) a list of loan such recipients for which the aggregate amount of PPP loans exceeded four times the greatest amount of wages paid by the recipient during a calendar month in 2019.</p><p>The IRS must notify the Department of Justice when the lists are complete.</p>",
      "updateDate": "2025-02-27",
      "versionCode": "id119hr324"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr324ih.xml"
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
      "title": "PPP Shell Company Discovery Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PPP Shell Company Discovery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T09:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the collection and sharing of information, including tax return information, for purposes of criminal investigations with respect to loans under the Paycheck Protection Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T09:03:21Z"
    }
  ]
}
```
