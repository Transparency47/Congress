# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/466
- Title: Nuclear Waste Informed Consent Act
- Congress: 119
- Bill type: HR
- Bill number: 466
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-05T21:42:39Z
- Update date including text: 2025-12-05T21:42:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/466",
    "number": "466",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Nuclear Waste Informed Consent Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:42:39Z",
    "updateDateIncludingText": "2025-12-05T21:42:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:04:05Z",
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
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NV"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr466ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 466\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Titus (for herself, Mr. Horsford , and Ms. Lee of Nevada ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Secretary of Energy to obtain the consent of affected State and local governments before making an expenditure from the Nuclear Waste Fund for a nuclear waste repository, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nuclear Waste Informed Consent Act .\n#### 2. Definitions\nIn this Act, the terms affected Indian tribe , affected unit of local government , high-level radioactive waste , repository , Secretary , spent nuclear fuel , and unit of general local government have the meanings given the terms in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 ).\n#### 3. Consent-based approval\n##### (a) In general\nThe Secretary may not make an expenditure from the Nuclear Waste Fund established under section 302(c) of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10222(c) ) for the costs of the activities described in paragraphs (4) and (5) of section 302(d) of that Act ( 42 U.S.C. 10222(d) ) unless the Secretary has entered into an agreement for a repository with\u2014\n**(1)**\nthe Governor of the State in which the repository is proposed to be located;\n**(2)**\neach affected unit of local government;\n**(3)**\nany unit of general local government contiguous to the affected unit of local government if spent nuclear fuel or high-level radioactive waste will be transported through that unit of general local government for disposal at the repository; and\n**(4)**\neach affected Indian tribe.\n##### (b) Conditions on agreement\nAny agreement for a repository under this Act\u2014\n**(1)**\nshall be in writing and signed by all parties;\n**(2)**\nshall be binding on the parties; and\n**(3)**\nshall not be amended or revoked except by mutual agreement of the parties.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-01-15",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "101",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Nuclear Waste Informed Consent Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-18T14:38:46Z"
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
          "measure-id": "id119hr466",
          "measure-number": "466",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr466v00",
            "update-date": "2025-04-15"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Nuclear Waste Informed Consent Act</strong></p><p>This bill prohibits the Department of Energy (DOE) from using the Nuclear Waste Fund for certain activities related to radioactive waste disposal unless DOE has entered into a written agreement for a repository with (1) the governor of the\u00a0state in which the proposed repository will be located, (2) affected local governments, (3) local\u00a0governments contiguous to the affected local governments if spent nuclear fuel or high-level radioactive waste will be transported through them for disposal at the repository, and (4) affected Indian tribes.</p>"
        },
        "title": "Nuclear Waste Informed Consent Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr466.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Nuclear Waste Informed Consent Act</strong></p><p>This bill prohibits the Department of Energy (DOE) from using the Nuclear Waste Fund for certain activities related to radioactive waste disposal unless DOE has entered into a written agreement for a repository with (1) the governor of the\u00a0state in which the proposed repository will be located, (2) affected local governments, (3) local\u00a0governments contiguous to the affected local governments if spent nuclear fuel or high-level radioactive waste will be transported through them for disposal at the repository, and (4) affected Indian tribes.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119hr466"
    },
    "title": "Nuclear Waste Informed Consent Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Nuclear Waste Informed Consent Act</strong></p><p>This bill prohibits the Department of Energy (DOE) from using the Nuclear Waste Fund for certain activities related to radioactive waste disposal unless DOE has entered into a written agreement for a repository with (1) the governor of the\u00a0state in which the proposed repository will be located, (2) affected local governments, (3) local\u00a0governments contiguous to the affected local governments if spent nuclear fuel or high-level radioactive waste will be transported through them for disposal at the repository, and (4) affected Indian tribes.</p>",
      "updateDate": "2025-04-15",
      "versionCode": "id119hr466"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr466ih.xml"
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
      "title": "Nuclear Waste Informed Consent Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T13:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nuclear Waste Informed Consent Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T13:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Energy to obtain the consent of affected State and local governments before making an expenditure from the Nuclear Waste Fund for a nuclear waste repository, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T13:33:22Z"
    }
  ]
}
```
