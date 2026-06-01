# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7237?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7237
- Title: Chemical Abortion Risk Awareness Act
- Congress: 119
- Bill type: HR
- Bill number: 7237
- Origin chamber: House
- Introduced date: 2026-01-23
- Update date: 2026-02-12T15:31:07Z
- Update date including text: 2026-02-12T15:31:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-23: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-23: Introduced in House

## Actions

- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Introduced in House
- 2026-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-23",
    "latestAction": {
      "actionDate": "2026-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7237",
    "number": "7237",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001188",
        "district": "3",
        "firstName": "Marlin",
        "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
        "lastName": "Stutzman",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Chemical Abortion Risk Awareness Act",
    "type": "HR",
    "updateDate": "2026-02-12T15:31:07Z",
    "updateDateIncludingText": "2026-02-12T15:31:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-23",
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
      "actionDate": "2026-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-23",
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
          "date": "2026-01-23T15:00:30Z",
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
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-01-23",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7237ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7237\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2026 Mr. Stutzman (for himself and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to ensure that a woman seeking a chemical abortion is made aware of the risks involved, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chemical Abortion Risk Awareness Act .\n#### 2. Chemical abortion risk awareness\nThe Public Health Service Act ( 42 U.S.C. 201 et seq. ) is amended by adding at the end the following:\nXXXIV Chemical abortion risk awareness 3401. Definitions In this title: (1) Chemical abortion The term chemical abortion \u2014 (A) means the use or prescription of an abortion-inducing drug dispensed with the intent to cause the death of the unborn child; and (B) does not include\u2014 (i) separation of the mother and her embryo or fetus to prevent the mother\u2019s death or immediate irreversible bodily harm if such death or harm cannot be mitigated in any other way; (ii) treatment of ectopic or molar pregnancy; and (iii) treatment of miscarriage. (2) Chemical abortion provider The term chemical abortion provider means any person licensed to perform a chemical abortion under applicable Federal and State laws. (3) Unborn child The term unborn child means a member of the species Homo sapiens, at any stage of development prior to birth. (4) Woman The term woman means a human being with XX chromosomes. 3402. Chemical abortion risk awareness (a) Requirement of compliance by providers Effective 30 days after the date of enactment of this title, any chemical abortion provider receiving Federal funds, or working in, for, or on behalf of a medical practice or company that receives Federal funds, who knowingly performs or induces, or attempts to perform or induce, any chemical abortion, shall comply with the requirements of this title. (b) Informed consent A chemical abortion shall not knowingly be performed or induced, or be attempted to be performed or induced, by a chemical abortion provider referred to in subsection (a) unless the chemical abortion provider, not later than 24 hours before the chemical abortion\u2014 (1) provides to the woman, in both electronic and paper form, a full Food and Drug Administration-approved product label for each abortion-inducing drug to be used, with the Warnings and Precautions and Adverse Reactions sections of the label (or such other similar sections) highlighted; (2) reads to the woman the full text of such highlighted sections; and (3) receives confirmation from the woman in writing that the requirements described in paragraphs (1) and (2) have been fulfilled. (c) Implementation plan Not later than 30 days after the date of enactment of this title, a chemical abortion provider referred to in subsection (a) (or the entity that such provider works in, for, or on behalf of) shall submit to the Secretary a plan for implementing the requirements of this title applicable to such provider. 3403. Withholding of Federal funding Notwithstanding any other law, in the case that a chemical abortion provider is not in compliance with the requirements of this title, the Secretary may withhold the Federal funding of the chemical abortion provider, the entity at which the chemical abortion provider is employed or on behalf of which the chemical abortion provider performs or induces chemical abortions, or both. 3404. Private right of action (a) In general A woman or a parent of a woman upon whom an abortion has been performed or induced, or attempted to be performed or induced, by a chemical abortion provider in violation of this title may commence a civil action against the chemical abortion provider for appropriate relief. (b) Appropriate relief Appropriate relief in a civil action under this section includes\u2014 (1) objectively verifiable money damages for all injuries, psychological and physical, occasioned by the violation; (2) statutory damages equal to 3 times the cost of the abortion; and (3) punitive damages. (c) Attorney\u2019s fees for plaintiff The court shall award a reasonable attorney\u2019s fee as part of the costs to a prevailing plaintiff in a civil action under this section. (d) Attorney\u2019s fees for defendant If a defendant in a civil action under this section prevails, and the court finds that the plaintiff\u2019s suit was frivolous, the court shall award a reasonable attorney\u2019s fee in favor of the defendant against the plaintiff. (e) Awards against woman In any civil action under this section, no damages or other monetary relief, and no attorney\u2019s fees except as provided in subsection (d), may be assessed against the woman upon whom the abortion was performed or induced or attempted to be performed or induced. .\n#### 3. Preemption\nNothing in this Act or the amendment made by this Act shall be construed to preempt any provision of State law to the extent that such State law establishes, implements, or continues in effect disclosure requirements regarding abortion or penalties for failure to comply with such requirements that are more extensive than those provided under the amendment made by this Act.\n#### 4. Severability\nIf any provision of this Act or the amendment made by this Act, or any application thereof, is found to be unconstitutional, the remainder of this Act or the amendment made by this Act, and any application thereof, shall not be affected by such finding.",
      "versionDate": "2026-01-23",
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
        "name": "Health",
        "updateDate": "2026-02-12T15:31:06Z"
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
      "date": "2026-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7237ih.xml"
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
      "title": "Chemical Abortion Risk Awareness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Chemical Abortion Risk Awareness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to ensure that a woman seeking a chemical abortion is made aware of the risks involved, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:21Z"
    }
  ]
}
```
