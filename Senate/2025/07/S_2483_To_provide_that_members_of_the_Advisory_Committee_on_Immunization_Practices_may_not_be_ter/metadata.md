# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2483?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2483
- Title: A bill to provide that members of the Advisory Committee on Immunization Practices may not be terminated except for cause and to require the immediate reinstatement of the members of such advisory committee.
- Congress: 119
- Bill type: S
- Bill number: 2483
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-12-02T21:03:03Z
- Update date including text: 2025-12-02T21:03:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2483",
    "number": "2483",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001303",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
        "lastName": "Blunt Rochester",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A bill to provide that members of the Advisory Committee on Immunization Practices may not be terminated except for cause and to require the immediate reinstatement of the members of such advisory committee.",
    "type": "S",
    "updateDate": "2025-12-02T21:03:03Z",
    "updateDateIncludingText": "2025-12-02T21:03:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-28",
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
          "date": "2025-07-28T22:30:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NM"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "GA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2483is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2483\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Ms. Blunt Rochester (for herself, Mr. Luj\u00e1n , Mr. Warnock , Mr. Heinrich , Mr. Merkley , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide that members of the Advisory Committee on Immunization Practices may not be terminated except for cause and to require the immediate reinstatement of the members of such advisory committee.\n#### 1. Membership of the Advisory Committee on Immunization Practices\n##### (a) Requirements for termination of members of ACIP\n**(1) In general**\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) may only terminate a member of the Advisory Committee on Immunization Practices (referred to in this section as the Advisory Committee ) for cause and after notice and opportunity for hearing.\n**(2) Justification for termination**\nIf the Secretary terminates a member of the Advisory Committee for cause as described in paragraph (1), not later than 1 day after the date of such termination, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, and make publicly available, a written justification for such termination.\n**(3) Effect on Federal employees**\nWith respect to a member of the Advisory Committee who is also an employee of the Federal Government, a termination for cause as described in paragraph (1) shall apply only with respect to the membership of the individual as such a member and may not be construed to modify or otherwise impact any protection available to the individual in the capacity of the individual as such an employee.\n**(4) Definition of for cause**\nIn this subsection, the term for cause , with respect to a termination of a member of the Advisory Committee, means a termination based on inefficiency, neglect of duty, or malfeasance in office.\n##### (b) Reinstatement of certain ACIP members\nThe Secretary shall immediately revert to the membership of the Advisory Committee as in effect on June 8, 2025, and such members of such Committee shall serve the remainder of the terms that applied to such members as of June 9, 2025.\n##### (c) Requirements for appointment of members of ACIP\nIn the case of any vacancy in the membership of the Advisory Committee that occurs after the date on which the individuals are reinstated to the Advisory Committee under subsection (b), the Secretary shall appoint a member to fill such vacancy from among individuals recommended by the Comptroller General of the United States.",
      "versionDate": "2025-07-28",
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
        "name": "Health",
        "updateDate": "2025-09-18T18:16:56Z"
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
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2483is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide that members of the Advisory Committee on Immunization Practices may not be terminated except for cause and to require the immediate reinstatement of the members of such advisory committee.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:52Z"
    },
    {
      "title": "A bill to provide that members of the Advisory Committee on Immunization Practices may not be terminated except for cause and to require the immediate reinstatement of the members of such advisory committee.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-29T10:56:22Z"
    }
  ]
}
```
