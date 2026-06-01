# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1901?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1901
- Title: Protect LNG Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1901
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-12-05T22:02:05Z
- Update date including text: 2025-12-05T22:02:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1901",
    "number": "1901",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protect LNG Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:02:05Z",
    "updateDateIncludingText": "2025-12-05T22:02:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T19:07:30Z",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "TX"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "MS"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1901is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1901\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Cruz (for himself, Mr. Cornyn , Mr. Wicker , and Mr. Scott of South Carolina ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo address the effect of litigation on applications to export liquefied natural gas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect LNG Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Covered application**\nThe term covered application means an application for\u2014\n**(A)**\nan authorization to export natural gas under section 3(a) of the Natural Gas Act ( 15 U.S.C. 717b(a) ); or\n**(B)**\nan authorization to site, construct, expand, or operate a covered facility under section 3(e) of the Natural Gas Act ( 15 U.S.C. 717b(e) ).\n**(2) Covered facility**\nThe term covered facility means a liquefied natural gas facility for which a proposal to site, construct, expand, or operate is required to be approved by\u2014\n**(A)**\nthe Secretary; and\n**(B)**\n**(i)**\nthe Federal Energy Regulatory Commission; or\n**(ii)**\nthe Maritime Administration.\n**(3) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 3. Effect of litigation on applications to export liquefied natural gas\n##### (a) Effect of litigation\nA civil action relating to an environmental review under the Natural Gas Act ( 15 U.S.C. 717 et seq. ) or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) with respect to a covered facility shall not affect the validity of a permit, license, or approval issued to the covered facility that is the subject of the civil action.\n##### (b) Remand; processing of covered applications\nIf, in a civil action described in subsection (a), the environmental review for a permit, license, or approval issued to the covered facility that is the subject of the civil action is found by the applicable court to violate the Natural Gas Act ( 15 U.S.C. 717 et seq. ) or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. )\u2014\n**(1)**\nnotwithstanding chapter 5 or 7 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ), the applicable court shall not set aside or vacate the permit, license, or approval issued to the covered facility but instead remand the matter to the relevant Federal agency to resolve the violation; and\n**(2)**\nthe relevant Federal agency shall continue to process all covered applications.\n#### 4. Action on covered applications\n##### (a) Judicial review\nExcept for review in the Supreme Court of the United States, the court of appeals of the United States for the circuit in which a covered facility is, or will be, located pursuant to a covered application shall have original and exclusive jurisdiction over any civil action for the review of an order issued by a Federal agency with respect to the covered application.\n##### (b) Expedited review\nThe applicable United States Court of Appeals under subsection (a) shall\u2014\n**(1)**\nset any civil action brought under this subsection for expedited review; and\n**(2)**\nset the action on the docket as soon as practicable after the filing date of the initial pleading.\n##### (c) Transfer of existing actions\nIn the case of a covered application for which a petition for review has been filed as of the date of enactment of this Act, the petition shall be\u2014\n**(1)**\non a motion by the applicant, transferred to the court of appeals of the United States in which the covered facility that is the subject of the covered application is, or will be, located; and\n**(2)**\nadjudicated in accordance with this section.\n##### (d) Limitation on claims\nNotwithstanding any other provision of law, a claim arising under Federal law seeking judicial review of a permit, license, or approval issued by a Federal agency for a covered facility pursuant to a covered application shall be barred unless the claim is filed not later than 90 days after publication of a notice in the Federal Register announcing that the permit, license, or approval is final pursuant to the law under which the agency action is taken, unless a shorter time is specified in the Federal law pursuant to which judicial review is allowed.\n##### (e) Savings clause\nNothing in this section establishes a right to judicial review or places any limit on filing a claim that a person has violated the terms of a permit, license, or approval.",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-09-10",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 14 - 9."
      },
      "number": "3592",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protect LNG Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-09-19T19:48:18Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-19T19:48:18Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-09-19T19:48:18Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-19T19:48:18Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2025-09-19T19:48:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-06-13T12:51:07Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1901is.xml"
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
      "title": "Protect LNG Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect LNG Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address the effect of litigation on applications to export liquefied natural gas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:49Z"
    }
  ]
}
```
