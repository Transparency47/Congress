# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1265
- Title: USTR Inspector General Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1265
- Origin chamber: Senate
- Introduced date: 2025-04-02
- Update date: 2025-09-18T18:14:37Z
- Update date including text: 2025-09-18T18:14:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in Senate
- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-02: Introduced in Senate

## Actions

- 2025-04-02 - IntroReferral: Introduced in Senate
- 2025-04-02 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1265",
    "number": "1265",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "USTR Inspector General Act of 2025",
    "type": "S",
    "updateDate": "2025-09-18T18:14:37Z",
    "updateDateIncludingText": "2025-09-18T18:14:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
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
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T20:43:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1265is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1265\nIN THE SENATE OF THE UNITED STATES\nApril 2, 2025 Mr. Gallego introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title 5, United States Code, to establish an Inspector General of the Office of the United States Trade Representative, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USTR Inspector General Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nSection 8 of article I of the Constitution of the United States provides that Congress has the sole power to regulate international trade.\n**(2)**\nCongress established the Office of the United States Trade Representative in the Executive Office of the President under section 141 of the Trade Act of 1974 ( 19 U.S.C. 2171 ) with the primary responsibility for developing, and coordinating implementation of, the international trade policy of the United States.\n**(3)**\nThe United States Trade Representative has primary responsibility for administering a variety of trade statutes and for monitoring the implementation and enforcement of trade agreements.\n**(4)**\nSection 141(c)(1)(F) of the Trade Act of 1974 ( 19 U.S.C. 2171(c)(1)(F) ) states that the United States Trade Representative shall report directly to the President and the Congress regarding, and be responsible to the President and the Congress for the administration of, trade agreements programs .\n#### 3. Establishment of Inspector General of the Office of the United States Trade Representative\n##### (a) Definitions\nSection 401 of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking or the National Reconnaissance Office, and inserting the National Reconnaissance Office, or the Office of the United States Trade Representative, ; and\n**(2)**\nin paragraph (3), by striking or the Director of the National Reconnaissance Office; and inserting the Director of the National Reconnaissance Office; or the United States Trade Representative; .\n##### (b) Appointment of Inspector General\nNot later than 120 days after the date of the enactment of this Act, the President shall appoint an individual to serve as the Inspector General of the Office for the United States Trade Representative in accordance with section 403(a) of title 5, United States Code.",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in Senate"
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-05-14T16:12:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
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
          "measure-id": "id119s1265",
          "measure-number": "1265",
          "measure-type": "s",
          "orig-publish-date": "2025-04-02",
          "originChamber": "SENATE",
          "update-date": "2025-09-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1265v00",
            "update-date": "2025-09-18"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>USTR Inspector General Act of 2025</strong></p><p>This bill requires the President to appoint an Inspector General of the Office of the U.S. Trade Representative (USTR).</p><p>Among other responsibilities, the Inspector General shall (1) conduct and supervise audits and investigations relating to the programs and operations of the USTR, (2) recommend policies for preventing and detecting fraud and abuse in those programs, and (3) provide reports to keep the USTR and Congress informed about problems and deficiencies in those programs and operations.</p>"
        },
        "title": "USTR Inspector General Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1265.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>USTR Inspector General Act of 2025</strong></p><p>This bill requires the President to appoint an Inspector General of the Office of the U.S. Trade Representative (USTR).</p><p>Among other responsibilities, the Inspector General shall (1) conduct and supervise audits and investigations relating to the programs and operations of the USTR, (2) recommend policies for preventing and detecting fraud and abuse in those programs, and (3) provide reports to keep the USTR and Congress informed about problems and deficiencies in those programs and operations.</p>",
      "updateDate": "2025-09-18",
      "versionCode": "id119s1265"
    },
    "title": "USTR Inspector General Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>USTR Inspector General Act of 2025</strong></p><p>This bill requires the President to appoint an Inspector General of the Office of the U.S. Trade Representative (USTR).</p><p>Among other responsibilities, the Inspector General shall (1) conduct and supervise audits and investigations relating to the programs and operations of the USTR, (2) recommend policies for preventing and detecting fraud and abuse in those programs, and (3) provide reports to keep the USTR and Congress informed about problems and deficiencies in those programs and operations.</p>",
      "updateDate": "2025-09-18",
      "versionCode": "id119s1265"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1265is.xml"
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
      "title": "USTR Inspector General Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "USTR Inspector General Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 5, United States Code, to establish an Inspector General of the Office of the United States Trade Representative, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:48:37Z"
    }
  ]
}
```
