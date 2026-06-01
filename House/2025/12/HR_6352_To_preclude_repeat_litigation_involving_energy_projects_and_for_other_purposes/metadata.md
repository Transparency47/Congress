# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6352
- Title: CLEAR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6352
- Origin chamber: House
- Introduced date: 2025-12-02
- Update date: 2026-01-07T17:39:31Z
- Update date including text: 2026-01-07T17:39:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-02: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-02: Introduced in House

## Actions

- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Introduced in House
- 2025-12-02 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-02",
    "latestAction": {
      "actionDate": "2025-12-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6352",
    "number": "6352",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001306",
        "district": "12",
        "firstName": "Troy",
        "fullName": "Rep. Balderson, Troy [R-OH-12]",
        "lastName": "Balderson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "CLEAR Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-07T17:39:31Z",
    "updateDateIncludingText": "2026-01-07T17:39:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-02",
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
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-02",
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
          "date": "2025-12-02T15:01:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6352ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6352\nIN THE HOUSE OF REPRESENTATIVES\nDecember 2, 2025 Mr. Balderson introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo preclude repeat litigation involving energy projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Curtailing Litigation Excess and Abuse Reform Act of 2025 or the CLEAR Act of 2025 .\n#### 2. Preclusion of repeat litigation\n##### (a) Definitions\nIn this section:\n**(1) Authorization**\nThe term authorization means any license, permit, approval, finding, determination, or administrative decision issued by an agency and any interagency consultation that is required or authorized under Federal law in order to site, construct, reconstruct, or commence operations of an energy project administered by\u2014\n**(A)**\na Federal agency; or\n**(B)**\nin the case of a State participating in or administering a review required or authorized under Federal law, as applicable, a State agency.\n**(2) Completion**\n**(A) In general**\nThe term completion , with respect to an energy project, means the earlier of\u2014\n**(i)**\nthe date that the energy project commences commercial operation; and\n**(ii)**\nthe date that the energy project begins production or delivery of energy or resources.\n**(B) Exclusion**\nThe term completion , with respect to an energy project, does not include construction activities pertaining to the energy project.\n**(3) Energy project**\nThe term energy project means a project for the development of a facility for\u2014\n**(A)**\nthe generation, transmission, distribution, or storage of electric energy;\n**(B)**\nthe production, processing, transportation, or delivery of fossil fuels, fuels derived from petroleum, or petrochemical feedstocks; or\n**(C)**\nthe extraction, processing, refining, recycling, or transportation of critical minerals essential to energy production, grid reliability, or national security.\n**(4) Legal action**\n**(A) In general**\nThe term legal action means a legal claim brought in a Federal or State court of competent jurisdiction pursuant to applicable law to remand, reverse, rescind, overturn, modify, or otherwise seek judicial relief (including equitable relief) with respect to an authorization for an energy project.\n**(B) Exception**\nThe term legal action does not include a legal claim involving an authorization for an energy project brought by a landowner for the fair market value of property which has been or may be acquired by eminent domain authority exercised pursuant to applicable Federal law.\n##### (b) Preclusion\n**(1) Common nucleus of operative fact**\nFor the purposes of this section and res judicata, an energy project and all associated authorizations for that energy project shall be considered the common nucleus of operative fact giving rise to any legal action under Federal law.\n**(2) Single action rule**\n**(A) In general**\nNotwithstanding any other provision of law, once a legal action or a claim involving any other aspect of an energy project has been finally adjudicated on the record by a court of competent jurisdiction, no subsequent legal action or a claim involving any aspect of an energy project may be brought in any Federal or State court with respect to the same energy project, regardless of\u2014\n**(i)**\nthe identity of the parties;\n**(ii)**\nthe form of relief sought; or\n**(iii)**\nwhether the subsequent legal action or claim challenges a different authorization or agency decision related to the same energy project.\n**(B) Final adjudication**\nA final adjudication under subparagraph (A) includes any judgment, degree, or order issued by a court that disposes of the legal action on the merits and is not subject to appeal.\n**(3) Jurisdiction**\nNo Federal or State court shall have jurisdiction to hear or consider any legal action barred under paragraph (2).\n##### (c) Effect\n**(1) In general**\nThe preclusive effect established pursuant to subsection (b) is solely for the benefit of, and may only be asserted by\u2014\n**(A)**\nthe Federal agency that issued an authorization for the applicable energy project; or\n**(B)**\nthe project sponsor of the applicable energy project.\n**(2) No expansion of rights**\nNothing in this section creates, enlarges, or recognizes any right of action, defense, or claim preclusion on behalf of any party other than\u2014\n**(A)**\nthe Federal agency that issued an authorization for the applicable energy project; and\n**(B)**\nthe project sponsor of the applicable energy project.\n##### (d) Exceptions\nNothing in this section precludes judicial review of\u2014\n**(1)**\na legal action alleging operational violations of Federal or State law occurring after completion of the energy project; or\n**(2)**\nan enforcement action brought by the United States or a State in its sovereign capacity to ensure compliance with applicable law.\n#### 3. Judicial review\n##### (a) Standard of review\nNotwithstanding chapter 7 of title 5, United States Code, in reviewing a legal action, a court may hold that an applicable Federal agency did not adequately comply with the procedural requirements needed to issue the authorization only if the court determines that the applicable Federal agency abused its substantial discretion in complying with the procedural requirements in issuing the authorization.\n##### (b) Role of the court\nA court reviewing a legal action described in subsection (a) shall defer to the applicable Federal agency and may not substitute its judgment for the judgment of the applicable Federal agency regarding factual determinations or the scope of review for issuance of the authorization.\n##### (c) Remand\n**(1) In general**\nIf a court holds that an applicable Federal agency failed to adequately comply with the procedural requirements needed to issue an authorization under subsection (a), the court may only remand the authorization to the Federal agency with\u2014\n**(A)**\nspecific instruction to correct the errors or deficiencies in compliance; and\n**(B)**\na reasonable schedule and deadline, subject to the condition that the deadline may not exceed\u2014\n**(i)**\nwith respect to an order entered on or after the date of enactment of this Act, the date that is 180 days after the date on which the order was entered; and\n**(ii)**\nwith respect to an order entered before the date of enactment of this Act, the date that is 180 days after that date of enactment.\n**(2) Continued effect**\nAn authorization remanded under paragraph (1) shall remain in effect while the Federal agency corrects any errors or deficiencies specified by the court.\n##### (d) Limitations on claims\nNotwithstanding chapter 7 of title 5, United States Code, a legal action described in subsection (a) shall be barred unless\u2014\n**(1)**\nthe legal action is filed not later than 150 days after the date on which the final agency action regarding the applicable authorization is made public, unless a shorter timeline is specified under Federal law; and\n**(2)**\nin the case of an authorization for which there was a public comment period, the legal action\u2014\n**(A)**\nis filed by a party that submitted a substantive and unique comment during a public comment period by the noticed comment deadline and that comment was sufficiently detailed to put the applicable Federal agency on notice of the issue on which the party seeks review and shows that the party would suffer direct harm if the comment was not addressed; and\n**(B)**\nconcerns the same subject matter raised in the comment submitted during the public comment period.",
      "versionDate": "2025-12-02",
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
        "actionDate": "2025-12-02",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3305",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "CLEAR Act of 2025",
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
        "updateDate": "2025-12-17T15:59:52Z"
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
      "date": "2025-12-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6352ih.xml"
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
      "title": "CLEAR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T07:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CLEAR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T07:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Curtailing Litigation Excess and Abuse Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-16T07:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To preclude repeat litigation involving energy projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-16T07:03:18Z"
    }
  ]
}
```
