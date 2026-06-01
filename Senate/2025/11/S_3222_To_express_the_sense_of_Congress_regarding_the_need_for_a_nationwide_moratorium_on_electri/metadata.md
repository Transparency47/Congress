# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3222
- Title: Stop Shut-Offs During Shutdowns Act
- Congress: 119
- Bill type: S
- Bill number: 3222
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-04-17T14:18:23Z
- Update date including text: 2026-04-17T14:18:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3222",
    "number": "3222",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Stop Shut-Offs During Shutdowns Act",
    "type": "S",
    "updateDate": "2026-04-17T14:18:23Z",
    "updateDateIncludingText": "2026-04-17T14:18:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
            "date": "2025-11-19T22:18:58Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-19T22:18:58Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IL"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3222is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3222\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Markey (for himself, Mrs. Gillibrand , Mr. Blumenthal , Mr. Wyden , and Ms. Duckworth ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo express the sense of Congress regarding the need for a nationwide moratorium on electric and natural gas utility disconnections during a Government shutdown, to ensure that electric service is not disconnected for electric consumers during certain lapses in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Shut-Offs During Shutdowns Act .\n#### 2. Sense of Congress regarding the need for a nationwide moratorium on electric and natural gas utility disconnections during a Government shutdown\nIt is the sense of Congress that, for the duration of any lapse in interim continuing appropriations or full-year appropriations for the Department of Health and Human Services, each relevant State regulatory authority and each electric or natural gas utility that sells electric energy or natural gas to a consumer should ensure that\u2014\n**(1)**\nno electric or natural gas service to a consumer is terminated based on inability to pay;\n**(2)**\nreasonable efforts are made to safely reconnect electric and natural gas consumers that have lost service;\n**(3)**\nno electric or natural gas consumer is charged for reconnection services;\n**(4)**\nlate fees and other penalties are waived for electric and natural gas consumers; and\n**(5)**\nthere are no increases in cost-of-service to electric and natural gas consumers.\n#### 3. Procedures for termination of electric service\nSection 115(g) of the Public Utility Regulatory Policies Act of 1978 ( 16 U.S.C. 2625(g) ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nby striking such service may not be terminated. in the undesignated matter following subparagraph (B);\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby striking the comma at the end and inserting ; and ; and\n**(ii)**\nby striking (B) he is and inserting the following:\n(ii) is ;\n**(C)**\nin subparagraph (A)\u2014\n**(i)**\nby striking , or at the end and inserting ; or ; and\n**(ii)**\nby striking (A) he is and inserting the following:\n(i) is ; and\n**(D)**\nin the matter preceding clause (i) (as so redesignated)\u2014\n**(i)**\nby striking and such consumer establishes that and inserting if the consumer establishes that the consumer ; and\n**(ii)**\nby striking (2) during any period when termination of service to an electric consumer and inserting the following:\n(B) no electric service to an electric consumer may be terminated during any period in which such termination ;\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nby striking , and at the end and inserting a semicolon; and\n**(B)**\nby striking (1) no and inserting the following:\n(A) no ;\n**(3)**\nin the matter preceding subparagraph (A) (as so redesignated), by striking The procedures and inserting the following:\n(1) Procedures The procedures ;\n**(4)**\nin the undesignated matter following paragraph (1)(B)(ii) (as so redesignated), by striking Such procedures and inserting the following:\n(2) Requirement The procedures under paragraph (1) ;\n**(5)**\nin paragraph (1) (as so redesignated), by adding at the end the following:\n(C) no electric service to an electric consumer may be terminated during any period in which interim continuing appropriations or full-year appropriations are not in effect for the Department of Health and Human Services. ; and\n**(6)**\nby adding at the end the following:\n(3) Recovery of certain costs Costs incurred by an electric utility to comply with paragraph (1)(C) may not be retroactively assessed on electric consumers for whom electric service would have been terminated if not for the requirements of that paragraph, but a State regulatory authority, after notice and an opportunity for comment, may establish an alternative mechanism that permits an electric utility to recover those costs if the State regulatory authority determines that the costs\u2014 (A) are substantial; (B) were prudently incurred; and (C) cannot reasonably be recovered through\u2014 (i) regulated rates or market prices for the electric energy or any services sold by the electric utility; or (ii) any supplemental funding received by the State or electric utility for the purpose of responding to the applicable lapse in appropriations. .",
      "versionDate": "2025-11-19",
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
        "name": "Energy",
        "updateDate": "2025-12-18T17:02:33Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3222is.xml"
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
      "title": "Stop Shut-Offs During Shutdowns Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T14:18:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Shut-Offs During Shutdowns Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to express the sense of Congress regarding the need for a nationwide moratorium on electric and natural gas utility disconnections during a Government shutdown, to ensure that electric service is not disconnected for electric consumers during certain lapses in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:18:39Z"
    }
  ]
}
```
