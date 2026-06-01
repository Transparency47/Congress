# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/886
- Title: Beat Bad Bureaucrats Act
- Congress: 119
- Bill type: HR
- Bill number: 886
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-03-24T19:10:56Z
- Update date including text: 2025-03-24T19:10:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/886",
    "number": "886",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "R000619",
        "district": "6",
        "firstName": "Michael",
        "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
        "lastName": "Rulli",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Beat Bad Bureaucrats Act",
    "type": "HR",
    "updateDate": "2025-03-24T19:10:56Z",
    "updateDateIncludingText": "2025-03-24T19:10:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:00:35Z",
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
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "MO"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr886ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 886\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Rulli (for himself, Mr. Graves , and Mr. Webster of Florida ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit the Administrator of the Small Business Administration from garnishing social security benefits with respect to certain named individuals of covered loans who are victims of identity theft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Beat Bad Bureaucrats Act .\n#### 2. Protection of Social Security benefits from garnishment in certain cases of identity theft\n##### (a) In general\nNotwithstanding section 3716(c)(3)(A)(i) of title 31, United States Code, the Administrator may not, with respect to a covered loan, garnish payments made to the named individual of such covered loan under section 202 of the Social Security Act ( 42 U.S.C. 402 et seq. ) for the purposes of repayment of such covered loan.\n##### (b) Exception\nSubsection (a) does not apply if the Administrator determines that the named individual is not a victim of identity theft.\n##### (c) Revision of rule\nNot later than 30 days after the date of the enactment of this Act, the Administrator shall revise section 140.11(e)(1) of title 13, Code of Federal Regulations, to add to the list of notice requirements in such section information about how to report identity theft to the Administrator.\n##### (d) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Small Business Administration.\n**(2) Covered loan**\nThe term covered loan means\u2014\n**(A)**\na loan made under paragraph (36) or (37) of section 7(a) of the Small Business Act ( 15 U.S.C. 636(a) ); or\n**(B)**\na loan made under section 7(b) of such Act ( 15 U.S.C. 636(b) ) in response to COVID\u201319 during the covered period (as defined in section 1110(a) of the CARES Act ( 15 U.S.C. 9009 ).\n**(3) Named individual**\nThe term named individual means an individual\u2014\n**(A)**\nunder whose name a covered loan was fraudulently made; and\n**(B)**\nthat has notified the Administrator, using the procedure posted on a public website of the Small Business Administration, that such individual is a victim of identity theft with respect to such covered loan.",
      "versionDate": "2025-01-31",
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
        "updateDate": "2025-03-04T17:32:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr886",
          "measure-number": "886",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr886v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Beat Bad Bureaucrats Act</strong></p><p>This bill prohibits the Small Business Administration (SBA) from garnishing Social Security payments to victims of identity theft on account of certain delinquent SBA loans obtained fraudulently during the COVID-19 pandemic.\u00a0</p><p>Specifically, the SBA may not garnish an individual\u2019s Social Security payments related to a covered loan if (1) the individual\u2019s name was used to fraudulently obtain the loan, and (2) the individual has reported the identity theft to the SBA. Under the bill, <em>covered loans</em> are Disaster Loans granted in response to COVID-19 between January 31, 2020, and December 31, 2021\u00a0(e.g.,\u00a0Economic Injury Disaster Loans) and loans granted under the Paycheck Protection Program. The prohibition on garnishment does not apply if the SBA determines that an individual is not a victim of identity theft.\u00a0</p><p>Further, the SBA must post instructions on how to report identity theft on its public\u00a0website and include them in the written notice provided to delinquent borrowers before garnishing their pay.\u00a0</p>"
        },
        "title": "Beat Bad Bureaucrats Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr886.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Beat Bad Bureaucrats Act</strong></p><p>This bill prohibits the Small Business Administration (SBA) from garnishing Social Security payments to victims of identity theft on account of certain delinquent SBA loans obtained fraudulently during the COVID-19 pandemic.\u00a0</p><p>Specifically, the SBA may not garnish an individual\u2019s Social Security payments related to a covered loan if (1) the individual\u2019s name was used to fraudulently obtain the loan, and (2) the individual has reported the identity theft to the SBA. Under the bill, <em>covered loans</em> are Disaster Loans granted in response to COVID-19 between January 31, 2020, and December 31, 2021\u00a0(e.g.,\u00a0Economic Injury Disaster Loans) and loans granted under the Paycheck Protection Program. The prohibition on garnishment does not apply if the SBA determines that an individual is not a victim of identity theft.\u00a0</p><p>Further, the SBA must post instructions on how to report identity theft on its public\u00a0website and include them in the written notice provided to delinquent borrowers before garnishing their pay.\u00a0</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr886"
    },
    "title": "Beat Bad Bureaucrats Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Beat Bad Bureaucrats Act</strong></p><p>This bill prohibits the Small Business Administration (SBA) from garnishing Social Security payments to victims of identity theft on account of certain delinquent SBA loans obtained fraudulently during the COVID-19 pandemic.\u00a0</p><p>Specifically, the SBA may not garnish an individual\u2019s Social Security payments related to a covered loan if (1) the individual\u2019s name was used to fraudulently obtain the loan, and (2) the individual has reported the identity theft to the SBA. Under the bill, <em>covered loans</em> are Disaster Loans granted in response to COVID-19 between January 31, 2020, and December 31, 2021\u00a0(e.g.,\u00a0Economic Injury Disaster Loans) and loans granted under the Paycheck Protection Program. The prohibition on garnishment does not apply if the SBA determines that an individual is not a victim of identity theft.\u00a0</p><p>Further, the SBA must post instructions on how to report identity theft on its public\u00a0website and include them in the written notice provided to delinquent borrowers before garnishing their pay.\u00a0</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr886"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr886ih.xml"
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
      "title": "Beat Bad Bureaucrats Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Beat Bad Bureaucrats Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T05:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Administrator of the Small Business Administration from garnishing social security benefits with respect to certain named individuals of covered loans who are victims of identity theft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T05:48:41Z"
    }
  ]
}
```
