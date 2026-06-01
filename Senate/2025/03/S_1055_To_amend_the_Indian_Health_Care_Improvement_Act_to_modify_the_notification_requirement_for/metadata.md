# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1055?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1055
- Title: Indian Health Service Emergency Claims Parity Act
- Congress: 119
- Bill type: S
- Bill number: 1055
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-02-11T15:15:05Z
- Update date including text: 2026-02-11T15:15:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2026-02-04 - Committee: Committee on Indian Affairs. Hearings held.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Indian Affairs.
- 2026-02-04 - Committee: Committee on Indian Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1055",
    "number": "1055",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Indian Health Service Emergency Claims Parity Act",
    "type": "S",
    "updateDate": "2026-02-11T15:15:05Z",
    "updateDateIncludingText": "2026-02-11T15:15:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Indian Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Indian Affairs Committee",
          "systemCode": "slia00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Indian Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
            "date": "2026-02-04T19:15:02Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-13T20:54:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Indian Affairs Committee",
      "systemCode": "slia00",
      "type": "Other"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1055is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1055\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Rounds (for himself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Indian Affairs\nA BILL\nTo amend the Indian Health Care Improvement Act to modify the notification requirement for emergency contract health services for certain beneficiaries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Indian Health Service Emergency Claims Parity Act .\n#### 2. Authorization for emergency contract health services\nSection 406 of the Indian Health Care Improvement Act ( 25 U.S.C. 1646 ) is amended\u2014\n**(1)**\nby striking With respect to and inserting the following:\n(b) Elderly or disabled Indians With respect to ; and\n**(2)**\nby inserting before subsection (b) (as so designated) the following:\n(a) In general Except as provided in subsection (b), with respect to an Indian receiving emergency medical care or services from a non-Service provider or in a non-Service facility under the authority of this Act, the time limitation (as a condition of payment) for notifying the Service of such treatment or admission shall be 15 days. .",
      "versionDate": "2025-03-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Emergency medical services and trauma care",
            "updateDate": "2026-02-11T15:15:04Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-02-11T15:14:53Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-02-11T15:14:58Z"
          },
          {
            "name": "Indian social and development programs",
            "updateDate": "2026-02-11T15:14:35Z"
          },
          {
            "name": "Minority health",
            "updateDate": "2026-02-11T15:14:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Native Americans",
        "updateDate": "2025-05-21T13:49:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-13",
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
          "measure-id": "id119s1055",
          "measure-number": "1055",
          "measure-type": "s",
          "orig-publish-date": "2025-03-13",
          "originChamber": "SENATE",
          "update-date": "2025-07-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1055v00",
            "update-date": "2025-07-30"
          },
          "action-date": "2025-03-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Indian Health Service Emergency Claims Parity Act</strong></p><p>This bill extends from 72 hours to 15 days the time period\u00a0to notify the Purchased/Referred Care (PRC) program of emergency medical care received from a non-Indian Health Service (IHS) medical provider or at a non-IHS medical facility. This bill does not apply to individuals who are elderly or disabled, who continue to have a 30-day notification requirement for emergency services.</p><p>The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. The PRC program pays for medical or dental care that is provided away from an IHS or tribal health care facility. The PRC program must be notified of requests for authorization of payment for health care services from a non-IHS provider.</p><p>Currently in emergency cases, the patient, an individual on behalf of the patient, or the medical care provider must, within 72 hours after the beginning of treatment for the condition or after admission to a health care facility, notify a PRC authorizing official of the need for the emergency medical care. This bill instead allows the patient, other individual, or provider to notify PRC within 15 days of the treatment or admission.</p>"
        },
        "title": "Indian Health Service Emergency Claims Parity Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1055.xml",
    "summary": {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Indian Health Service Emergency Claims Parity Act</strong></p><p>This bill extends from 72 hours to 15 days the time period\u00a0to notify the Purchased/Referred Care (PRC) program of emergency medical care received from a non-Indian Health Service (IHS) medical provider or at a non-IHS medical facility. This bill does not apply to individuals who are elderly or disabled, who continue to have a 30-day notification requirement for emergency services.</p><p>The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. The PRC program pays for medical or dental care that is provided away from an IHS or tribal health care facility. The PRC program must be notified of requests for authorization of payment for health care services from a non-IHS provider.</p><p>Currently in emergency cases, the patient, an individual on behalf of the patient, or the medical care provider must, within 72 hours after the beginning of treatment for the condition or after admission to a health care facility, notify a PRC authorizing official of the need for the emergency medical care. This bill instead allows the patient, other individual, or provider to notify PRC within 15 days of the treatment or admission.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119s1055"
    },
    "title": "Indian Health Service Emergency Claims Parity Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Indian Health Service Emergency Claims Parity Act</strong></p><p>This bill extends from 72 hours to 15 days the time period\u00a0to notify the Purchased/Referred Care (PRC) program of emergency medical care received from a non-Indian Health Service (IHS) medical provider or at a non-IHS medical facility. This bill does not apply to individuals who are elderly or disabled, who continue to have a 30-day notification requirement for emergency services.</p><p>The IHS provides medical and dental services directly to American Indian and Alaska Native patients whenever possible. The PRC program pays for medical or dental care that is provided away from an IHS or tribal health care facility. The PRC program must be notified of requests for authorization of payment for health care services from a non-IHS provider.</p><p>Currently in emergency cases, the patient, an individual on behalf of the patient, or the medical care provider must, within 72 hours after the beginning of treatment for the condition or after admission to a health care facility, notify a PRC authorizing official of the need for the emergency medical care. This bill instead allows the patient, other individual, or provider to notify PRC within 15 days of the treatment or admission.</p>",
      "updateDate": "2025-07-30",
      "versionCode": "id119s1055"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1055is.xml"
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
      "title": "Indian Health Service Emergency Claims Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Indian Health Service Emergency Claims Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Indian Health Care Improvement Act to modify the notification requirement for emergency contract health services for certain beneficiaries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:28Z"
    }
  ]
}
```
