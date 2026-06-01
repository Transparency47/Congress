# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7694?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7694
- Title: Gwenn’s Law
- Congress: 119
- Bill type: HR
- Bill number: 7694
- Origin chamber: House
- Introduced date: 2026-02-25
- Update date: 2026-04-21T17:01:04Z
- Update date including text: 2026-04-21T17:01:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-25: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-25: Introduced in House

## Actions

- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Introduced in House
- 2026-02-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-25",
    "latestAction": {
      "actionDate": "2026-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7694",
    "number": "7694",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Gwenn\u2019s Law",
    "type": "HR",
    "updateDate": "2026-04-21T17:01:04Z",
    "updateDateIncludingText": "2026-04-21T17:01:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-25",
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
      "actionDate": "2026-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-25",
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
          "date": "2026-02-25T14:02:15Z",
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
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CO"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7694ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7694\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2026 Mr. Gottheimer (for himself, Ms. Pettersen , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services to carry out a public awareness campaign to increase participation by women in clinical trials that are conducted or supported by the National Institutes of Health, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gwenn\u2019s Law .\n#### 2. Public awareness campaign to increase participation of women in NIH clinical trials\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Director of the National Institutes of Health (in this section referred to as the Secretary ) shall carry out a public awareness campaign to increase the participation of women in clinical trials conducted or supported by the National Institutes of Health.\n##### (b) Targeted outreach\nIn carrying out the campaign under subsection (a), the Secretary shall increase outreach at hospitals, physicians\u2019 offices, health centers, health care clinics, and other locations that the Secretary determines appropriate.\n##### (c) Priority\nIn carrying out the campaign under subsection (a), the Secretary shall prioritize increasing the participation of women in clinical trials involving research on, and development of, products to prevent, diagnose, or treat rare diseases and conditions.\n##### (d) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $10,000,000 for each of fiscal years 2027 through 2031.\n#### 3. Public awareness campaign to increase awareness of bleeding and clotting disorders in women\n##### (a) In general\nThe Secretary of Health and Human Services shall carry out a public awareness campaign to increase the number of women participating in programs of the Department of Health and Human Services for research, surveillance, and prevention with respect to bleeding and clotting disorders, including hemophilia.\n##### (b) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $10,000,000 for each of fiscal years 2027 through 2031.\n#### 4. Interagency Task Force on Advancing Treatments for Rare Diseases\nPart A of title III of the Public Health Service Act ( 42 U.S.C. 241 et seq. ) is amended by adding at the end the following:\n310C. Interagency Task Force on Advancing Treatments for Rare Diseases (a) In general The Secretary shall maintain a permanent task force, to be known as the Interagency Task Force on Advancing Treatments for Rare Diseases (in this section referred to as the Task Force ). The Secretary shall establish the Task Force not later than 90 days after the date of enactment of the legislation. (b) Composition The Task Force shall be composed of the following members: (1) The Secretary. (2) The Administrator of the Centers for Medicare & Medicaid Services. (3) The Commissioner of Food and Drugs. (4) The Director of the National Institutes of Health. (5) The Director of the Centers for Disease Control and Prevention. (6) Four individuals, to be appointed by the Secretary, who are\u2014 (A) biopharmaceutical innovators with respect to rare diseases and conditions; (B) private health plan administrators; or (C) representatives of institutions or organizations conducting federally funded research with respect to rare diseases and conditions. (7) Four individuals, to be appointed by the Secretary, who are representatives of rare disease advocacy groups. (c) Duties The Task Force shall\u2014 (1) assess\u2014 (A) Federal agency activities concerning rare diseases, including projects involving two or more agencies; (B) overall programmatic funding; and (C) potential measurable outcomes to include in future reports; and (2) coordinate the efforts of the Department of Health and Human Services to incentivize research on, and development of, products for prevention, diagnosis, and treatment with respect to rare diseases and conditions, particularly rare diseases and conditions that disproportionately impact women. .\n#### 5. Action plan for coordinating HHS efforts with respect to certain rare diseases and conditions\n##### (a) In general\nThe Secretary of Health and Human Services shall prepare an action plan for coordinating efforts of the Department of Health and Human Services to incentivize research on, and development of, products for prevention, diagnosis, and treatment with respect to rare diseases and conditions that disproportionately impact women.\n##### (b) Submission and public availability\nNot later than 180 days after the date of enactment of this Act, the Secretary shall\u2014\n**(1)**\ncomplete the action plan required by subsection (a);\n**(2)**\nsubmit such action plan to the Congress; and\n**(3)**\nmake such plan publicly available, including by posting on the websites of the Department of Health and Human Services and the National Institutes of Health.",
      "versionDate": "2026-02-25",
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
        "updateDate": "2026-04-21T17:01:04Z"
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
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7694ih.xml"
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
      "title": "Gwenn\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gwenn\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services to carry out a public awareness campaign to increase participation by women in clinical trials that are conducted or supported by the National Institutes of Health, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T05:33:38Z"
    }
  ]
}
```
