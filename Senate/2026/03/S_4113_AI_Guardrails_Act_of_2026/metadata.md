# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4113?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4113
- Title: AI Guardrails Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4113
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-03-31T20:35:18Z
- Update date including text: 2026-04-22T16:27:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4113",
    "number": "4113",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001208",
        "district": "",
        "firstName": "Elissa",
        "fullName": "Sen. Slotkin, Elissa [D-MI]",
        "lastName": "Slotkin",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "AI Guardrails Act of 2026",
    "type": "S",
    "updateDate": "2026-03-31T20:35:18Z",
    "updateDateIncludingText": "2026-04-22T16:27:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T18:32:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4113is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4113\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Ms. Slotkin introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo provide for limitations on the use of artificial intelligence by Department of Defense.\n#### 1. Short title\nThis Act may be cited as the AI Guardrails Act of 2026 .\n#### 2. Limitations on use of artificial intelligence by Department of Defense\n##### (a) Sense of Congress\nIt is the sense of Congress that, consistent with America\u2019s AI Action Plan dated July 2025, the United States must aggressively adopt artificial intelligence (AI) within its Armed Forces if it is to maintain its global military preeminence while also ensuring that the Department of Defense\u2019s use of AI is secure and reliable.\n##### (b) Limitations\nThe Department of Defense is prohibited from using artificial intelligence as follows:\n**(1)**\nFor the execution of launching or detonating a nuclear weapon.\n**(2)**\nFor the monitoring, tracking, profiling, or targeting of individuals or groups in the United States, without an individualized, articulable legal basis, regardless of the origin of the data used. In no event may the Department of Defense use AI solely for the purpose of monitoring, tracking, profiling, or targeting activities protected by the First Amendment or the lawful exercise of other rights secured by the Constitution or laws of the United States.\n**(3)**\nIn the employment of lethal force by autonomous weapon systems without appropriate levels of human judgment and supervision. All other uses of artificial intelligence in autonomous weapon systems shall be consistent with Department of Defense Directive 3000.09, Autonomy in Weapon Systems, dated January 25, 2023.\n##### (c) Waiver for certain autonomous weapon systems\n**(1) In general**\nThe Secretary of Defense, without delegation, may waive the prohibitions under subsection (b)(3) with respect to a system for up to one year, or renew such a waiver for up to one year, if the Secretary certifies, in writing, to the congressional defense committees that extraordinary circumstances affecting the national security of the United States require the waiver and that the probability of the system producing a result inconsistent with commander intent does not exceed the documented error rate of trained human operators performing equivalent functions under equivalent conditions.\n**(2) Notifications**\nFor each waiver issued under paragraph (1) with respect to a system, the Secretary of Defense shall notify Congress, including submission of the certification required under such paragraph, not later than 5 days after\u2014\n**(A)**\nthe issuance of a waiver for formal development of such system;\n**(B)**\nthe issuance of a waiver for fielding of such system; and\n**(C)**\nany modification to such system that results in the system algorithms, intended missions sets, intended operational environments, intended target sets, or expected adversarial countermeasures to substantially differ from those granted for previously waived uses.\n**(3) Elements**\nEach notification submitted under paragraph (1) shall include the following elements:\n**(A)**\nThe rationale for the waiver.\n**(B)**\nA description of the autonomous weapon system or technology covered by the waiver.\n**(C)**\nA description of the operational parameters and safeguards for the system, including:\n**(i)**\nAssessments of system performance, capability, reliability, effectiveness, and suitability under realistic conditions.\n**(ii)**\nA description of the associated training, doctrine, and tactics, techniques, and procedures.\n**(iii)**\nThe timeframe and geographic area of intended use.\n**(iv)**\nA description of measures taken to minimize the probability and consequences of unintended engagements or failures.\n**(v)**\nClear procedures for trained operators to activate and deactivate system functions.\n**(vi)**\nPost-deployment continuous monitoring mechanisms.\n**(vii)**\nResults from the realistic system developmental and operational testing and evaluation that demonstrate the probability of the system misidentifying a target, taking unintended action, or producing a result inconsistent with commander intent does not exceed the documented error rate of trained human operators performing equivalent functions under equivalent conditions.\n**(D)**\nThe anticipated duration of the waiver.\n**(4) Form**\nA notification under paragraph (1) shall be submitted in unclassified form, but may include a classified annex, as the Secretary determines necessary.\n##### (d) Artificial intelligence defined\nIn this section, the term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).",
      "versionDate": "2026-03-17",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-03-31T20:35:18Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4113is.xml"
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
      "title": "AI Guardrails Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI Guardrails Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for limitations on the use of artificial intelligence by Department of Defense.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:33Z"
    }
  ]
}
```
