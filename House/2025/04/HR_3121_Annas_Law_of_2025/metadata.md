# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3121
- Title: Anna’s Law of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3121
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2025-11-18T09:05:46Z
- Update date including text: 2025-11-18T09:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3121",
    "number": "3121",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Anna\u2019s Law of 2025",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:46Z",
    "updateDateIncludingText": "2025-11-18T09:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:00:30Z",
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "GA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NC"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "MI"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TX"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "IN"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3121ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3121\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Ms. Schakowsky (for herself, Ms. Kamlager-Dove , Mr. Johnson of Georgia , Mrs. Dingell , and Ms. Ross ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to expand trauma-informed training for law enforcement personnel and emergency medical technicians related to sexual assault, domestic violence, dating violence, and stalking cases, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Anna\u2019s Law of 2025 .\n#### 2. Expanding trauma-informed training for law enforcement personnel and emergency medical technicians related to sexual assault cases\nPart D of title V of the Public Health Service Act ( 42 U.S.C. 290dd et seq. ) is amended by adding at the end the following:\n553. Expanding trauma-informed training for law enforcement personnel and emergency medical technicians related to sexual assault cases (a) In general The Secretary may award grants to eligible entities to establish and expand training for law enforcement personnel and emergency medical technicians\u2014 (1) to increase understanding and awareness of the impact of trauma in sexual assault cases; and (2) to develop and implement strategies for trauma-informed responses and policies in such cases. (b) Period of grants The period of a grant under this section shall be 1 year. (c) Training described The training funded pursuant to subsection (a) shall\u2014 (1) be trauma-informed, evidence-based or demonstrate promising practices and policies, and victim-centered; (2) focus on the circumstances of individuals who\u2014 (A) have experienced sexual assault or other sexual violence, domestic violence, dating violence, or stalking; and (B) have dealt with related trauma in interacting with law enforcement personnel and emergency medical technicians; and (3) include training on\u2014 (A) identifying the impact of trauma on the brain and behavior (B) how contact with law enforcement personnel and emergency medical technicians can cause or lead to retraumatization of sexual assault victims; (C) recognizing how the impact of trauma can influence interactions with law enforcement personnel and emergency medical technicians; (D) identifying tools and strategies to navigate trauma challenges when interacting with survivors of sexual assault, domestic violence, dating violence, and stalking; (E) communicating with survivors in a trauma-informed manner; and (F) how law enforcement personnel and emergency medical technicians can best support victims of sexual assault or other sexual violence during their interactions with law enforcement. (d) Trainer listing The Secretary shall maintain and make available online\u2014 (1) a listing of trainers who provide training described in subsection (c); and (2) make such listing searchable according to the trainer\u2019s\u2014 (A) geographic area; and (B) professional background. (e) Diversity among trainers As a condition on receipt of a grant under this section, an eligible entity shall strive to provide the training funded through the grant by trainers with\u2014 (1) diverse professional backgrounds; and (2) inclusive racial, ethnic, and gender representation. (f) Required number of training hours As a condition on receipt of a grant under this section, an eligible entity shall agree to require\u2014 (1) individuals enrolled in a law enforcement academy (or other initial training for law enforcement personnel) fire academy (or other initial training for fire fighters), and emergency medical services (or other initial training for emergency medical technicians) of such agencies to receive training described in subsection (c) for at least eight hours; and (2) all other law enforcement personnel and emergency medical technicians of such agencies to receive training described in subsection (c) for at least four hours annually. (g) Reports to Congress The Secretary shall collect data and submit annual reports to the Congress on the grant program under this section. Each such report shall include\u2014 (1) the number of eligible entities receiving grants under this section; (2) an evaluation of the effectiveness of such grants in improving trauma-informed training for law enforcement personnel and emergency medical technicians for sexual assault cases; (3) the prosecution of such cases and outcomes of such prosecution; and (4) survivor feedback on their experiences with law enforcement personnel and emergency medical technicians. (h) Definitions In this section: (1) The term eligible entity means\u2014 (A) a State, Tribal, or local law enforcement agency; and (B) a State or local agency overseeing emergency medical services. (2) The term trauma-informed means\u2014 (A) an understanding of the neurological, biological, psychological, and social effects of trauma and violence on an individual; and (B) an understanding of the environment, practices, policies, and infrastructure that may need to be modified to address the prevalence of trauma and its impacts. .",
      "versionDate": "2025-04-30",
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
        "updateDate": "2025-05-21T12:44:56Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3121ih.xml"
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
      "title": "Anna\u2019s Law of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Anna\u2019s Law of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to expand trauma-informed training for law enforcement personnel and emergency medical technicians related to sexual assault, domestic violence, dating violence, and stalking cases, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T11:18:18Z"
    }
  ]
}
```
