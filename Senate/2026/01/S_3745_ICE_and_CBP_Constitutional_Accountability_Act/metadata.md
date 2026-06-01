# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3745?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3745
- Title: ICE and CBP Constitutional Accountability Act
- Congress: 119
- Bill type: S
- Bill number: 3745
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-25T17:53:18Z
- Update date including text: 2026-02-25T17:53:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3745",
    "number": "3745",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "ICE and CBP Constitutional Accountability Act",
    "type": "S",
    "updateDate": "2026-02-25T17:53:18Z",
    "updateDateIncludingText": "2026-02-25T17:53:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T22:12:07Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3745is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3745\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Merkley (for himself and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo provide a civil remedy for any individual whose rights have been violated by an officer or agent of U.S. Customs and Border Protection or U.S. Immigration and Customs Enforcement.\n#### 1. Short title\nThis Act may be cited as the ICE and CBP Constitutional Accountability Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe First, Fourth, Fifth, and Fourteenth Amendments to the Constitution of the United States were passed by Congress and ratified by the State legislatures to ensure the protection of fundamental rights for the people of the United States.\n**(2)**\nU.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection officers and agents have undermined the fundamental rights guaranteed by those amendments, including\u2014\n**(A)**\nviolating due process;\n**(B)**\nracial profiling based on individuals\u2019 skin color and languages spoken;\n**(C)**\nconducting unreasonable and warrantless searches and seizures; and\n**(D)**\nviolating individuals\u2019 rights to privacy and free speech.\n**(3)**\nThe recent and ongoing reckless conduct by U.S. Immigration and Customs Enforcement and U.S. Customs and Border Protection has resulted in needless injuries, deaths, and public distrust of the Federal Government.\n**(4)**\nCivil suits provide individuals a remedy when their fundamental rights are violated by Government officials.\n#### 3. Civil remedy for victims of unlawful immigration enforcement actions\nChapter 171 of title 28, United States Code (commonly known as the Federal Tort Claims Act ) is amended, in section 2674, by inserting after punitive damages. the following: If, while acting under color of law, an officer or agent of U.S. Customs and Border Protection or U.S. Immigration and Customs Enforcement, or any other person acting under the direction of any such officer or agent, subjects, or causes to be subjected, any individual within the jurisdiction of the United States to the deprivation of any rights, privileges, or immunities secured by the United States Constitution or laws, the United States Government shall be liable to the aggrieved party in an action at law, a suit in equity, or any other proper proceeding for redress, regardless of whether a policy or custom of the Department of Homeland Security caused the violation and without regard to whether the officer, agent or other person was acting consistent with an official policy, practice, or custom. Monetary damages awarded in cases authorized under this paragraph shall be derived from any amounts appropriated under title IX and sections 100051 and 100052 of Public Law 119\u201321 and, if such amounts have been depleted, amounts appropriated pursuant to section 1304 of title 31, United States Code. Section 2675(a) of title 28, United States Code, shall not apply to a civil action authorized under this paragraph. Notwithstanding any other provision of law, in cases authorized under this paragraph, a plaintiff may seek punitive damages. This paragraph shall constitute a waiver of sovereign immunity of the United States with respect to U.S. Customs and Border Protection and U.S. Immigration and Customs Enforcement for any claim brought under this section. Nothing in this paragraph may be construed to limit or preclude any legal, equitable, or other remedy that is otherwise available against an individual officer, agent, or other person. .",
      "versionDate": "2026-01-29",
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
        "actionDate": "2026-01-30",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "7297",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ICE and CBP Constitutional Accountability Act",
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
        "name": "Immigration",
        "updateDate": "2026-02-25T17:53:18Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3745is.xml"
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
      "title": "ICE and CBP Constitutional Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-20T11:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ICE and CBP Constitutional Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-20T11:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide a civil remedy for any individual whose rights have been violated by an officer or agent of U.S. Customs and Border Protection or U.S. Immigration and Customs Enforcement.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-20T11:18:25Z"
    }
  ]
}
```
