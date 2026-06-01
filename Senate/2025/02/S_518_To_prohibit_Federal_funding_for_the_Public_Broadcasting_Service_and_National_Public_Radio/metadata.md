# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/518?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/518
- Title: Defund Government-Sponsored Propaganda Act
- Congress: 119
- Bill type: S
- Bill number: 518
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-12-05T21:55:31Z
- Update date including text: 2025-12-05T21:55:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/518",
    "number": "518",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Defund Government-Sponsored Propaganda Act",
    "type": "S",
    "updateDate": "2025-12-05T21:55:31Z",
    "updateDateIncludingText": "2025-12-05T21:55:31Z"
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
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
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
          "date": "2025-02-11T20:25:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s518is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 518\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Lee introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit Federal funding for the Public Broadcasting Service and National Public Radio and to provide for the transfer of certain Federal funds that would have been made available to those organizations to reduce the public debt, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defund Government-Sponsored Propaganda Act .\n#### 2. Prohibition on Federal funding for Public Broadcasting Service and National Public Radio\n##### (a) In general\nAfter the date of enactment of this Act, no Federal funds may, directly or indirectly, be made available to or used to support an organization described in subsection (b), including through the payment of dues to or the purchase of programming from the organization by a public broadcast station using Federal funds received by the station.\n##### (b) Organizations described\nThe organizations described in this subsection are\u2014\n**(1)**\nthe organization known, as of the date of enactment of this Act, as the Public Broadcasting Service ;\n**(2)**\nthe organization known, as of the date of enactment of this Act, as National Public Radio ; and\n**(3)**\nany successor organization to an organization described in paragraph (1) or (2).\n##### (c) Transfer of certain funds To reduce the public debt\nFor fiscal years 2025, 2026, and 2027, the Corporation for Public Broadcasting shall transfer to the account established by section 3113(d) of title 31, United States Code, an amount equal to the sum of the amounts allocated under clauses (ii) and (iii) of section 396(k)(3)(A) of the Communications Act of 1934 ( 47 U.S.C. 396(k)(3)(A) ) that would have been made available to an organization described in subsection (b) but for the prohibition in subsection (a).",
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
      "number": "1216",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Defund Government-Sponsored Propaganda Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-17T15:43:27Z"
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
          "measure-id": "id119s518",
          "measure-number": "518",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s518v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Defund Government-Sponsored Propaganda Act</strong></p><p>This bill prohibits federal funding of the Public Broadcasting Service (PBS), National Public Radio (NPR), and any successor organization to PBS or NPR. The prohibition extends to the payment of dues to or the purchase of programming from PBS or NPR by a public broadcast station using federal funds.\u00a0</p><p>The bill also directs the Corporation for Public Broadcasting to transfer to the Department of the Treasury for the purpose of reducing the public debt an amount equal to certain funding that would have otherwise been provided to PBS or NPR in FY2025-FY2027.</p>"
        },
        "title": "Defund Government-Sponsored Propaganda Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s518.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Defund Government-Sponsored Propaganda Act</strong></p><p>This bill prohibits federal funding of the Public Broadcasting Service (PBS), National Public Radio (NPR), and any successor organization to PBS or NPR. The prohibition extends to the payment of dues to or the purchase of programming from PBS or NPR by a public broadcast station using federal funds.\u00a0</p><p>The bill also directs the Corporation for Public Broadcasting to transfer to the Department of the Treasury for the purpose of reducing the public debt an amount equal to certain funding that would have otherwise been provided to PBS or NPR in FY2025-FY2027.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119s518"
    },
    "title": "Defund Government-Sponsored Propaganda Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Defund Government-Sponsored Propaganda Act</strong></p><p>This bill prohibits federal funding of the Public Broadcasting Service (PBS), National Public Radio (NPR), and any successor organization to PBS or NPR. The prohibition extends to the payment of dues to or the purchase of programming from PBS or NPR by a public broadcast station using federal funds.\u00a0</p><p>The bill also directs the Corporation for Public Broadcasting to transfer to the Department of the Treasury for the purpose of reducing the public debt an amount equal to certain funding that would have otherwise been provided to PBS or NPR in FY2025-FY2027.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119s518"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s518is.xml"
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
      "title": "Defund Government-Sponsored Propaganda Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defund Government-Sponsored Propaganda Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit Federal funding for the Public Broadcasting Service and National Public Radio and to provide for the transfer of certain Federal funds that would have been made available to those organizations to reduce the public debt, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:32Z"
    }
  ]
}
```
