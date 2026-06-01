# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/523?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/523
- Title: Protect Medicaid Act
- Congress: 119
- Bill type: S
- Bill number: 523
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-12-05T21:57:06Z
- Update date including text: 2025-12-05T21:57:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/523",
    "number": "523",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Protect Medicaid Act",
    "type": "S",
    "updateDate": "2025-12-05T21:57:06Z",
    "updateDateIncludingText": "2025-12-05T21:57:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T20:30:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s523is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 523\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Cassidy (for himself, Mr. Barrasso , Mr. Wicker , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XIX of the Social Security Act to prohibit Federal Medicaid funding for the administrative costs of providing health benefits to individuals who are unauthorized immigrants.\n#### 1. Short title\nThis Act may be cited as the Protect Medicaid Act .\n#### 2. Prohibiting Federal Medicaid funding for the administrative costs of providing health benefits to individuals who are unauthorized immigrants\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ; and\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amounts expended for the administration of a State program that provides health benefits to noncitizens who are ineligible for medical assistance under this title on the basis of not having a satisfactory immigration status (as defined in section 1137(d)(1)(B)(iii)) (except that such prohibition shall not be construed as prohibiting payment under the preceding provisions of this section for costs attributable to the establishment or operation of a system designed to ensure compliance with such prohibition). .\n#### 3. Inspector General report\nNot later than 180 days after the date of enactment of this Act, the Inspector General of the Department of Health and Human Services shall submit to Congress a report that includes the following information with respect to States that provide health benefits to noncitizens who are ineligible on the basis of immigration status for medical assistance under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ):\n**(1)**\nHow such States separate amounts expended on the administrative costs related to the State's Medicaid program and amounts expended on administrative costs related to providing health benefits to such noncitizens.\n**(2)**\nThe types of procedures, protocols, or systems that such States employ to ensure that they are in full compliance with prohibitions on the use of Federal funding to provide health benefits to such noncitizens and how effective they are at ensuring compliance.\n**(3)**\nA description of States' methods of financing State programs that provide health benefits to noncitizens who are ineligible for medical assistance due to not having a satisfactory immigration status, including through the increased use of provider taxes and intergovernmental transfers to finance the non-Federal share of expenditures under the State Medicaid program for medical assistance provided to individuals who are not so ineligible.\n**(4)**\nAn analysis of\u2014\n**(A)**\nthe extent to which such noncitizens are provided covered outpatient drugs purchased under\u2014\n**(i)**\nthe Medicaid Drug Rebate Program under section 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ); or\n**(ii)**\nthe drug discount program under section 340B of the Public Health Service Act ( 42 U.S.C. 256b ); and\n**(B)**\nthe effect that the provision to such noncitizens of covered outpatient drugs purchased under the programs described in subparagraph (A) has on the average manufacturer price (as defined in section 1927(k)(1) of the Social Security Act ( 42 U.S.C. 1396r\u20138(k)(1) )) of such drugs, including whether the average manufacturer price for such drugs would be lower if no drugs purchased under such programs were provided to such noncitizens.",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-11",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1195",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Protect Medicaid Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-05-02T14:51:10Z"
          },
          {
            "name": "Immigrant health and welfare",
            "updateDate": "2025-05-02T14:51:10Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-05-02T14:51:10Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-05-02T14:51:10Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-05-02T14:51:10Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-05-02T14:51:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T17:37:25Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s523",
          "measure-number": "523",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-03-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s523v00",
            "update-date": "2025-03-20"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Protect Medicaid Act</b></p> <p>This bill prohibits federal payment under Medicaid for the administrative costs of providing health benefits to noncitizens who are ineligible for Medicaid based on their immigration status. The Department of Health and Human Services must report on specified information regarding states that provide health benefits to such individuals.</p>"
        },
        "title": "Protect Medicaid Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s523.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protect Medicaid Act</b></p> <p>This bill prohibits federal payment under Medicaid for the administrative costs of providing health benefits to noncitizens who are ineligible for Medicaid based on their immigration status. The Department of Health and Human Services must report on specified information regarding states that provide health benefits to such individuals.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119s523"
    },
    "title": "Protect Medicaid Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Protect Medicaid Act</b></p> <p>This bill prohibits federal payment under Medicaid for the administrative costs of providing health benefits to noncitizens who are ineligible for Medicaid based on their immigration status. The Department of Health and Human Services must report on specified information regarding states that provide health benefits to such individuals.</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119s523"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s523is.xml"
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
      "title": "Protect Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XIX of the Social Security Act to prohibit Federal Medicaid funding for the administrative costs of providing health benefits to individuals who are unauthorized immigrants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:05Z"
    }
  ]
}
```
