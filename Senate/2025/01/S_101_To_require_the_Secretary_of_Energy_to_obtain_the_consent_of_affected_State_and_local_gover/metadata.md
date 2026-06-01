# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/101
- Title: Nuclear Waste Informed Consent Act
- Congress: 119
- Bill type: S
- Bill number: 101
- Origin chamber: Senate
- Introduced date: 2025-01-15
- Update date: 2025-12-05T21:42:46Z
- Update date including text: 2025-12-05T21:42:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in Senate
- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-01-15: Introduced in Senate

## Actions

- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/101",
    "number": "101",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Nuclear Waste Informed Consent Act",
    "type": "S",
    "updateDate": "2025-12-05T21:42:46Z",
    "updateDateIncludingText": "2025-12-05T21:42:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T19:39:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s101is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 101\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Ms. Cortez Masto (for herself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Secretary of Energy to obtain the consent of affected State and local governments before making an expenditure from the Nuclear Waste Fund for a nuclear waste repository, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nuclear Waste Informed Consent Act .\n#### 2. Definitions\nIn this Act, the terms affected Indian tribe , affected unit of local government , high-level radioactive waste , repository , Secretary , spent nuclear fuel , and unit of general local government have the meanings given the terms in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 ).\n#### 3. Consent-based approval\n##### (a) In general\nThe Secretary may not make an expenditure from the Nuclear Waste Fund established under section 302(c) of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10222(c) ) for the costs of the activities described in paragraphs (4) and (5) of section 302(d) of that Act ( 42 U.S.C. 10222(d) ) unless the Secretary has entered into an agreement for a repository with\u2014\n**(1)**\nthe Governor of the State in which the repository is proposed to be located;\n**(2)**\neach affected unit of local government;\n**(3)**\nany unit of general local government contiguous to the affected unit of local government if spent nuclear fuel or high-level radioactive waste will be transported through that unit of general local government for disposal at the repository; and\n**(4)**\neach affected Indian tribe.\n##### (b) Conditions on agreement\nAny agreement for a repository under this Act\u2014\n**(1)**\nshall be in writing and signed by all parties;\n**(2)**\nshall be binding on the parties; and\n**(3)**\nshall not be amended or revoked except by mutual agreement of the parties.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-01-15",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "466",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nuclear Waste Informed Consent Act",
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
        "name": "Energy",
        "updateDate": "2025-02-13T15:24:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119s101",
          "measure-number": "101",
          "measure-type": "s",
          "orig-publish-date": "2025-01-15",
          "originChamber": "SENATE",
          "update-date": "2025-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s101v00",
            "update-date": "2025-04-15"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Nuclear Waste Informed Consent Act</strong></p><p>This bill prohibits the Department of Energy (DOE) from using the Nuclear Waste Fund for certain activities related to radioactive waste disposal unless DOE has entered into a written agreement for a repository with (1) the governor of the\u00a0state in which the proposed repository will be located, (2) affected local governments, (3) local\u00a0governments contiguous to the affected local governments if spent nuclear fuel or high-level radioactive waste will be transported through them for disposal at the repository, and (4) affected Indian tribes.</p>"
        },
        "title": "Nuclear Waste Informed Consent Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s101.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nuclear Waste Informed Consent Act</strong></p><p>This bill prohibits the Department of Energy (DOE) from using the Nuclear Waste Fund for certain activities related to radioactive waste disposal unless DOE has entered into a written agreement for a repository with (1) the governor of the\u00a0state in which the proposed repository will be located, (2) affected local governments, (3) local\u00a0governments contiguous to the affected local governments if spent nuclear fuel or high-level radioactive waste will be transported through them for disposal at the repository, and (4) affected Indian tribes.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119s101"
    },
    "title": "Nuclear Waste Informed Consent Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Nuclear Waste Informed Consent Act</strong></p><p>This bill prohibits the Department of Energy (DOE) from using the Nuclear Waste Fund for certain activities related to radioactive waste disposal unless DOE has entered into a written agreement for a repository with (1) the governor of the\u00a0state in which the proposed repository will be located, (2) affected local governments, (3) local\u00a0governments contiguous to the affected local governments if spent nuclear fuel or high-level radioactive waste will be transported through them for disposal at the repository, and (4) affected Indian tribes.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119s101"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s101is.xml"
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
      "title": "Nuclear Waste Informed Consent Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-12T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nuclear Waste Informed Consent Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-12T03:08:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to obtain the consent of affected State and local governments before making an expenditure from the Nuclear Waste Fund for a nuclear waste repository, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-12T03:03:25Z"
    }
  ]
}
```
