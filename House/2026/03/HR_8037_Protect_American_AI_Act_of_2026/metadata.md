# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8037?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8037
- Title: Protect American AI Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8037
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-04-02T15:35:14Z
- Update date including text: 2026-04-02T15:35:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8037",
    "number": "8037",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001322",
        "district": "5",
        "firstName": "Michael",
        "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
        "lastName": "Baumgartner",
        "party": "R",
        "state": "WA"
      }
    ],
    "title": "Protect American AI Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-02T15:35:14Z",
    "updateDateIncludingText": "2026-04-02T15:35:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-24T16:00:50Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8037ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8037\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Mr. Baumgartner introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the effect of litigation on the environmental application process for data centers and associated infrastructure.\n#### 1. Short title\nThis Act may be cited as the Protect American AI Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Covered application**\nThe term covered application means an application for an authorization to site, construct, expand, or operate a\u2014\n**(A)**\ndata center; or\n**(B)**\ncovered infrastructure.\n**(2) Data center**\nThe term data center means any facility that primarily contains electronic equipment used to process, store, or transmit digital information.\n**(3) Covered infrastructure**\nThe term covered infrastructure means any infrastructure, facility, or other project that is primarily constructed, expanded, or operated to support a data center.\n#### 3. Effect of litigation on data center and covered infrastructure applications\n##### (a) Effect of litigation\nA civil action relating to an environmental review under the Natural Gas Act ( 15 U.S.C. 717 et seq. ), the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ), the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), sections 10 and 14 of the Act of March 3, 1899 ( 33 U.S.C. 403 ; 408), the Clean Air Act ( 42 U.S.C. 7401 et seq. ), or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) with respect to a data center or covered infrastructure shall not affect the validity of a permit, license, or approval issued for the data center or covered infrastructure that is the subject of the civil action.\n##### (b) Remand; processing of covered applications\nIf, in a civil action described in subsection (a), the environmental review for a permit, license, or approval issued to the data center or covered infrastructure that is the subject of the civil action is found by the applicable court to violate the Natural Gas Act ( 15 U.S.C. 717 et seq. ), the Federal Water Pollution Control Act ( 33 U.S.C. 1251 et seq. ), the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), sections 10 and 14 of the Act of March 3, 1899 ( 33 U.S.C. 403 ; 408), the Clean Air Act ( 42 U.S.C. 7401 et seq. ), or the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. )\u2014\n**(1)**\nnotwithstanding chapter 5 or 7 of title 5, United States Code (commonly referred to as the Administrative Procedure Act ), the applicable court shall not set aside or vacate the permit, license, or approval issued for the data center or covered infrastructure but instead remand the matter to the relevant Federal agency to resolve the violation; and\n**(2)**\nthe relevant Federal agency shall continue to process all covered applications.\n#### 4. Action on covered applications\n##### (a) Judicial review\nExcept for review in the Supreme Court of the United States, the court of appeals of the United States for the circuit in which a data center or covered infrastructure is, or will be, located pursuant to a covered application shall have original and exclusive jurisdiction over any civil action for the review of an order issued by a Federal agency with respect to the covered application.\n##### (b) Expedited review\nThe applicable United States Court of Appeals under subsection (a) shall\u2014\n**(1)**\nset any civil action brought under this subsection for expedited review; and\n**(2)**\nset the action on the docket as soon as practicable after the filing date of the initial pleading.\n##### (c) Transfer of existing actions\nIn the case of a covered application for which a petition for review has been filed as of the date of enactment of this Act, the petition shall be\u2014\n**(1)**\non a motion by the applicant, transferred to the court of appeals of the United States in which the data center or covered infrastructure that is the subject of the covered application is, or will be, located; and\n**(2)**\nadjudicated in accordance with this section.\n##### (d) Limitation on claims\nNotwithstanding any other provision of law, a claim arising under Federal law seeking judicial review of a permit, license, or approval issued by a Federal agency for a data center or covered infrastructure pursuant to a covered application shall be barred unless the claim is filed not later than 90 days after publication of a notice in the Federal Register announcing that the permit, license, or approval is final pursuant to the law under which the agency action is taken, unless a shorter time is specified in the Federal law pursuant to which judicial review is allowed.\n##### (e) Savings clause\nNothing in this section establishes a right to judicial review or places any limit on filing a claim that a person has violated the terms of a permit, license, or approval.",
      "versionDate": "2026-03-24",
      "versionType": "Introduced in House"
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
        "name": "Law",
        "updateDate": "2026-04-02T15:35:14Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8037ih.xml"
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
      "title": "Protect American AI Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect American AI Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T11:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the effect of litigation on the environmental application process for data centers and associated infrastructure.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T11:18:24Z"
    }
  ]
}
```
